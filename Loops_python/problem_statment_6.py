# take a string as input from user and print the total vowels present in the given string

print("count the vowels present in the string using for loop")
Word = input("enter a string : ")
vowelss = 0

for ch in Word:
    if ch in "aeiouAEIOU":
        vowelss += 1

print("total vowels : " , vowelss)


print("Count the total vowels in a string using a while loop")
print("code execution successfully .....")

woord = input("Enter a word or string: ")
vowl = 0
i = 0

while i < len(woord):
    ch = woord[i]

    if ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u' or ch == 'A' or ch == 'E' or ch == 'I' or ch == 'O' or ch == 'U':
        vowl += 1

    i += 1

print("Total vowels:", vowl)
print("code execution successfully .....")


print("Question -> take a string as input and print the total vowels present in the string using for loop")

word = input("Enter any string : ")
vowel = 0

for ch in word:
   if  ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u' or ch == 'A' or ch == 'E' or ch == 'I' or ch == 'O' or ch == 'U':
      vowel += 1 

print("total vowels in string : " , vowel)


print("code ended....")