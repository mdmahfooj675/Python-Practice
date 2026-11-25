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