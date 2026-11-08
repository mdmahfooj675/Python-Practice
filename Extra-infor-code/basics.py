# 7-> 

# 6-> some string method
hi = "hello mahfooj coder"

print("in lower case : " , hi.lower()) # it convert the string into the lower case
print("in upper case : " , hi.upper()) # it convert the string into the upper case

ho = "     mahfooj.      "
msg = "@@@@@@coding@@@@@@"
print("using strip method : " , ho.strip())
print("using strip method : " , ho.strip("@"))

# 5-> put some condition and check weather a word is not present in the given string
txt = "i am the student of computer science and engineering at IES College"
if "hi" not in txt:
    print("not present in the string -> false")
else:
    print("present in the string -> true")


# 5-> check weather a word is not present in the given string
txt = "i am the student of computer science and engineering at IES College"
print("hi" not in txt)


# 4 -> some conditional to cheack given word is present in the string or not
text = "I am an engineering student at IES College"

if "an" in text:
    print("it's present in the string")
else:
    print("it's not present in the string")

print("code ended....")

# 3 -> check weather a word or character present in the given string
message = "hello my name is md mahfooj alam"
print("alam" in message) # it check a word if present in the string if yes-> true other wise -> false

print("code ended....")


# 2 -> basic code based on the string 
for x in "md mahfooj alam":
    print("character are : " , x)

print("code ended.....")


# 1 -> basic code based on the type casting
x = 1
a = float(x) # it convert the int value into the float
b = str(x) # it convert thr int value into the string

print("type of a variable : " , type(a))
print("type of b variable : " , type(b))

print("value of a : " , a)
print("value of b : " , b)

print("code execution successfully....")
