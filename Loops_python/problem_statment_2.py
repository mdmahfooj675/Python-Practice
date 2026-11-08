# print the all even number form 1 to 20


print("print all even number between 1 to 20 using loop and conditionals")
for i in range(1 , 20):
    if i % 2 == 0:
        print("even : " , i)
   

print("print all the even number between 1 to 20 using while loop and conditionals")
i = 2
while(i <= 20):
    if i % 2 == 0:
        print("even : " , i)
    else:
        print("odd : " , i) 
    i+=2


print("question -> print the even numbers between 1 to 20")
print("using while loop")

i = 2
while(i <= 20):
    print("even number : " , i)
    i+=2


print("question -> print the even numbers between 1 to 20")
print("using for loop")

for i in range(2 , 20 , 2):
    print("even num : " , i)


print("code ended....")