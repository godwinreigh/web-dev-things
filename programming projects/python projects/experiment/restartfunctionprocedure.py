def main():
    accounts = []
    username = input("Please enter your username ")
    print(" Welcome " + username)
    accounts.append(username)
    print(accounts)
    accounts = True
    if not accounts:
        print("Invalid")
    else:
        print("What are you looking for today? ")

    # restart button
    restart = input(" Do you want to restart? ").lower()
    if restart == "yes":
        main()

    else:
        print("Come back again ")
        exit()


main()