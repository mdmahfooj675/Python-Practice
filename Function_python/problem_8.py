#creat a function that find the factorial of n (n as a parameters)

print("question -> creat a function that find the factorial of n (n as a parameters) , take n as input foem the user")

def calc_factorial(n):
    fact = 1
    for i in range(1 , n+1):
        fact *= i
    print("factorial of the number " , n , ": " ,  fact)

num = int(input("enter a number : "))
calc_factorial(num)

print("problem executed successfully.....")