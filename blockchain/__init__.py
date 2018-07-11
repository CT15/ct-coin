from datetime import datetime

from block import Block
from transaction import Transaction


def get_timestamp():
    sec_since_epoch = datetime.now().timestamp()
    return datetime.fromtimestamp(sec_since_epoch).strftime("%Y-%m-%d %H:%M:%S")


class Blockchain:
    def __init__(self, difficulty=1, reward=100):
        self.chain = [self.create_genesis_block()]
        self.difficulty = difficulty
        self.pending_transactions = [];
        self.mining_reward = reward

    def create_genesis_block(self):
        return Block(get_timestamp(), [], "0")

    def get_latest_block(self):
        return self.chain[len(self.chain) - 1]

    def mine_pending_transactions(self, mining_reward_address):
        # generation transaction
        self.pending_transactions.insert(0, Transaction(None, mining_reward_address, self.mining_reward))

        block = Block(get_timestamp(), self.pending_transactions, self.get_latest_block().hash)
        block.mine_block(self.difficulty)

        # Reward is halved for every block mined
        self.mining_reward = self.mining_reward / 2

        print(f"Block successfully mined! New mining reward is {self.mining_reward}")
        self.chain.append(block)

        # in preparation to mine the next block
        self.pending_transactions = []

    def create_transaction(self, transaction):
        self.pending_transactions.append(transaction)

    def get_balance_of_address(self, address):
        balance = 0

        for block in self.chain:
            for transaction in block.transactions:
                if transaction.from_address == address:
                    balance -= transaction.amount

                if transaction.to_address == address:
                    balance += transaction.amount

        return balance

    def is_chain_valid():
        for index in range(1, len(self.chain)):
            current_block = self.chain[index]
            previous_block = self.chain[index - 1]

            if current_block.hash != current_block.calculate_hash():
                return False

            if current_block.previous_hash != previous_block.hash:
                return False

        return True
