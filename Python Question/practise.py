# practise question based on the conditioal statments python language

units = int(input("Enter your electricity units :  "))

if units < 0 and units >= 100:
    units_price = 5
    total_bill = units_price * units
    print("Your electricity units bill : " , total_bill)

elif units < 101 and units >= 200:
    units_price = 7
    total_bill = units_price * units
    print("your electricity units bill : " , total_bill)

elif units < 200:
    units_price = 10
    total_bill = units_price * units
    print("your electricity bill units : " , total_bill)

    if total_bill < 1000:
        final_bill = (total_bill * 10) / 100

        print("your final bill : " , final_bill)

print("code ended....")