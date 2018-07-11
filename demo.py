import argparse
import sys
from random import randint

from blockchain import Blockchain
from transaction import Transaction


def generate_transaction():
    from_address = "address" + str(randint(1, 20))
    to_address = "address" + str(randint(1, 20))
    amount = randint(1, 500)

    return Transaction(from_address, to_address, amount)


def execute(args):
    print("--- START ---")

    ct_coin = Blockchain(args.difficulty, args.reward)

    for _ in range(args.blocks):
        for _ in range(args.transactions):
            transaction = generate_transaction()

            if args.verbose:
                print(f"{transaction.from_address} sends {transaction.amount} coins to {transaction.to_address}")

            ct_coin.create_transaction(transaction)

        print(f"Miner with address {args.miner} started mining...")
        ct_coin.mine_pending_transactions(args.miner)

        print(f"Balance of Miner is {ct_coin.get_balance_of_address(args.miner)}")

    print("---- END ----")


def validate_positive(value):
    if value <= 0:
        msg = f"{value} is not a positive integer"
        raise argparse.ArgumentTypeError(msg)

    return value


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Options for blockchain demo")

    parser.add_argument("-b", "--blocks", type=int, default=2, help="number of blocks mined (positive int)")
    parser.add_argument("-d", "--difficulty", type=int, default=1, help="number of 0s at the beginning of a valid block hash (positive int)")
    parser.add_argument("-m", "--miner", default="calvin-address", help="address of the miner")
    parser.add_argument("-r", "--reward", type=int, default=100, help="reward given to the miner after successfully mining a block (positive int)")
    parser.add_argument("-t", "--transactions", type=int, default=2, help="number of transactions per block (positive int)")
    parser.add_argument("-v", "--verbose", action="store_true", help="print out all transactions")

    args = parser.parse_args()

    validate_positive(args.blocks)
    execute(args)
