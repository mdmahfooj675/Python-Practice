# single inheritance in python
print("sigle inheritance in python..")

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
