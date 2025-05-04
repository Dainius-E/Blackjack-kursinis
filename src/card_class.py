class Card:
    def __init__(self, rank, suit):
        self.rank, self.suit = rank, suit

    def __repr__(self):
        return f"{self.rank}{self.suit}"

    def value(self):
        if self.rank in ['J','Q','K']:
            return [10]
        if self.rank == 'A':
            return [1,11]
        return [int(self.rank)]