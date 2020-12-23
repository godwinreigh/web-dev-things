def integer_picker():
    integers = ["1", "2", "3", "4", "5"]
    thechosenumber = [ ]
    numbers = input("Please take any numbers (1,2,3,4,5) ")
    if numbers <="5":
        thechosenumber.append(numbers)
        integers.remove(numbers)
        print(integers)
        print(thechosenumber)
    else:
        print("INVALID TRY AGAIN")
        integer_picker()


integer_picker()