class Person:
  def __init__(self, fname, age):
    self.firstname = fname
    self.age = age

  def have_birthday(self,age):
    self.age = age
  def change_name(self,fname):
    self.firstname = fname 
  def __str__(self):
    return f"Namn: {self.firstname}\nÅlder: {self.age}"

name = input("Namn? ")
age = int(input("Ålder? "))
p1 = Person(name, age)
p2 = Person ("Apa", 2)

print(p2)
p2.have_birthday(p2.age + 1 )
p2.change_name("RÅTTA")
print(p2)
