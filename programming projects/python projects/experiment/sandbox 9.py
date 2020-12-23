#guessing game
import random
not_done = True
while not not_done:
    print("Let's play a guessing game")
    print("I pick a number from 1 to 10 and you have to guess it.")
    print("You get 3 guesses. All guesses must be from 1 to 10.")
    print("I will tell you if you have to guess higher or lower.")
    print("")
#create a number 1 to 10
    number = random.randit( 1,10)
    not_guessed = True
    #First guess
    not_got_it = True
    while not_got_it:
        guess = int(input("Guess from 1 to 10"))
        if guess < 1 or guess > 10:
            print("Bad guess")
        else:
            not_got_it = False

    if guess == number:
        print("You guessed it correctly")
        not_guessed = False
    elif number < guess:
        print("Guess Lower")
    else:
        print("Guess Higher")

    if not_guessed:
        not_got_it = True
        while not_got_it:
            guess =int(input("Guess 1 to 10"))
            if guess <1 or guess> 10:
                print("bad guess")
            else:
                print("sorry you lost")
            yn = input("Do you want to play again?(Y/N)")
            if yn == 'N':
                not_done = False
                print("Thank you for playing")







