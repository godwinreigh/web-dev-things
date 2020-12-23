#my own calculator

numA=float(input("Please enter the number: "))
op=input("Please enter operator (+, -, /, *) ")
numB=float(input("Please enter another number: "))

if op == "+":
    print(numA + numB)
elif op == "-":
    print(numA - numB)
elif op == "/":
    print(numA / numB)
elif op == "*":
    print(numA * numB)
else:
    print("Invalid")
