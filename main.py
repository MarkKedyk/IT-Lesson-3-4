class Student:
    def __init__(self, name, age, height, number):
        self.name = name
        self.age = age
        self.height = height
        self.number = number

    def grow(self, height = 1):
        self.height += height



Mark = Student(name="Mark", age=14, height="250", number="+380 (96) 529 3240")

print("Name - ", Mark.name)
print("Age - ", Mark.age)
print("Height - ", Mark.height)
print("Number - ", Mark.number)

Mark.grow(height="5")
print(Mark.height)