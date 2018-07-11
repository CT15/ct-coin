# CT Coin

The code is adapted from Michiel Mulders' [code](https://github.com/michielmulders/blockgeeks-build-blockchain-javascript)
on building blockchain with JavaScript.

## About CT Coin
* Initial mining reward value is specified when the blockchain is first created.
* The genesis block is created at the same time as the creation of the blockchain.
* No one mines the genesis block.
* The mining reward is halved for every block mined.

## Python Version
Python 3.6.4

## Demo Instruction
1. Clone the repository (using HTTPS: `git clone https://github.com/CT15/ct-coin.git`)
2. Create and activate virtual environment in the project directory
    ```shell
    $ cd ct-coin
    $ python3.6 -m venv venv
    $ source venv/bin/activate
    ```
3. Run `demo.py`
    ```shell
    $ python demo.py
    ```
4. To deactivate virtual environment:
    ```shell
    $ deactivate
    ```

## Available Options

When running `demo.py`, it is possible to specify extra arguments:

* -b/--blocks => number of blocks mined (positive int), default = 2
* -d/--difficulty => number of 0s at the beginning of a valid block hash (positive int <= 64), default = 1
* -m/--miner => address of the miner, default = "calvin-address"
* -r/--reward => reward given to the miner after successfully mining a block (positive int), default = 100
* -t/--transactions => number of transactions per block (positive int), default = 2
* -v/--verbose => print out all transactions

Examples:
```shell
$ python demo.py -b=3 -d=2 -m=some_address -r=758 -t=5 -v
```
```shell
$ python demo.py --blocks=4 --difficulty=3 -m=some_address --verbose
```
