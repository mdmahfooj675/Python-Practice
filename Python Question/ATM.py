# here is the basic python code that tells how an ATM works on the background

account_balance = 5000
secret_pin = 1234  # it is the atm pin to access the atm

entered_pin = int(input("Enter your valid atm pin : "))
if entered_pin != secret_pin:
    print("you entered the wrong ATM pin")
    exit()

withdraw_ammount = float(input("Enter the withdraw ammount : "))

if withdraw_ammount <= 0:
    print("your account can't be negative")
    print("Invalid Ammount")

elif withdraw_ammount > account_balance:
    print("Insufficient Account Balance")
    print("you don't have money in your account")

elif  withdraw_ammount < account_balance:
    new_balance = account_balance - withdraw_ammount
    print("withdraw sucessfully ! ")
    print("you have left money in your account : " , new_balance)

print("Thank you for using the ATM ")
print("code ended.....")