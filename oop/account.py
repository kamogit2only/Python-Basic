import time


class Account():
    
    count = 0 
    
    def __init__(self, balance, name) -> None:
        self.balance = balance
        self.name = name
        self.account_number = Account.count
        self.transaction_history = []
        Account.count += 1
    
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance = self.balance - amount   
            self.show_balance()     
            self.add_transaction(-amount)
        else:
            print(f"残高({self.balance}円)が足りません")
        
    def deposit(self, amount):
        self.balance += amount
        self.show_balance()
        self.add_transaction(amount)
        
    def show_balance(self):
        print("{0.name}{0.account_number}の残高は{0.balance}円です".format(self))
        
    def add_transaction(self, amount):
        transaction = {
            'withidraw/deposit': amount,
            'new balance': self.balance,
            'time': Account.get_time_str()
        }
        self.transaction_history.append(transaction)
        
    @staticmethod
    def get_time_str():
        current_time = time.localtime()
        return "{0.tm_year}年{0.tm_mon}月{0.tm_mday}日{0.tm_hour}時{0.tm_min}分".format(current_time)
    
    def show_transaction_history(self):
        for transaction in self.transaction_history:
            transaction_str_list = []
            for k, v in transaction.items():
                transaction_str_list.append(f"{k}: {v}, ")
            print(", ".join(transaction_str_list))
    
myaccount = Account(balance=1000, name="my account")
print(myaccount.name)
print(myaccount.balance)
myaccount.withdraw(300)
myaccount.deposit(500)
myaccount.withdraw(2000)
print(myaccount.transaction_history)
print(Account.get_time_str)
myaccount.show_transaction_history()