#making ordinary conversasion

print("Goodmorning! ")
greeting = input("Greet him/her? (y/n) ").lower()
if greeting == "y":
    print("Goodmorning too\n")
else:
    print("Shutup\n")

#proceeding to next event

#at school

print(" ------THE BELL RINGS--------\n ")
print(" -------AS THE STUDENTS GO TO THEIR OWN HOME ------\n")

print("Your classmate ask you.")
print("Can I go home with you?")
go_home = input("Should I go with him/her? (y/n) ").lower()
print(   )
if go_home == "y":
    print("Okay, let's go\n")
else:
    a= print("No, thanks I have something to do\n")

#to the next event 3
def event_3():
    print("You asked your sister\n")
    choices_1 = input(
    "A.Ask her that she has something to do.\n"
    "B.Ask her that I need something.\n"
    "C.Ask her to do my assignment.\n"
    "Your choice: \n").upper()

    if choices_1 == "A":
        print("No nothing")
    elif choices_1 == "B":
        print("Here you go")
    elif choices_1 == "C":
        print("You should do it by yourself")
    else:
        print("INVALID\n")
        event_3()

event_3()