# question number 1. -> take input string from the user and count the vowels

print("question -> count the vowels present in the sentence ")

moto = input("Enter a word or sentence : ")
count = 0

for character in moto:
    if character in "aeiouAEIOU":
        count +=1

print("total vowels are : "  , count)

print("code ended....")