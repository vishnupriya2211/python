class Bank:

    account_number=int
    account_type=str
    customer_name:str
    balance:int

    def __init__(self,account_number,account_type,customer_name,balance):
        self.account_number=account_number
        self.account_type=account_type
        self.customer_name=customer_name
        self.balance=balance

    def deposite(self,amount):
        self.balance+=amount
        print(f"your account{self.account_number}has been credited with amount{amount} avl bal{self.balance}")

    def withdraw(self,amount):
        if self.balance<amount:
            self.balance-=amount
            print(f"your account{self.account_number}has been debited with amount{amount} avl bal{self.balance}")
        else:

            print("insufficient balance")
    def get_balance(self):
        print("yoour aval bal",self.balance)

customer_instance=Bank(100023,2500,"saving","aseed")

customer_instance.withdraw(5000)