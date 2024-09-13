class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname


class Student(Person):
  pass

s1 = Student("Student", "Namn")
s1.printname()

name = input("What's the name of the person? ")
last = input("What's their last name? ")
p1 = Person(name, last)

print(p1.firstname, p1.lastname)