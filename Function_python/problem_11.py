# creat a function that return the maximum numbers among two numbers
# take number as input foem user

print("question -> creat a function that return the mazimum number among two numbers ")

def max_two(a , b):
    if a > b:
        print("a is the maximum number : " , a)
        return a
    else:
        print("b is the maximum number : " , b)
    return b

x = float(input("Enter a number : "))
y = float(input("Enter a number : "))

max_two(x , y)

print("code execution successfully.....")