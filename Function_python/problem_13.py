#  Reverse string: string lo aur use ulta karke return karo


print("Question: Reverse a string")

def reverse_str(values):
    return values[::-1]

Str = input("Enter a string: ")

result = reverse_str(Str)

print("Reverse of the string:", result)

print("code execution successfully.....")

#----------------------------------------------------------------------------------

print("question -> take string as input form user and print the reverse of the string")

def reverse_str(values):
    print("reverse of the string : " , values[ : : -1])
    return values

Str = input("enter a string : ")
reverse_str(Str)

print("code execution successfully.....")