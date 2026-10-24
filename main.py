class Animal:
    def __init__(self, name, age, height, Breed):
        self.name = name
        self.age = age
        self.height = height
        self.Breed = Breed

sobaka = Animal(name="sobaka", age=5, height="60", Breed="Mutt")

print("Name - ", sobaka.name)
print("Age - ", sobaka.age)
print("Height - ", sobaka.height)
print("Breed - ", sobaka.Breed)
