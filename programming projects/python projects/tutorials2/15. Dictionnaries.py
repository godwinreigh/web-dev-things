#they are really good for:
#super organized data (mini databases)
#fast as hell (constant time)

#sorted dictionary
from collections import OrderedDict









groceries = {'bananas': 5,
             'oranges': 3
             }
print(groceries['bananas'])
#to avoid syntax error that is because the element is not in the list we can use get, but it will result to none
#it is like safety check
print(groceries.get('starberry'))


contacts = {
    'James':{'phone':'123-4567','email':'web@com'},
            'Jane':{'phone':'987-6543','email':'web2@com'''},
}
print(contacts['James'])

# if we want to count words here
sentence = "I like the name Aaron, because the name Aaron is the best."
word_counts = {
    'I': 1,
    'like': 1,
    'the' : 3
}
#I is keys
# 1 is value

word_counts['the'] =  + 1 #to change the value
print(word_counts)

#casting dictionary to list

#the result will be all of the elements contain in dictionary
print(word_counts.items())

#the result will be the only the keys of dictionary
print(word_counts.keys())

#the result will be the only the value of dictionary
print(word_counts.values())

#to delete something from dictionary
word_counts.pop('I')
print(word_counts)

#to remove arbituary element
word_counts.popitem()
print(word_counts)

#to add something in dictionary

word_counts['Aaron'] = 2 #<to add the element 2 times
print(word_counts)

#to wipe entire dictionary
#word_counts.clear()
#print(word_counts)


#to sort the list
print(sorted(list(word_counts.values())))