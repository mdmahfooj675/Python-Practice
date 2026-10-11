# basic calculate the online shopping using python language

product_type = str(input("Enter your product type (gold , silver , regular ) : "))
product = input("enter choice of product (1)(2)(3) : ")

         
product_price = int(input("Enter your product ammount : "))

if product_price >= 5000:
    total_price = (product_price * 100) / 5
    print("your final price is : " , total_price)


coupon = input("Enter your coupon code (yes / no ) : ")

