# smart movie ticket calculator using python language

age = int(input("Enter your age : "))
is_student = input("are you a student (yes / no ) : ")

if age <= 0:
    print("Invalid Age ")
    exit()

elif age < 12:
    base_price = 100
    print("Base price is Rs 100")

elif age >= 59:
    base_price = 300
    print("Base price is Rs 300")

if is_student == "yes":
    final_price = base_price - 30 # you have instant discount rs 30 as a student
    print("your final price is : " , final_price)

print("code ended.....")