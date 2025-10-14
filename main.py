
# class Person:
#     def __init__(self, name, age):
#         self.ism = name
#         self.yosh = age

#     def greet(self):
#         return f"Assalomu alaykum {self.ism}"

# odam = Person("Sox", 25)
# x, y = odam.ism, odam.yosh

# salom = odam.greet()

# # print(x, y)
# # print(salom)
# # <-------------------------------------------------->
# class Dog:
#     species = "Canine"  # Class attribute shared by all instances of the class.
#     def __init__(self, name, age): # __init__ method: Initializes the name and age attributes when a new object is created
#         self.nomi = name  # Instance attribute
#         self.yoshi = age  # Instance attribute

# it = Dog("Apch", "wcbe")
# print(it.nomi)
# print(Dog.species)

# Dog.species = "Updated"
# print(it.species)

# # <------------------------------------------------>
# class Car:
#     def __init__(self, model, price):
#         self.rusum = model
#         self.narxi = price

# Audi = Car(123,234) 

# modeli = Audi.rusum
# narxi = Audi.narxi
# # print(modeli, narxi)
# # -------------------------------------------------------
# class Mynumber:
#     def __init__(self, value):
#         self.qiymati = value 

#     def print_value(self):
#         print(self.qiymati)

# obj1 = Mynumber(12345455)
# obj1.print_value()

# # <-------------------------------------------------------------

# class Subjects:
#     def __init__(self, name, teacher):
#         self.nomi = name
#         self.ustoz = teacher
    

# obj = Subjects("History", "John")
# x, y = obj.nomi, obj.ustoz
# print(x, y)

# # <----------------------------------------------------------------------
# class Test:
#     def __init__(this, name, age):
#         this.name = name
#         this.yosh = age
#     def test1(this):
#         print(f"Ishladi {this.name}")
#         print(f"Ishladi {this.yosh}")

# x = Test('Suxrob', 23)
# x.test1()

# # -------------------------------------------------------
# class Test2:
#     static = "hello"
#     def __init__(this):
#         print(f"Adress{ id(this)}")
# obj = Test2()
# print(f"Adress{id(obj)}")


test_list  = [23, 34, 45, 32, 67, 78, 66, 21, 89]

d = len(test_list)




print(d)
