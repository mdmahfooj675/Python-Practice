# creat a function that find the factorial of n (n as a parameters)

print("question -> creat a function that find the factorial of n (n as a parameters)")

def calc_factorial(n):
    fact = 1
    for i in range(1 , n+1):
        fact *= i
    print("factorial of the number " , n , ": " ,  fact)

calc_factorial(5)

print("problem executed successfully.....")