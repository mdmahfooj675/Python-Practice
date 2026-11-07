#  creat a list and print the sum of the elements

print("question -> creat a list and print the sum of the elements")

# solve this question using the for loop
x = [12 , 44 , 56 , 78 , 90]

idx , add = 0 , 0

for idx in range(len(x)):
    print("elements are : " , x[idx])
    add = add + x[idx]

print("sum of the elements : " , add)

print("code execution successfully...")



# solve this question using the while loop
n = [10 , 20 , 40 , 60 , 80 , 90]

i , sum = 0 , 0

while i <= len(n)-1:
    print("elemets are : " , n[i])
    sum+=n[i]
    i+=1

print("sum of all the elements present in the list : " , sum)

print("code ended....")