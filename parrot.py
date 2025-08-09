class parrot:
    species = "Cockateil"
    def __init__(self, name, age):
        self.name = name
        self.age = age

charlie = parrot("Charlie", 2)
honey = parrot("Honey", 2)

print(charlie.name, " is a ", charlie.species)
print(honey.name, "is also a ", honey.species)

print(charlie.name, "is {} years old".format(charlie.age))
print(honey.name, "is {} years old".format(honey.age))

