# find the largest number among four numbers
a = int(input("Enter a first number : "))
b = int(input("Enter a second number : "))
c = int(input("Enter a third number : "))
d = int(input("Enter a fourth number : "))

if a > b and a > c and a > d:
    print("a is larger the  number : " , a)

elif b > c and b > d:
    print("b is the larger : " , b)

elif c > d:
    print("c is the larger number : " , c)

else:
    print("d is the larger number : " , d)

print("code ended.....")


# find the smaller number among three numbers
a = int(input("Enter a first number : "))
b = int(input("Enter a second number : "))
c = int(input("Enter a third number : "))

if a < b and a < c:
    print("a is smaller number : " , a)
elif b < c:
    print("b is smaller : " , b)
else:
    print("c is smaller : " , c)


# find the largest number using python
a = int(input("Enter a first number : "))
b = int(input("Enter a second number : "))
c = int(input("Enter a third number : "))

if a > b and a > c:
    print("a is larger number : " , a)
elif b > c:
    print("b is larger : " , b)
else:
    print("c is larger : " , c)

print("code ended.....")