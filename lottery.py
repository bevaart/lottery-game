# deze functies draaien een loterij

# inputs :
#   welke loten heeft de speler gekocht

# outputs :
#   update van de loterij geschiedenis
#   update van de speler z'n wallet met de winst uit de loterij
#
# we gaan een loterij doen met ballen! we trekken 3 ballen uit een bak met 12 :-)
#

def run_lottery():
    # import modules
    import random

    # eerst maken we een lijst van alle mogelijke lotto getallen
    lotto = range(1,31)

    print("Hello from the lottery! Let's pull some numbers!")
    print "all our lotto numbers are : ", lotto

    for x in range(0, 3):
        # random 1 getal trekken
        result = random.choice(lotto)
        # dat getal uit de lijst halen, je kunt niet 2x hetzelfde getal pakken
        lotto.remove(result)
        print "lotto number", x+1, "is : ", result
