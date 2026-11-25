# question number 1:-
# define a circle class to create a circle with radius r using the constructor
# define the area() method of the class which calculate the area of the circle
# defien the perimeter() method of the class which calculate the perimeter of the circle

class Circle:
    def __init__(self , radius):
        self.radius = radius

    def show(self):
        print("area of the circle : " , self.area())
        print("perimeter of the circle : " , self.perimeter())

    def area(self):
        return 3.14 * self.radius * self.radius

    def perimeter(self):
        return 2 * 3.14 * self.radius

c1 = Circle(21)
c1.show()
# print(c1.area())
# print(c1.perimeter())

print("=============================================")

# question number 2:-
# define a employee class with attributes role , department , salary
# this class also has a showDetails method
# create en engineer class that inherit property from employee

class Employee:
    def __init__(self , role , department , salary):
        self.role = role
        self.department = department
        self.salary = salary

    def show_details(self):
        print("role of the employee : " , self.role)
        print("department  of the employee : " , self.department)
        print("salary of the employee : " , self.salary)

        print("name  of the employee : " , self.name)
        print("age of the employee : " , self.age)

class Engineer(Employee):
    def __init__(self , name , age):
        super().__init__("Accountant" , "Finance" , "60,000")
        self.name = name
        self.age = age


eng1 = Engineer("mohan" , 19)
eng1.show_details()

print("=============================================")

# question number 3:-
# create a class called order which stores item and it's price
# use dunder function __gt__() to convay that:
# order1 > order2 if price of order1 > price of order2

class Order:
    def __init__(self , item , price):
        self.item = item
        self.price = price

    def __gt__(self , odr2):
        return self.price > odr2.price

odr1 = Order("chips" , 20)
odr2 = Order("frooti" , 10)

print(odr1 > odr2)


print("=============================================")