# ---------------------------------------------------------------------------

# Instructions
# Inside the editor, complete the following steps:
# Create a class called Rectangle
# Add an __init__ method with width and height, and store them as properties
# Add a method called area that returns the width multiplied by the height
# Create an object r1 with width 5 and height 3
# Print the area of r1

class Rectangle:
    def __init__(self , width , height):
        self.width = width
        self.height = height

    def area(self):
       return self.width * self.height

r1 = Rectangle(5 , 3)

print(r1.area())


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

# Create a class called Car.

# It should have three attributes:
# - brand
# - color
# - model
# Create two objects with different values and print their information.

class Car:
    brand = "BMW"
    colour = "blue"
    model = "M4"


car1 = Car()
car2 = Car()

print(f"car brand is : {car2.brand} car colour is :  {car2.colour} car model is :  {car2.model}")

car2.brand = "mercedes"
car2.colour = "white"
car2.model = "z class"

print(f"car brand is : {car1.brand} car colour is :  {car1.colour} car model is :  {car1.model}")
print(f"car brand is : {car2.brand} car colour is :  {car2.colour} car model is :  {car2.model}")

# ---------------------------------------------------------------------------

# how to use del keyword in object oriented
class Student:
    def __init__(self , name):
        self.name = name 

s1 = Student("Md Mahfooj Alam")
print("student name is : " , s1.name)

#del s1.name
print(s1.name)

print("code ended....")
