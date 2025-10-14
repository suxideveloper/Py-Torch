
class Person:
    def __init__(self, name, age):
        self.ism = name
        self.yosh = age

    def greet(self):
        return f"Assalomu alaykum {self.ism}"

odam = Person("Sox", 25)
x, y = odam.ism, odam.yosh

salom = odam.greet()


# print(x, y)
# print(salom)

class Dog:
    species = "Canine"  # Class attribute shared by all instances of the class.
    def __init__(self, name, age): # __init__ method: Initializes the name and age attributes when a new object is created
        self.nomi = name  # Instance attribute
        self.yoshi = age  # Instance attribute

it = Dog("Apch", "wcbe")
print(it.nomi)
print(Dog.species)

class Car:
    def __init__(self, model, price):
        self.rusum = model
        self.narxi = price


Audi = Car(123,234) 

modeli = Audi.rusum
narxi = Audi.narxi



# print(modeli, narxi)