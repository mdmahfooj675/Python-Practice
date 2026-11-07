# question number 5. -> take input a word form user and print the length , first and last character and reverse slicing

print("question -> take a word input & print the length , first & last character and reverse slicing")

word = input("Enter a word : ")

print("length of the word is : " , len(word))
print("first character of the word is : " , word[0])
print("last character of the word is : " , word[-1])
print("reverse of the word is : " , word[ : : -1])

print("code execution sucessfully ...")