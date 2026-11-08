# take a number input form user and print the table of the given number n

print("question -> take a number as input form user and print the tabel using the for loop")
n = int(input("Enter a number : "))

for i in range(1 , 11):
    print(n , "*" , i , "=" , n*i)


print("print the table of n using while loop")

m = int(input("Enter a number : "))
i = 1
while i <= 10:
    print(m , "*" , i , "=" , m*i)
    i+=1


print("code ended....")