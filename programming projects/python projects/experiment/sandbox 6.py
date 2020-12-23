#data storer
#collect data from the user
#survey_entry()
#survey
collected_name = []
collected_age = []

def survey_questions2():
    print("Hello")
    print(collected_name)
    print(collected_age)

def survey_questions():
    try:
        required_character_age = 2
        secondQ = input("Please enter your age: ")
        number = (len(secondQ))
        collected_age.append(secondQ)
        if float(secondQ) >= 18:
            survey_questions2()
        elif float(secondQ) <= 18:
            print("You're still early to do this")
            collected_age.remove(secondQ)
            exit()
        elif number <= required_character_age:
            print("INVALID")
            collected_age.remove(secondQ)
            survey_questions()
    except ValueError:
        print("INVALID")
        collected_age.remove(secondQ)
        survey_questions()

def survey_entry():
    a = input("Do you want to enter the survey? (y/n) ").lower()
    if a == 'y':
        name()
    else:
        print("INVALID")
        survey_entry()

def name():
    required_lenght = 8
    firstQ = input("Please enter your name (PLEASE LIMIT TO 8 CHARACTERS) ")
    a = (len(firstQ))
    collected_name.append(firstQ)
    if a < required_lenght:
        survey_questions()
    else:
        print("INVALID PLEASE TRY AGAIN")
        collected_name.remove(firstQ)
        name()
survey_entry()

