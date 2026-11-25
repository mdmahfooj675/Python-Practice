# class method in python
print("changing the class attribute without using class method")

class Persons:
    name = "anonymous"

    def change_name(self , name):
        Persons.name = name

P1 = Persons()

P1.change_name("rahul kumar")
print(P1.name)
print(Persons.name)

print("-------------------------")

# class method in python
print("class method in python....")

class Persons:
    name = "anonymous"

    def change_name(self , name):
        self.__class__.name = "Rahul"

Per1 = Persons()

Per1.change_name("rahul kumar")
print(P1.name)
print(Persons.name)

print("-------------------------")

class Persons:
    name = "anonymous"

    @classmethod
    def change_name(cls , name):
        cls.name = name

Per1 = Persons()

Per1.change_name("rahul kumar")
print(P1.name)
print(Persons.name)