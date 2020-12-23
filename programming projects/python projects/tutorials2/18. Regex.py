#email address text scripper
#its way to specify different patterns in strings and text so that you can match those certain patterns pick things out
import re

text = 'A random string. Myname123@website.me . some more random text'
#what compile will do is will take string in that describes our pattern or regular expression and will create object from it
pattern = re.compile("A random string.")
result = pattern.search(text)
print(result)
#it stops when it finds the first match

pattern = re.compile("[ABC]")
result = pattern.search(text)
print(result)
#it also matches the capitals if it is either lower and upper
pattern = re.compile("[a-zA-Z]")
result = pattern.search(text)
print(result)

