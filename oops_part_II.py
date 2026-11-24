class Account:
    def __init__(self , acc_no , acc_pass):
        self.acc_no = acc_no
        self.__acc_pass = acc_pass # acc_pass is private 

    def reset_pass(self):
        print(self.__acc_pass)

acc1 = Account("123456789" , "Mac@123")
print("your account number : " , acc1.acc_no)
acc1.reset_pass()
#print("your account password : " , acc1.reset_pass())

print("=============================================")

class Person:
    __name = "karan"

    def __hello(self):
        print("hello person!")

    def welcome(self):
        self.__hello()

p1 = Person()

p1.welcome()
print(p1.welcome())
# print(p1.__name)
# print(p1.hello())

print("=============================================")

# inheritance in oops in python

# simgle inheritance in python
class Car:
    @staticmethod
    def start():
        print("car is starting.....")

    @staticmethod
    def stop():
        print("car stopped.....")

class Toyota_car(Car):
    def __init__(self , name):
        self.name = name 

car1 = Toyota_car("Fortnuer")
car2 = Toyota_car("prius")

car1.start()
print(car1.name)
car1.stop()

print("-------------------------")

car2.start()
print(car2.name)
car2.stop()

print("=============================================")

# multi level inheritance in python
print("multi level inheritance in python..")

class Car:
    @staticmethod
    def start():
        print("car is starting.....")

    @staticmethod
    def stop():
        print("car stopped.....")

class Toyota_car(Car):
    def __init__(self , brand):
        self.brand = brand

class Fortnure(Toyota_car):
    def __init__(self , type):
        self.type = type

Car1 = Fortnure("diesel")
Car2 = Fortnure("electric")

Car1.start()
print(Car1.type)
Car1.stop()

print("-------------------------")

Car1.start()
print(Car1.type)
Car1.stop()


print("=============================================")

# multiple inheritance in python
print("multiple inheritance in python..")

class A:
    varA = "welcome to class A"

class B:
    varB = "welcome to class B"

class C(A,B):
    varC = "welcome to class C"

c1 = C()

print(c1.varC)
print(c1.varB)
print(c1.varA)

print("=============================================")

# super method in python
print("super method in python..")

class Cars:
    def __init__(self , type):
        self.type = type

    @staticmethod
    def start():
        print("car is starting.....")

    @staticmethod
    def stop():
        print("car stopped.....")

class Toyota_car(Cars):
    def __init__(self , name , type):
        super().__init__(type)
        self.name = name 
        super().start()
        super().stop()

cars1 = Toyota_car("prius" , "electric")
print(cars1.type)

print("=============================================")

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