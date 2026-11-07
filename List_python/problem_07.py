# find the sum of the elements present in the list using for loop in different ways

print("question -> find the sum of the elements present in the list ")

# first method of solving
print("first method of solveing...")

num = [60 , 70 , 80 , 90 , 100]
total = 0

index = 0
for i in range(len(num)):
    num[index]

    total = total + (num[index])
    index+=1

print("total sum of the elements : " , total)

print("code executed succesfully.....")


# second method of solvig
print("second method of solving...") 

numbers = [100 , 200 , 300 , 400 , 500 , 600 , 700 , 800 , 900 , 1000]
total_sum = 0

for i in range(len(numbers)):
    total_sum = total_sum + numbers[i]

print("total sum of the elements : " , total_sum)

print("code ended....")


# third method of solveing 
print("third method of solving....")

Num = [43 , 55 , 89 , 90 , 65 , 78 , 98]

total_suum = 0
for value in Num:
    total_suum = total_suum + value

print("total sum of the elements present in the list : " , total_suum)

print("code ended successfully.....")


# fourth method of solving
print("fourth method of solving..")

element = [555 , 546 , 890 , 876 , 980 , 434]

print("total sum of the elements : " , sum(element))

print("code ended successfully....")