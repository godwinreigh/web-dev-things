#slicing
digits = [0,1,2,3,4,5,6,7,8,9]
print(digits[2])
#: inside of the parenthesis, you can call 2 or more certain data
print(digits[0:-4])
print(digits[5: ])

#name = "FIRST LAST"
#print(name[0:5])

#Striding is like skipper function to list

print(digits[0:4:2])
print(digits[::-2])
print(digits[5:0:-2])
#- negative is like reverse function to striding

#using for loops in striding
#len means the lenght of the holding string at list
#We have a loop in variable i from digits to 0 - 10
for i in range(len(digits)):
    print(digits[0:i])

for i in range(len(digits)):
    print(digits[i:i + 3])

for i in range(len(digits)-2):
    print(digits[i:i + 3])

window_size2 = 3
for i in range(len(digits)):
    print(digits[i:i + window_size2])

window_size = 5
for i in range(len(digits)-(window_size-1)):
    print(digits[i:i + window_size])