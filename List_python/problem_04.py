# print some question based on the list slicing

print("question -> use some list slicing method and print them")

num =  [4, 8, 15, 16, 23, 42]

print(type(num))

# print the first three element present in the list using slicing concept
print("first three number using slicing : " , (num[0:3]))
#print(num)

# print the last three element present in the list using slicing concept
print("last three number using slicing : " ,(num[-4 : -1]))

# print the list and skip the second element(print in odd format)
print("skip of two : " , (num[0 : : 2]))


# print the list in reverse format
num.reverse()
print("print the list in the reverse format : " , num)

print("code ended...")