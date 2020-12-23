numA = float(input("Please enter a number "))
operator = input("Please print an operator ")
numB = float(input("Please enter the another number "))

if operator == "+":
    print(numA + numB)
elif operator == "-":
    print(numA + numB)
elif operator == "*":
    print(numA * numB)
elif operator == "/":
    print(numA / numB)
else:
    print("INVALID")



#put float so that num1 won't be a string as a result
#It will immediately convert whatever the user inputs into float