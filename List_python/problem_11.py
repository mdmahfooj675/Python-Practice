# problem statment :-

# you have the list nums = [12, 7, 19, 24, 5, 30, 8, 15]
# write a python function Python function process_numbers(nums) that perform:
# only the even numbers also larger then the 10.
# return the square of  the filtered numbers and append in the new list.
# Expected Output for above list:[144, 576, 900]


print("question -> retrun the square of the elements whose element are even and larger than 10")

print("-----------------------------------------------------")
print("first way to solve the problem")

def process_numbers(nums):
    return [item ** 2 for item in nums if item % 2 == 0 and item > 10]

nums = [12, 7, 19, 24, 5, 30, 8, 15]
print(process_numbers(nums))

print("-----------------------------------------------------")

print("second way to sovle the problem...")

num = [12 , 7 , 19 , 24 , 5 , 30 , 8 , 15]
new_num = []

for item in num:
    if item % 2 == 0:
        if item > 10:
            print("even no & larger then 10 no are : " , item)
            new_num.append(item)

print("list of even and larger then 10 : " , new_num)

new_num2 = []

for item in new_num:
    square = item * item
    print("square of the even no : " , square)
    new_num2.append(square)

print("final list : " , new_num2)