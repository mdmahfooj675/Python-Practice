# List sum: list lo aur uske saare elements ka sum return karo (bina sum() use kiye).

print("question -> creat a function that return the sum of all the elements")

num = [10 , 20 , 30 , 40 , 50]
value = [54 , 67 , 78 , 90 , 76 , 54]

sum = 0

def list_sum(numbers):
    total = 0 

    for item in numbers:
       total += item

    return total
 
result = list_sum(num)
print("addition of the elements in the list : " , result)

add = list_sum(value)
print("sum of tht elements present in the list : " , add)  

print("code execution successfully....")