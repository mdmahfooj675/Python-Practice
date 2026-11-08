# take a number as input and print the factorial of that number

print("print the factorial of a given number using for loop")

m = int(input("Enter a number : "))
factorial = 1

for i in range(m , 1 , -1):
    factorial *= i
    #i+=1

print(factorial)


print("question -> take a number as input and print the factorial of that number using while loop")

n = int(input("Enter a number : "))

i = 1
fact = 1

while i <= n:
    fact = fact*i

    i+=1

print(fact)
      

print("code ended....")