# tuple is list with strings
t = (1,2,3) #list have brackets while tuple has parenthesis
print(t[0]) # tuples is you can't change it, you can't add and remove elements to it

credit_card1 = (1234123412341234, 'Joe Roggan', 11/20, 123)
credit_card2 = (1234123412341234, 'Joe Roggan', 11/20, 123)

print(credit_card1 + credit_card2)
#because they are well structured you can do like unpacking a tuple
person = ("Nancy", 25, 'pizza')
person2 = ("Joe", 30, 'hotdog')
people =[person ,person2]
(name, age, favfood) =  person
print(name)
print(age)
print(favfood)

name, age, favfood = person2
print(name)

for name in people:
    print(name, age, favfood)
