class Wallet:

    # class attribute
    tickets = 0

    # instance attribute
    def __init__(self, start_tegoed):
        self.tegoed = start_tegoed
    def betalen(self, bedrag):
        self.tegoed -= bedrag

# instantiate the Parrot class
player1 = Wallet(60)


# access the class attributes
print("player1 has a balance of {}" . format(player1.tegoed))
player1.betalen(100)
print("player1 heeft 10 betaald en nu een balance of {}" . format(player1.tegoed))
