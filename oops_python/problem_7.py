# Constructor Practice

# Create a class Laptop.

# Requirements:
# - Attributes: brand, model, price.
# - Initialize attributes using __init__().
# - Create a method display_info().
# - Create at least 3 objects.

class Laptop:
    def __init__(self , brand , model , price):
        self.brand = brand
        self.model = model
        self.price = price

    def display(self):
        return (
            f"brand of the laptop : {self.brand}\n"
            f"model of the laptop : {self.model}\n"
            f"price of the laptop : {self.price}"
        )

L1 = Laptop("macbook" , "m5" , 149900)
L2 = Laptop("Lenovo" , "LOQ" , 93000)
L3 = Laptop("Lenovo" , "think pad" , 31000)

Laptops = [L1, L2 , L3]

for Laptop in Laptops:
    print("Laptop information.....")
    print(Laptop.display())
    print("----------------------")

print("code execution successfully.....")