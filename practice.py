# solving python problem 

# create a class student that take name and marks of three subject as argument in constructor
# print the average of the marks

class Student:
    
    def __init__(self , name , mark1 , mark2 , mark3):
        self.name = name
        self.mark1 = mark1
        self.mark2 = mark2
        self.mark3 = mark3

    def display(self):
        print("student details are ....")
        print("name of the student : " , self.name)
        print("marks of the first of the student : " , self.mark1)
        print("marks of the second of the student : " , self.mark2)
        print("marks of the third of the student : " , self.mark3)

        print("average marks : " , (self.mark1 + self.mark2 + self.mark3) / 3)

    

s1 = Student("mohan" , 87 , 89 , 90)
s1.display()

print("--------------------------------------")

s2 = Student("mohan" , 78 , 95 , 88)
s2.display()

print("==================================================")

# solve the same question in another way

class Students:
    def __init__(self , name , marks):
        self.name = name
        self.marks = marks

    def get_avg(self):
        sum = 0

        for val in self.marks:
            sum += val

        print("hi" , self.name , "your average score : " , sum / 3)

S1 = Students("mahfooj" , [92 , 97 , 95])
S1.get_avg()

print("==================================================")

# New requirement:

# Create a Student class that accepts a student's name and a list of marks.

# Add two methods:
# - get_avg() — calculates the average.
# - check_result() — checks whether the average is at least 40 and prints "Pass" or "Fail".
# Important hint: Your check_result() method should use the result calculated by get_avg().

class Students:
    def __init__(self , name , marks):
        self.name = name
        self.marks = marks

    @staticmethod
    def greet():
        print("it's result time")

    def get_avg(self):
        marks = 0

        for val in self.marks:
            marks += val

        self.average = marks / len(self.marks)
        print("hi" , self.name , "your average score : " , self.average)
        return self.average

    def get_result(self):

        if self.average >= 40:
            print("your result : Pass")
        else:
            print("your result : fail")

S1 = Students("Tony Star" , [86 , 93 , 85])
S1.greet()
S1.get_avg()
S1.get_result()

print("--------------------------------------")

S2 = Students("iron man" , [85 , 90 , 95])
S2.greet()
S2.get_avg()
S2.get_result()

print("--------------------------------------")

S3 = Students("halk" , [28 , 25 , 22])
S2.greet()
S3.get_avg()
S3.get_result()

print("==================================================")