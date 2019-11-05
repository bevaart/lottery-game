#
# dit is het main python script wat de game gaat runnen, de GUI neerzet, etc...
#

# import modules

# import de andere bestanden/definities
from wallet import *
from lottery import *

# global variables
lottery_count = 0;

# voor nu doen we even een dummy test... DEBUG style zeg maar ;-)
#
player1 = Wallet(60)

print("player1 has a balance of {}" . format(player1.tegoed))
player1.betalen(10)
print("player1 heeft 10 betaald en nu een balance of {}" . format(player1.tegoed))

run_lottery()
