print("question 1-> debug the code based on the variable and average")
# DEBUG PRACTICE - Individual topics
# Rule: Har section ke andar bugs hain. Expected output comment mein diya hai.
# Tip: VS Code mein "# %%" cells ko alag-alag run kar sakte ho,
# ya ek section fix karke aage badho.


# %% 1. VARIABLES (3 bugs)
# Expected output:
# Name: Md Age: 19
# Next year age: 20
# Total marks: 255 Average: 85.0
name = "Md"
age = int("19")
print("Name:", name, "Age:", age)
next_year = age + 1
print("Next year age:", next_year)

maths = 80
physics = 90
chemistry = 85
total = maths + physics + chemistry
average = total / 3
print("Total marks:", total, "Average:", average)

print("code debugging sucessfully...")


print("question 2-> debug the code based on the conditional statments")
# %% 2. CONDITIONS (3 bugs)
# Expected output:
# Grade B
# Odd
# Eligible to vote
marks = 72
if marks >= 40 and marks <= 59:
    print("Grade C")
elif marks >= 60:
    print("Grade B")
elif marks >= 90:
    print("Grade A")
else:
    print("Fail")

num = 7
if num % 2 == 0:
    print("Even")
else:
    print("Odd")

age = 18
if age >= 18:
    print("Eligible to vote")
else:
    print("Not eligible to vote")

print("code debug successfully....")


print("question 3-> debug the code based on the list")
# %% 3. LIST (3 bugs)
# Expected output:
# [5, 12, 8, 21, 14, 30]
# Last element: 30
# Even numbers: [12, 8, 14, 30]

numbers = [5, 12, 8, 21, 14]
numbers.append(30)
print(numbers)

print("Last element:", numbers[-1])


evens = []
for el in numbers:
    if el % 2 == 0:
      evens.append(el)
      print("even numbers in the list : " , el)
      
print("final list of the Even numbers:", evens)

print("code debug done...")


print("question 4-> debug the code based on the tuple")
# %% 4. TUPLE (3 bugs)
# Expected output:
# red
# ('red', 'yellow', 'blue')
# <class 'tuple'>
# 1 2 3
colors = ("red", "green", "blue")
print(type(colors))
print(colors[0])
print("previous tuple : " , colors)

#colors[1] = "yellow".  tuple does not allow to replace any element in the exixting tuple

temp_list = list(colors) # step 1-> convert the tuple into temp_list
temp_list[1] = "yellow" #  step 2-> update the element in the first index in the temempory list
colors = tuple(temp_list) # step 3-> then convert the temp_list into the tuple

print("updated tem_list is : " , temp_list)
print("updated tuple : " , colors)

colors = colors[:1] + ("yellow",) + colors[2:] # another method to update the element in the exixting tuple
print("update tuple by using slicing : " , colors)


single = ("hello" ,)
print("type of the single : " , type(single))

a, b , c  = (1, 2, 3)
print(a, b , c)

print("code debugging successfully...")


print("question 5-> debug the code based on the dictionary")
# %% 5. DICTIONARY (3 bugs)
# Expected output:
# Md
# {'name': 'Md', 'course': 'B.Tech', 'year': 1, 'city': 'Bhopal'}
# name : Md
# course : B.Tech
# year : 1
# city : Bhopal
student = {"name": "Md", "course": "B.Tech", "year": 1}
print(student["name"])

student.update({"city": "Bhopal"})
print(student)

for key , value in student.items():
    print(key, ":", value)


print("code dubugging successfully...")


print("question 6-> debug the code based on the set")
# %% 6. SET (3 bugs)
# Expected output:
# {1, 2, 3, 4}
# {1, 2, 3, 4}
# {1}
nums = [1, 2, 2, 3, 3, 3, 4]
unique = set(nums)
print(unique)

s = {1, 2, 3}
s.add(4)
print(s)

empty = set()
empty.add(1)
print(empty)

print("code debugging successfully.....")