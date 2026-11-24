# Create a class Car.

# Create two objects and assign these attributes:
# - Car 1: Brand = Toyota, Model = Fortuner, Year = 2024
# - Car 2: Brand = BMW, Model = X5, Year = 2025
# Print the details of both cars.

class Car:
    def __init__(self , brand , model , year):
        self.brand = brand
        self.model = model
        self.year = year

    def display(self):
        return (
            f"brand of the car : {self.brand}\n"
            f"model of the car : {self.model}\n"
            f"year of the car : {self.year}\n"
        )

car1 = Car("Toyota" , "fortunre" , 2024)
car2 = Car("BMW" , "X5" , 2025)

print("details of car1")
print(car1.display())

print("--------------------------------------")

print("details of car2")
print(car2.display())