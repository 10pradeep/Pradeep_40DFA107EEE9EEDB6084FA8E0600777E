#challenge 2.1

class BankAccount:
  def __init__(self, account_number, account_holder_name, initial_balance=0.0):
    self.__account_number = account_number 
    self.__account_holder_name = account_holder_name 
    self.__account_balance = initial_balance
  
  def deposit (self, amount):
    if amount > 0 :
     self.__account_balance += amount 
#self__account_balance=self.__account_balance + amount 
     print ( "Deposited ₹{}. New balance :₹{}".format(amount, self.__account_balance))
    else:  
     print("Invalid deposit amount. Please deposit a positive amount. ") 
  def withdraw(self, amount):
   if amount>0 and  amount<=self.__account_balance:
     self.__account_balance -=amount 
#self.__account_balance=self.__account_balance - amount 
     print("Withdrew ₹{}.New balance:₹{}".format ( amount , self.__account_balance))
   else:
     print("Invalid withdrawal amount or insufficient balance.")
  def display_balance(self):
     print("Account balance for {} (Account #{}): ₹{}".format(self.__account_holder_name,self.__account_number,self.__account_balance))
  #create an instance of the bank account class 
account = BankAccount (account_number="123456789", account_holder_name="Pradeep",initial_balance=5000.0)

# Test deposit and withdrawal functionality
account.display_balance()
account.deposit(500.0)
account.withdraw(200.0)
account.display_balance()