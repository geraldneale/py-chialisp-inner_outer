# py-chialisp-inner_outer
Chialisp - Inner/Outer Puzzle - Python Driver Study

Purpose
------------   
This project is to study inner and outer puzzles in chialisp using a python3 driver for assistance. I've found this concept challenging when programming chialisp by hand, yet fundamental to understanding how chia blockchain currency exchange works. For example, the standard wallet transaction uses an inner puzzle. 

Introduding the python driver helped me to iterate quicker through increasingly complex examples. Once beyond the common stumbling points, like crafting valid solutions for inner puzzles, I began getting the feedback I desired to address some of my bigger picture concerns with chialisp and keep moving forward. 

Using this tool, I hope the inner puzzle construct becomes clearer for you to debug, analyze what is going on and internalize this technique's potential. It is designed to be easy to use as-is with a single layer inner puzzle example, but you can add to the outer puzzle as complex as you want and it should just work. Adding inner-inner puzzles should not be too hard either using the code examples therein already.  

Requirements
------------

- A synced Chia node and wallet (XCH)

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
>>> smart_coin=deploy_smart_coin(OUTER_PUZZLE)
>>> spend_smart_coin(smart_coin)
```
NOTE: Promised to work on TESTNET10 only. MAINNET usage at your own risk.
