import asyncio
from inspect import signature
from blspy import AugSchemeMPL, G2Element, G1Element, PrivateKey
import json
import time
from chia.wallet.puzzles.load_clvm import load_clvm
from chia.rpc.full_node_rpc_client import FullNodeRpcClient
from chia.rpc.wallet_rpc_client import WalletRpcClient
from chia.types.blockchain_format.coin import Coin
from chia.types.blockchain_format.program import Program
from chia.types.blockchain_format.sized_bytes import bytes32
from chia.types.coin_spend import CoinSpend
from chia.types.spend_bundle import SpendBundle
from chia.util.bech32m import encode_puzzle_hash, decode_puzzle_hash
from chia.util.config import load_config
from chia.util.default_root import DEFAULT_ROOT_PATH
from chia.util.ints import uint16, uint64
from chia.wallet.transaction_record import TransactionRecord
from chia.util.hash import std_hash
from chia.util.keychain import Keychain

# # config/config.yaml                                                                                                                                                                                                                                                                                                       
config = load_config(DEFAULT_ROOT_PATH, "config.yaml")
self_hostname = config["self_hostname"] # localhost                                                                                                                                                                                                                                                                          
full_node_rpc_port = config["full_node"]["rpc_port"]
wallet_rpc_port = config["wallet"]["rpc_port"]

pwd = b"hello"
pwd_hash = std_hash(pwd)
target_wallet = "txch1494tus2m74xha2g3yp3jq38adpmsv8acegqytwlxll4ar99tnv7sq0tvss" #change to your wallet address for the value to return to at the end
if target_wallet == "xch1n6meway2mps529suufuetvgscyvh7cff4p2056xzggcu8trg6neszayhnh":
    print("NOTE: Set target_wallet to something other than the default by editing driver.py file, unless you want the funds at the end sent to the author's wallet ;)")
amt = 5000
INNER_PUZZLE = load_clvm("inner-ppc.clsp", package_or_requirement=__name__).curry(pwd_hash,decode_puzzle_hash(target_wallet),amt)
OUTER_PUZZLE = "outer.clsp"
min_fee = 10        #sometimes there is fee pressure on testnet10

#switch ADD_DATA for environment
#ADD_DATA = bytes.fromhex("ccd5bb71183532bff220ba46c268991a3ff07eb358e8255a65c30a2dce0e5fbb") #genesis challenge(works for mainnet)
ADD_DATA = bytes.fromhex("ae83525ba8d1dd3f09b277de18ca3e43fc0af20d20c4b3e92ef2a48bd291ccb2")  #genesis challenge(works for testnet10)
#ADD_DATA = bytes.fromhex("eb8c4d20b322be8d9fddbf9412016bdffe9a2901d7edb0e364e94266d0e095f7")  #genesis challenge(works for simulator0)

def print_json(dict):
    print(json.dumps(dict, sort_keys=True, indent=4))

# # Send from your default wallet on your machine
# # Wallet has to be running, e.g., chia start wallet
async def send_money_async(address, fee=min_fee):
    wallet_id = "1"
    try:
        print(f"sending {amt} to {address} ...")
        # create a wallet client
        wallet_client = await WalletRpcClient.create(
                self_hostname, uint16(wallet_rpc_port), DEFAULT_ROOT_PATH, config
            )
        # send standard transaction
        res = await wallet_client.send_transaction(wallet_id, amt, address, fee)
        tx_id = res.name
        print(f"waiting until transaction {tx_id} is confirmed...")
        # wait until transaction is confirmed
        tx: TransactionRecord = await wallet_client.get_transaction(wallet_id, tx_id)
        while (not tx.confirmed):
            await asyncio.sleep(5)
            tx = await wallet_client.get_transaction(wallet_id, tx_id)
            print(".", end='', flush=True)
        # get coin infos including coin id of the addition with the same puzzle hash
        print(f"\ntx {tx_id} is confirmed.")
        puzzle_hash = decode_puzzle_hash(address)
        coin = next((c for c in tx.additions if c.puzzle_hash == puzzle_hash), None)
        print(f"Coin Info: {coin}")
        return coin
    finally:
        wallet_client.close()
        await wallet_client.await_closed()

#send_money("txch1y9vvu4t3dd03w7gvvq5jn2ff7ckze5jc8uk3ek8fmahwrufw0jtq0wwgw7",100) #for example
def send_money(address, fee=min_fee):
    return asyncio.run(send_money_async(address, fee))

def deploy_smart_coin(clsp_file: str, fee=min_fee):
    s = time.perf_counter()
    # load coins (compiled and serialized, same content as clsp.hex)
    mod = load_clvm(clsp_file, package_or_requirement=__name__).curry(INNER_PUZZLE.get_tree_hash())
    # cdv clsp treehash
    treehash = mod.get_tree_hash()
    # cdv encode - xch->mainnet or txch->testnet10
    if ADD_DATA == bytes.fromhex("ccd5bb71183532bff220ba46c268991a3ff07eb358e8255a65c30a2dce0e5fbb"):
        address = encode_puzzle_hash(treehash, "xch")
    else:
        address = encode_puzzle_hash(treehash, "txch")
    coin = send_money(address, fee)
    elapsed = time.perf_counter() - s
    print(f"deploy {clsp_file} with {amt} mojos to {treehash} in {elapsed:0.2f} seconds.")
    print(f"coin_id: {coin.get_hash().hex()}")

    return coin

def solution_for_inner(pwd) -> Program:
     return Program.to([pwd])


def solution_for_outer(inner_puz, pwd) -> Program:
     return Program.to([inner_puz, solution_for_inner(pwd)])

async def push_tx_async(spend_bundle: SpendBundle):
    try:
        # create a full node client
        full_node_client = await FullNodeRpcClient.create(
                self_hostname, uint16(full_node_rpc_port), DEFAULT_ROOT_PATH, config
            )
        status = await full_node_client.push_tx(spend_bundle)
        return status
    finally:
        full_node_client.close()
        await full_node_client.await_closed()

def push_tx(spend_bundle: SpendBundle): 
    return asyncio.run(push_tx_async(spend_bundle))

def spend_smart_coin(smart_coin: Coin):
    # coin information, puzzle_reveal, and solution
    smart_coin_spend = CoinSpend(
        smart_coin,
       load_clvm(OUTER_PUZZLE, package_or_requirement=__name__).curry(INNER_PUZZLE.get_tree_hash()),
       solution_for_outer(INNER_PUZZLE, pwd)
    )
    #signature                                
    signature = G2Element()     #empty signature
    # SpendBundle
    spend_bundle = SpendBundle(
            # coin spends
            [
                smart_coin_spend
            ],
            # aggregated_signature
            signature,
        )
    json_string=spend_bundle.to_json_dict()    
    print_json(json_string)
    #write to file for reference
    with open('spend_bundle.json', 'w') as outfile:
        json.dump(json_string, outfile)
    outfile.close()    
    status = push_tx(spend_bundle)
    print_json(status)
