def restart():
    rest = input("Do you want to play again? (Y/N) ").upper()
    if rest == 'Y':
        thegame()
    elif rest == 'N':
        exit()
    else:
        print("INVALID")
        restart()


import random
engine = random.randint(1, 10)
def thegame():
    try:
        not_got_it = True
        while not_got_it:
            print("You have 3 chances")
            v = int(input("Guess a number: "))
            if engine < v:
                print("Guess Lower")
                not_got_it = False
            elif engine > v:
                print("Guess Higher")
                not_got_it = False
            elif engine == v:
                print("you got it correct")
                restart()
    except ValueError:
        print("INVALID")
            #second attempt
    try:
        not_done = True
        while not_done:
            print("You have 2 chances")
            a = int(input("Guess another number: "))
            if engine < a:
                print("Guess Lower")
                not_done = False
            elif engine > a:
                print("Guess Higher")
                not_done = False
            elif engine == a:
                print("you got it correct")
                restart()
    except ValueError:
        print("INVALID")

    try:
        neversurrender = True
        while neversurrender:
            print("You have only 1 chance")
            c = int(input("Guess another number: "))
            if engine < c:
                print("YOU LOST")
                restart()
            elif engine > c:
                print("YOU LOST")
                restart()
            elif engine == c:
                print("you got it correct")
                restart()
    except ValueError:
        print("INVALID")
thegame()

