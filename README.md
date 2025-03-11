# py-chialisp-inner_outer
Chialisp - Inner/Outer Puzzle - Python Driver Study

Purpose
------------   
The goal of this project is to explore and better understand inner and outer puzzles in Chialisp, using a Python 3 driver to facilitate the process. Programming Chialisp manually, especially with inner and outer puzzles, can be complex and challenging. However, these concepts are crucial for understanding how transactions work within the Chia blockchain, particularly when it comes to native currency exchange in this context. For example, the standard transaction utilizes a very early version of the inner puzzle.

By introducing a Python 3 driver, I've been able to iterate quickly through increasingly complex examples to aid comprhension. Once I overcame initial common challenges, such as creating valid solutions for inner puzzles, I was able to gain necessary insights to address broader concerns related to Chialisp and continue making progress. Progress that is not always so easy following the official documentation.

With this tool, I aim to make the inner puzzle structure more accessible for debugging and analysis. It's been designed to be simple enough for beginners to work with on a single-layer inner puzzle. However, the framework is flexible enough to easily extend into more complexity. For example, you can add multiple layers of inner puzzles using the provided code example. The goal is to make it easier to experiment and deepen your understanding of this powerful technique.

Requirements
------------

- A synced Chia node and wallet (XCH)

Install
-------

Download, create and activate a virtualenv.

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
