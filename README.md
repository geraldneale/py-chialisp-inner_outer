# py-chialisp-inner_outer
Chialisp - Inner/Outer Puzzle - Python Driver Study

Purpose
------------
This project is a study in inner and outer puzzles in chialisp using a python3 driver for assistance. I've found the concept of using inner puzzles challenging to understand when programming chialisp by hand. Using a python driver to iterate quicker I've found that some of the sticking points, especially around crafting valid solutions for inner puzzles, becomes clearer to debug, analyze and internalize this technique's potential.   

Requirements
------------

- A synced Chia wallet (XCH)

Install
-------

Create and activate a virtualenv (first two lines), then install.

```
$ git clone https://github.com/geraldneale/py-chialisp-inner_outer.git
$ cd py-chialisp-inner_outer/
$ python3 -m venv venv
$ source venv/bin/activate
$ pip3 install -r requirements.txt
```
Use
---
Run the driver in python interactive mode.
```
$ python3 -i driver.py
```

```
>>> deploy_smart_coin(OUTER_PUZZLE)
>>> smart_coin = get_coin("b81fab02112a65a7a762dce9c91ae414d04a5e3875babb05a28b6410eb107333") #change coinID to outputted by previous command
>>> spend_smart_coin(smart_coin)
```
NOTE: Promised to work on TESTNET10 only. MAINNET usage at your own risk.
