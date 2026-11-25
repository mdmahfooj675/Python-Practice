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
