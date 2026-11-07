# take a character as input form user and print the wheater it's vowels or consonent

print("question -> take a character as input form user and print the wheater it's vowels or consonent")

char = input("Enter a character : ") 

if char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u' or char == 'A' or char == 'E' or char == 'I' or char == 'O' or char == 'U':
    print("entered character is vowels : " , char)
else:
    print("entered character is consonent : " , char)

print("code ended.....")