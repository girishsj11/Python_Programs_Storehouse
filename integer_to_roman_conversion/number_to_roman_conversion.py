# -*- coding: utf-8 -*-
"""
Created on Thu Jul 23 12:23:12 2020

@author: gshambul
"""

'''

The program will accepts the input integre number from the user & will display the equivalent of Roman letters 

'''

int_number = int(input("Enter the integer number to conver it to Roman equivalent : "))

class Roman_conversion:
    
    
    def __init__(self,number):
        self.number = number
        self.roman=''
        self.integer_numbers = [1000, 900,  500, 400, 100,  90, 50,  40, 10,  9,   5,  4,   1]
        self.roman_letters = ['M',  'CM', 'D', 'CD','C', 'XC','L','XL','X','IX','V','IV','I']
        
        
    def int_to_roman_conversion(self):
        if (self.number == 0):
            self.roman=str(self.number)
            
        
        else:
            for i in range(len(self.integer_numbers)):
                count = int(self.number/self.integer_numbers[i])
                if(count>0):
                    self.roman+=(count*self.roman_letters[i])
                    self.number-=(count*self.integer_numbers[i])
                else:
                    continue
        
        print("The input integer is '{}' and its equivalent roamn numeral numeral is : '{}' ".format(int_number,self.roman))
                
        
    
if __name__ == '__main__':
    R = Roman_conversion(int_number)
    R.int_to_roman_conversion()              
                
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
if __name__ == '__main__' :
    R = Roman_conversion(int_number)
