# print the sum of the numbers between 1 to 100

print("print the sum of the number form 1 to 100 usnig for loop")

sum = 0

for i in range(1 , 101 ):
    sum = sum + i
    i+=1
print("sum of the number between 1 to 100 : " , sum)


print("print the sum of the number form 1 to 100 using while loop")

n = 1 
sum = 0
while(n <= 100):
    #n += 1 

    sum = sum + n
    n+=1

print("sum of the number : " , sum)


print("code ended....")