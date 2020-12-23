problems = 'pale, nerdy, short, broke'
print(problems)
#but if you want to make list you can use split
#it 's a "delimitter" it is something that goes between things
l = problems.split(", ") #<------list maker
print(l)

#l = problems.split("pale")
#print(l)

#join it will join whole list together up to one string

#joined = ' and '.join(problems)
#print(joined)

joined = ' and '.join(l)
print(joined)

csv = ','.join(l)
print(csv)


