# -*- coding: utf-8 -*-
"""
Created on Sat Nov  7 18:11:47 2020

@author: giri
"""
'''
1. Write a python program to simulate a BankAccount class such that it allows us to have a starting 
balance, make deposits, make withdrawals, and get the current balance.
'''


import random

class Bank:
    Bank_name = "First Bank"  
    
    def __init__(self,name,age,mobile,location):
        self.name = name
        self.age = age
        self.mobile = mobile
        self.location = location
        self.balance = 100
        
        
    def account_creation(self):
        print()
        print("Thanks for opening a account in {} , as your new account holder so our {} will deposit {} onto your account as a bonus".format(self.Bank_name,self.Bank_name,self.balance))
        
        account_number = random.randint(1,10000)
        print("Welcome to {}".format(self.Bank_name))
        print("\nPlease find the Your useful details below : ")
        
        print("Name  : {} \nAccount_number : {} \nContact_number : {} \nAccount_balance : {}".format(self.name,account_number,self.mobile,self.balance))


    def deposit(self,amount):
        print("\nThanks for depositing {} \nYour current account balance is : {} ".format(amount,amount+self.balance))
        
    def withdraw(self,amount):
        if(self.balance==100):
            print("Withdraw itself is not possible due to account balance is having only bonus !!")
            print("Please try to deposit first !")
        else:    
            if (amount>self.balance):
                print("\nWrong Entry of amount !! \nThe amount which you entered is more than present account balance")
            else:
                print("\nHope You have received the amount of {} \n Your current account balance is : {}".format(amount,self.balance-amount))
        
      

if __name__ == "__main__":
    choice = str(input("Do you want to open a bank account ? \n if 'Yes', please type 'Y' or 'y' \n if 'No', please Tyep 'N' or 'n' \n: "))
    if(choice == 'Y' or choice == 'y'):
        print("Welcome to Banking Process !")
        name = str(input("Enter your name : "))
        age = int(input("Enter your age : "))
        mobile = int(input("Enter your mobile number : "))
        location = str(input("Enter your location : "))
        
        customer = Bank(name,age,mobile,location)
        customer.account_creation()
        
        
        print("\n1. Deposit")
        print("2. Withdraw")
        selection = int(input("Press 1 for Deposit , 2 for withdraw \n:"))
        
        if (selection == 1):
            amount = int(input("Enter the amount to depsoit onto your account : "))
            if(amount>0):
                customer.deposit(amount)
            else:
                print("Entered amount is less than what bank excepts !")
        elif(selection == 2):
            amount = int(input("Enter the amount to withdraw from your account : "))
            if(amount>0):
                customer.withdraw(amount)
            else:
                print("Entered amount is less than what bank excepts !")
        else:
            print("Wrong Entry ")
        
        
        
    elif(choice=='N' or choice=='n'):
        print("Thanks for contacting us ,Hope in future you may need bank account. will be in touch !!! ")
    
    else:
        print("Wrong Entry , please try again !")
        
        
        