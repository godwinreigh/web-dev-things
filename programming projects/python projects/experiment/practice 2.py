a = input("Please enter your name here ")
b = input("Please enter your age here ")

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name + ' my age is ' + str(self.age))

p1 = Person(a, b)
p1.myfunc()
