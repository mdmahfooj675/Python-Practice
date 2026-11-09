# ---------------------------------------------------------------------------

# multiple methods on a class

class Playlist:
  def __init__(self, name):
    self.name = name
    self.songs = []

  def add_song(self, song):
    self.songs.append(song)
    print(f"Added: {song}")

  def remove_song(self, song):
    if song in self.songs:
      self.songs.remove(song)
      print(f"Removed: {song}")

  def show_songs(self):
    print(f"Playlist '{self.name}':")
    for song in self.songs:
      print(f"- {song}")

my_playlist = Playlist("Favorites")
my_playlist.add_song("Bohemian Rhapsody")
my_playlist.add_song("Stairway to Heaven")
my_playlist.show_songs()


# ---------------------------------------------------------------------------
 
class Person:
    def __init__(self , name , age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old"

p1 = Person("Tobies" , 36)
p2 = Person("Mahfooj" , 19)
print(p1)
print(p2)

# ---------------------------------------------------------------------------

# Inside the editor, complete the following steps:
# Create a class Student with an __init__ that takes name and grade, and stores them as properties
# Create an object s1 with name "Anna" and grade "A"
# Print the grade of s1
# Change the grade of s1 to "B"
# Print the updated grade

class Student:
    def __init__(self , name , grade):
        self.name = name
        self.grade = grade

s1= Student("Anna" , "A")
print(s1.grade)

s1.grade = "B"
print(s1.grade)

# ---------------------------------------------------------------------------

# Inside the editor, complete the following steps:
# Create a class called Dog
# Add an __init__ method with parameters name and age, and store them as properties using self
# Add a method called bark that prints the dog's name followed by " says Woof!"
# Create an object d1 of the Dog class with name "Buddy" and age 3
# Call the bark method on d1

class Dog:
    def __init__(self , name , age):
        self.name = name
        self.age = age

    def bark(self):
        print(self.name , "says woof!")
        print("the age of the dog : " , self.age)

    def birthday(self):
        self.age +=1
        print("updated age : " , self.age )

d1 = Dog("Buddy" , 3)
d1.bark()
d1.birthday()

print("code ended....")

# ---------------------------------------------------------------------------

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