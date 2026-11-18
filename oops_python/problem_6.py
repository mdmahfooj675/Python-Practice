# Bank Account Management
# Now let's introduce a slightly more realistic problem.

# Create a class BankAccount with:
# - account_holder
# - balance

# Requirements:
# 1. Create a constructor.
# 2. Create a method deposit(amount) that adds money to the balance.
# 3. Create a method withdraw(amount) that subtracts money from the balance.
# 4. Create a method display_balance() that returns the current balance.

class Bank_Account:
    def __init__(self ,account_holder , balance):
        self.account_holder = account_holder
        self.balance = balance

    def display(self):
        return (
            f"account holder name: {self.account_holder}\n"
            f"current balance : ₹{self.balance}\n"
        )

    def deposit_moeny(self , ammount):
        # self.ammount = ammount

        if (self.balance > 0):
            self.balance += ammount
            print(f"₹{ammount} deposited successfully....")
   
     
    def withdraw_money(self, amount):
        if amount <= 0:
            print("Invalid withdrawal amount!")
        elif self.balance >= amount:
            self.balance -= amount
            print(f"₹{amount} withdrawn successfully!")
        else:
            print("Insufficient balance!")
     
# creating objects
acc1 = Bank_Account("Rahul" , 10000)
acc2 = Bank_Account("Aman" , 20000)

print("-------- Rahul --------")
print(acc1.display())

# rahul transation
acc1.deposit_moeny(5000)
acc1.withdraw_money(2000)

print("\n after transation")
print(acc1.display())


print("------ Aman --------")
print(acc2.display())

# aman transation
acc2.deposit_moeny(3000)
acc2.withdraw_money(1000)

print("\n after transation")
print(acc2.display())