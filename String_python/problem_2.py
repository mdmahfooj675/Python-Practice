# question number 2. -> take a word input form user and print weather it's palindrome or not

print("question -> check the given word is palindrome or not")

word = input("Enter a word : ")

word2 = word[ : : -1]
if word == word2:
    print("palindrome")
else:
    print("not palindrome")

print("code ended.....")