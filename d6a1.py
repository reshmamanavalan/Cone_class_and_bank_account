class Account():
    def __init__(self,ownername,balance):
        self.ownername=ownername
        self.balance=balance
    def _str_(self):
        return 'Account owner:{ownername}\nAccount balance:${balance}'.format(ownername=self.owner,balance=self.balance)
    def deposit(self,dp_money):
        self.balance+=dp_money
        print('deposit accepted,your balance is{balance}'.format(balance=self.balance))
    def withdraw(self,wd_money):
        if wd_money >self.balance:
            print("funds unavailable!")
        else:
            self.balance-=wd_money
            print("withdrawel accepted,your balance is {balance}".format(balance=self.balance))
acct1=Account("jose",100)
print(acct1)
acct1.deposit(50)
acct1.withdraw(75)
acct1.withdraw(500)
