# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 21:58:49 2020

@author: giri
"""

'''
Write a python function to check a password whether it is good or not? 
A good password is atleast 8 characters long and contains an uppercase letter, a lowercase letter and a number.

'''

def password_verification(password):

    if(len(password)>=8):
        number = 0
        upper_case = 0
        lower_case = 0
        for char in password:
            if(char.isupper()):
                upper_case+=1
            elif(char.islower()):
                lower_case+=1
            elif(char.isnumeric()):
                number+=1
            else:
                continue
        
        if(number>=1 and upper_case>=1 and lower_case>=1):
            print("Your Data will be protected !!")
        
        else:
            print("Your data can't be protected , because it didn't meet the criteria ")
       
    
           
    else:
        print("The entered password didn't met the criteria , so please try again & provide the atleast 8 characters long and contains an uppercase letter, a lowercase letter and a number. ")


if __name__ == "__main__":
    password = str(input("enter your favoirate password for your data protection : "))
    password_verification(password)