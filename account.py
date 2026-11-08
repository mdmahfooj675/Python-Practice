# question -> creat account class with 2 attrubutes balance and account no
# creat method for debit , credit and printing the balnce

class Account:
    def __init__(self , bal , acc):
        self.balance = bal
        self.account_no = acc

    # for debit
    def debit(self , ammount):
        if ammount > self.balance:
            print("Insufficient balance")
            return
        
        self.balance -= ammount
        print("₹ " ,ammount , "was debited from your account")
        print("reamining total balance : " , self.get_balance())

        # for credit
    def credit(self , ammount):
        if ammount > self.balance:
            print("Insufficient balance")
            return
        
        self.balance += ammount
        print("₹ " ,ammount , "was credited from your account")
        print("reamining total balance : " , self.get_balance())

    def get_balance(self):
        return self.balance

acc1 = Account(10000 , 1234567)
print("your account balance : " , acc1.balance)
print("your account number : " , acc1.account_no)

acc1.debit(100005)
acc1.credit(555)