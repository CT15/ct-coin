from hashlib import sha256


class Block:
    def __init__(self, timestamp, transations, previous_hash=""):
        self.timestamp = timestamp
        self.transactions = transations
        self.previous_hash = previous_hash
        self.nonce = 0
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        transactions_string = ""
        for transaction in self.transactions:
            transactions_string += transaction.__repr__()

        return str(sha256((self.previous_hash + self.timestamp + transactions_string + str(self.nonce)).encode()).hexdigest())

    # difficulty is the number of 0s at the beginning of the hash
    def mine_block(self, difficulty):
        while self.hash[:difficulty] != "0" * difficulty:
            self.nonce += 1
            self.hash = self.calculate_hash()

        print(f"BLOCK MINED: {self.hash}")
