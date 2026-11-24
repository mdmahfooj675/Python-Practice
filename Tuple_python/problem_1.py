# problem 1: modify a tuple

# second method to solve the problem

print("question -> based on the modify of a tuple")

tup = (10 , 20 , 30 , 40)

tup = tup[ : 2] + (99 , ) + tup[3 : ]
print("updated tuple : " , tup)

print("code execution successfully....")

print("-------------------------------------------------") 

# first way to solve the problem using change the data tpye

# original tuple -> (10, 20, 30, 40)
# Result -> (10, 20, 99, 40) 

print("question -> based on the modify of a tuple")


tup = (10 , 20 , 30 ,40)
print("original tuple : " ,tup)

# step 1-> firslt we change the tuple to list 
# for changing immutalbe to mutable
num = list(tup)

# step 2-> change the value at the particular index
num[2] = 99

# step 3-> again. change to the tuple
tup = tuple(num)

print("updated tuple : " , num)

print("code ended....")