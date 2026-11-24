# problem statment based on the employee managment

# Employee Management
# Create a class Employee with these attributes:
# - name
# - salary
# - department
# Create three employee objects:
# Object	Name	Salary	Department
# emp1	Rahul	25000	IT
# emp2	Aman	30000	HR
# emp3	Priya	35000	AI

# Requirements:
# 1. Create a constructor.
# 2. Create a method display_info() to display employee details.
# 3. Create a method annual_salary() that returns the annual salary.
# Formula:
# \[
# \text{Annual Salary} = \text{Monthly Salary} \times 12
# \]

class Employee:
    def __init__(self , name , salary , department):
        self.name = name
        self.salary = salary
        self.department = department

    def display_info(self):
        return (
            f"name of the employee : {self.name}\n"
            f"salary of the employee : {self.salary}\n"
            f"department of the employee : {self.department}"
        )

    def annual_salary(self ):
        return self.salary*12

emp1 = Employee("Rahul" , 25000 , "IT")
emp2 = Employee("Aman" , 30000 , "HR")
emp3 = Employee("Priya" , 35000 , "AI")

Employees = [emp1 , emp2 , emp3]

for employee in Employees:
    print("employee details...")
    print(employee.display_info())
    print(employee.annual_salary())
    print("-------------")

print("code execution successfully....")