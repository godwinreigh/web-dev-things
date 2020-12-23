file = open("C:/Users/godwi/Desktop/test.txt", "w")
file.write("This file has been re-written")
file.close()

file = open("C:/Users/godwi/Desktop/test.txt", "r")
print(file.read())
file.close()
