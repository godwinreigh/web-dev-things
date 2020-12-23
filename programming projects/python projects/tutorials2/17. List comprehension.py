names = ['Jennifer', 'Susan', 'Jane', 'Sophie']
l = []
for persons in names:
    l.append(persons)
print(l)

print([person for person in names])

l = []
for persons in names:
    l.append(persons + ' dumped me.')
print(l)

print([person + ' dumped me.' for person in names])
l=[]
movies_and_ratings = {"intersella": 9, "Dark Knights": 8, "50 Shades":3, "50 Shades Darker": 2, "50 Shades Darkest": 1}
for movies in movies_and_ratings:
    if movies_and_ratings[movies] > 6:
        l.append(movies)
print(l)

print([movies for movies in movies_and_ratings if movies_and_ratings[movies]>6])