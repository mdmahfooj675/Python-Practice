# question -> creat account class with 2 attrubutes balance and account no
# creat method for debit , credit and printing the balnce

class Account:
    def __init__(self , bal , acc):
        self.balance = bal
        self.account_no = acc

    # for debit
    def debit(self , ammount):
        if ammount > self.balance:
            print("Insufficient balance")
            return
        
        self.balance -= ammount
        print("₹ " ,ammount , "was debited from your account")
        print("reamining total balance : " , self.get_balance())

        # for credit
    def credit(self , ammount):
        if ammount > self.balance:
            print("Insufficient balance")
            return
        
        self.balance += ammount
        print("₹ " ,ammount , "was credited from your account")
        print("reamining total balance : " , self.get_balance())

    def get_balance(self):
        return self.balance

acc1 = Account(10000 , 1234567)
print("your account balance : " , acc1.balance)
print("your account number : " , acc1.account_no)

acc1.debit(100005)
acc1.credit(555)

# ---------------------------------------------------------------------------

# basic example of abstraction in object oriented

# it shows only necessary thing like car started 
# hide the unwanted like how clutch and acc are goes false to true

class car:
    def __init__(self):
        self.acc = False
        self.brk = False
        self.clutch = False

    def start(self):
        self.clutch = True
        self.acc = True
        print("car started successfully....")

car1 = car()
car1.start()


# ---------------------------------------------------------------------------

# creat student class that take name and marks of three subject as argument in the constructor
# then creat a method to print the average marks

class Student:
    def __init__(self , name , marks):
        self.name = name
        self.marks = marks

    def get_average(self):
        sum = 0
        for val in self.marks:
            sum += val
        print("hi " , self.name , "your average marks is : " , sum/3)

s1 = Student("thor" , [98 , 96 , 97])
s1.get_average()

# ---------------------------------------------------------------------------

class Mac:
    college_name = "apna college"

    def __init__(self , name , marks):
        self.name = name
        self.marks = marks

    def welcome(self):
        print("welcome student : ", self.name , " on apna college ")

    def get_marks(self):
        return self.marks
    
s1 = Mac("mohan" , 89)
s1.welcome()
print(s1.get_marks())

# ---------------------------------------------------------------------------

class student:
    # this is called the default constructor ( python creat automatically)
    def __init__(self):
        pass # alse here we can print some info or data
        
    # this is called the parametrized constructor
    # in parametrized constructor we passes some parameters
    def __init__(self , name , marks):
        self.name = name
        self.marks = marks
        print("add new student in the database")

s1 = student("karan" , 88)
s2 = student("mahfooj" , 98)
s3 = student("IES", 44)
print(s1.name , s1.marks)
print(s2.name , s2.marks)
print(s3.name , s3.marks)


# s1 = student("karan")
# print(s1.name)

# s2 = student("mahfooj" )
# print(s2.name)

# s3 = student("IES")
# print(s3.name)

# ---------------------------------------------------------------------------

# creating an class
class student:
    name = "mahfooj"

# creating object 
s1 = student()
print(s1.name)

# ---------------------------------------------------------------------------