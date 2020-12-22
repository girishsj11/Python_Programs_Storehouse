#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 22 16:54:13 2020

@author: giri
"""

'''

fibonaci series evaluation with out using recusrive methods

'''

def main():
    value = [0,1]
    
    if(count==2):
        return value
    
    elif(count<=0 or count==1):
        print("Please enter valid input & input should be positive , greater than 1 !")
        
    else:
        for i in range(count-2):
            value.append(value[i]+value[i+1])
        
        return value
    
if __name__ == "__main__":
    count = int(input("Enter the number to get series of fibonaci numbers : "))
    print(main())
    
    
    

 
