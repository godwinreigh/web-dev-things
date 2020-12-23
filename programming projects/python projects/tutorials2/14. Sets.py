# list use brackets []
# tuples use parenthesis ()
# sets use braces {}
# sets is another way to group bunch together
# but special about them you cannot have duplicate elements on it
# sets can grow and get smaller but cannot duplicate
# it is also unordered so you cannot iterate to it in particular order
# you cast sets into list
# it also used to remove duplicates at list

l = [1,1,1,2,2,2,3,3,3,4,4,4,5,5,5]
s = {'blueberry', 'raspberry'}
s.add('strawberry')
s.add(4)
s.add(4)
print(s)
#to cast list to set
no_duplicate_list = set(l)
print(no_duplicate_list)
#to cast set to list
no_duplicate_set = list(l)
print(no_duplicate_set)
#building like a vendiagram
library_1 = {'Harry Potter', 'Hunger Games', 'Lord of the Rings'}
library_2 = {'Harry Potter', 'Romeo and Juliet'}
# you can add sets together but if it is duplicate it will ignore it
all_books_in_town = library_1.union(library_2)
print(all_books_in_town)
#.intersection is use to get between two list if the element is duplicated
all_books_in_town = library_1.intersection(library_2)
print(all_books_in_town)
#.difference it tells everything in this 2 sets but not for the duplicates
all_books_in_town = library_1.difference(library_2)
print(all_books_in_town)