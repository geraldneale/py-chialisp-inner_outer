# py-chialisp-inner_outer
Chialisp - Inner/Outer Puzzle - Python Driver Study

Purpose
------------   
This project is to study inner and outer puzzles in chialisp using a python3 driver for assistance. I've found this concept challenging when programming chialisp by hand, yet fundamental to understanding how chia blockchain currency exchange works. For example, the standard wallet transaction uses inner puzzles. 

Introduding the python driver helped me to iterate quicker through increasingly complex examples. Once beyond the common stumbling points, like crafting valid solutions for inner puzzles, I began getting the feedback I desired to address some of my bigger picture concerns with chialisp and keep moving forward. 

Using this tool, I hope the simplest version of an inner puzzle construct becomes clearer to debug, analyze and internalize this fundamental technique's potential. I hoped to design it to be easy to clone and use as-is with a single layer inner puzzle example, but the intention is to make the outer puzzle as complex as you want and expand deeper layer into inner-inner puzzles from here.  

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
>>> smart_coin = get_coin("b81fab02112a65a7a762dce9c91ae414d04a5e3875babb05a28b6410eb107333") #change coinID to that outputted by previous command
>>> spend_smart_coin(smart_coin)
```
NOTE: Promised to work on TESTNET10 only. MAINNET usage at your own risk.
