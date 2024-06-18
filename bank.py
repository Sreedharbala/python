import random
from random import randint

 
class savingAccount(Account):
   def __init__(self):
      self.savingAccount={}

   def createAccount(self,name,initialdeposit):
      print()
      self.accountNumber = random.randint(10000,99999)
      self.savingAccount[self.accountNumber] = [name,initialdeposit]
      print("Account creation is successful.your account number is:",self.accountNumber)
      print( )
