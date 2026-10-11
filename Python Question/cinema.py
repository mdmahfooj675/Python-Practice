# smart movie ticket calculator using python language

age = int(input("Enter your valid age : "))
is_student = input("are you a student (yes / no ) : ")

if age <= 0:
    print("Invalid Age ")
    exit()

elif age < 12:
    ticket_price = 100
    print("your ticket price is : " , ticket_price)

elif age >= 60:
    ticket_price = 130
    print("your ticket price is : " , ticket_price)

elif age > 12 and age < 59:
    base_price = 200
    print("your ticet price is : " , base_price)

if is_student == "yes":
    new_price = base_price - 30
    print("your final ticket price is : " , new_price)

print("code ended.....")