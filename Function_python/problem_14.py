# Keyword arguments: student_info(name, age, city) banao.
#  Isko alag-alag order me keyword arguments ke saath call karo, jaise student_info(city="Bhopal", name="Md", age=18).

print("question -> solve the problem based on the keyword arguments")

def student_info(name , age , city):
    print("name : " , name)
    print("age : " , age)
    print("city : " , city)

student_info(name = "mahfooj" , age = 18 , city = "bhopal")
student_info(name = "mohan" , age = 55 , city = "pune")

print(student_info)
