class Pet(object):
    def __init__(self, name, age, animal, is_hungry, mood):
        self.name = name
        self.age = age
        self.animal = animal
        self.is_hungry = is_hungry
        self.mood = mood
my_pet = Pet("Fido", 3, "Dog", False, "Happy")
print("My pet %s is %s years old" % (my_pet.name, my_pet.age))
pet_2 = Pet("Gary", 15, "Cat", True, "Sad")
pet_3 = Pet("Garfield", 3, "Cat", True, "Jubilant")
print("I also have two cats named %s and %s" % (pet_2.name, pet_3.name))
