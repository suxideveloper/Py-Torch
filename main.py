
class Person:
    def __init__(self, name, age):
        self.ism = name
        self.yosh = age

    def greet(self):
        return f"Assalomu alaykum {self.ism}"

odam = Person("Sox", 25)
x, y = odam.ism, odam.yosh

salom = odam.greet()


print(x, y)
print(salom)

