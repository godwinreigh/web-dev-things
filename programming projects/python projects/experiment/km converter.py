#km = convert(miles)
#km = 1.6 * miles
#1000 miles = 1km
print("This is mile converter miles to km")
inp = input("What miles are you moving? ")
mile = int(inp)
km = 1000
def mile_converter(mile, km):
    calc = mile / km
    print("You are moving about: ")
    print(calc)
a = mile_converter(mile, km)
print(a)