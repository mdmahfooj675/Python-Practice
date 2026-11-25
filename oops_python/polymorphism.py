# polymorphhim is object oriented 

# addition of two complex number without using dunder function
print("addition of two complex number without using dunder function...")

class Complex:
    def __init__(self , real , imag):
        self.real = real
        self.imag = imag

    def show_number(self):
        print(self.real , "i + " , self.imag , "j")

    def add(self , num2):
        new_real = self.real + num2.real
        new_imag = self.imag + num2.imag

        return Complex(new_real , new_imag)

num1 = Complex(2 ,3)
num1.show_number()

num2 = Complex(5 ,4)
num2.show_number()

num3 = num1.add(num2)
num3.show_number()

print("=============================================")

# using dunder function
print("using dunder function...")

class Complex:
    def __init__(self , real , imag):
        self.real = real
        self.imag = imag

    def show_number(self):
        print(self.real , "i + " , self.imag , "j")

    def __add__(self , num2):
        new_real = self.real + num2.real
        new_imag = self.imag + num2.imag

        return Complex(new_real , new_imag)

    
    def __sub__(self , num2):
        new_real = self.real - num2.real
        new_imag = self.imag - num2.imag

        return Complex(new_real , new_imag)

num1 = Complex(2 ,3)
num1.show_number()

num2 = Complex(5 ,4)
num2.show_number()

# for addition
num3 = num1 + num2
num3.show_number()

# for substraction
num3 = num1 - num2
num3.show_number()