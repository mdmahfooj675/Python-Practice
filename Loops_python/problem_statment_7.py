# take a number input from user 
# calculate and print the factorial of the number using loops

print("question -> print the factorial of a given number using loops")
n = int(input("Enter a number : "))

fact = 1

for i in range(1 , n ):

    if n <= 0:
        print("factorial is one")

    else:
        fact *= n
        
print(fact)
