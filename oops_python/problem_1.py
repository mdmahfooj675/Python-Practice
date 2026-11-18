# Q1. Student Information

# Create a class Student.
# - Create two objects: student1 and student2.
# - Assign each object a name, age, and branch.
# - Print the details of both students.

class student:
    def __init__(self , name , age , branch):
        self.name = name
        self.age = age
        self.branch = branch

    def display(self):
        return (
            f"name of the student : {self.name}\n"
            f"age of the student : {self.age}\n"
            f"branch of the student : {self.branch}"
        )
student1 = student("mohan" , 18 , "CSE")
student2 = student("sohan" , 19 , "machanical")

print("information of student1 ")
print(student1.display())

print("--------------------------------------")

print("information of student2 ")
print(student2.display())



# ---------------------------------------------------------------------------

class Student:
    def __init__(self , name , age , branch):
        self.name = name
        self.age = age
        self.branch = branch

Student1 = Student("mohan" , 18 , "AI & ML")
Student2 = Student("sohan" , 19 , "machanical")
   
print("information of student1 : ")
# Student1.display
print("name : " , Student1.name)
print("name : " , Student1.age)
print("name : " , Student1.branch)

print("information of student2 : " )
# Student2.display
print("name : " , Student2.name)
print("name : " , Student2.age)
print("name : " , Student2.branch)