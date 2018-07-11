class Transaction:
    def __init__(self, from_address, to_address, amount):
        self.from_address = from_address
        self.to_address = to_address
        self.amount = amount

    def __repr__(self):
        return f"Transaction({self.from_address}, {self.to_address}, {self.amount})"
