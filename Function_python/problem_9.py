# creat a function that check wheather a number is even or odd

print("question -> creat a function that check given number is even or odd")

def check_num(x):
    if x % 2 == 0:
        print("even number : " , x)
    else:
        print("odd number : " , x)

Num = int(input("Enter a number : "))
check_num(Num)

print("code execution successfully....")