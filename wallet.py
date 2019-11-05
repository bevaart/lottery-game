class Wallet:

    # class attribute
    tickets = 0

    # instance attribute
    def __init__(self, start_tegoed):
        self.tegoed = start_tegoed
    def betalen(self, bedrag):
        self.tegoed -= bedrag
