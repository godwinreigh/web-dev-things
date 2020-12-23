import re

text = "random string. Myname123@website.com. random text. Mycompany123@website.net"

pattern = re.compile("random string")
result = pattern.search(text)
print(result)

pattern= re.compile("[a-zA-Z]+")
result = pattern.search(text)
print(result)

pattern= re.compile("@")
result = pattern.search(text)
print(result)

pattern= re.compile("@website")
result = pattern.search(text)
print(result)

pattern= re.compile("[a-zA-Z0-9]+@[a-zA-Z0-9]+\.[a-zA-Z]+")
result = pattern.search(text)
print(result)
#to get the two email adresses
pattern= re.compile("[a-zA-Z0-9]+@[a-zA-Z0-9]+\.[a-zA-Z]+")
result = pattern.findall(text)
print(result)