from random import randint
t = ['rock','paper','scissors']

def game():
    run = True
    while run:
        play_count= 0
        attempts = 1
        play_count = (play_count + attempts)
        if play_count == '4':
            try_again = print("You lose try again? (Y/N").upper()
            if try_again == 'Y':
                game()
            else:
                exit()
                run = False
        else:
           pass
        computer = t[randint(0, 2)]
        player = input("Chose Rock, Paper or Scissors ").lower()
        if player == computer:
            print("It's a tie")
            game()
        elif player == 'rock':
            if computer == 'paper':
                print("You lose! " + computer + " covers " + player)
            else:
                print("You win! " + player + " smashes " + computer)
                exit()
        elif player == 'paper':
            if computer == 'scissors':
                print("You lose " + computer + " cuts " + player)
            else:
                print("You win! " + player + " covers " + computer)
                exit()
        elif player == 'scissors':
            if computer == 'rock':
                print("You lose " + computer + " blocks " + player)
            else:
                print("You win!" + player + "cuts" + player)
                exit()
        else:
            print("That's invalid please try again")
            game()

game()
