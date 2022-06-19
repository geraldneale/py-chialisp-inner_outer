# py-chialisp-inner_outer
Chialisp - Inner/Outer Puzzle - Python Driver Study

This project is a study in inner and outer puzzles in chialsip using a python3 driver.

Requirements
------------

- Chia Wallet (XCH)

Install
-------

Create and activate a virtualenv (first two lines), then install.

```
$ git clone https://github.com/geraldneale/py-chialisp-inner_outer.git
$ cd into the directory
$ pip3 install -r requirements.txt
$ python3 -m venv venv
$ source venv/bin/activate
```
Use
---

Run the driver in python interactive mode.

```
$ python3 -i driver.py
```

```
>>> deploy_smart_coin(OUTER_PUZZLE)
>>> smart_coin = get_coin("b81fab02112a65a7a762dce9c91ae414d04a5e3875babb05a28b6410eb107333") #for example
>>> spend_smart_coin(smart_coin)
```
