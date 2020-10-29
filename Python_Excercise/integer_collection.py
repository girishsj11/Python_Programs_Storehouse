# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 22:10:33 2020

@author: giri
"""

'''
Read a collection of integers from the user. Display all negative integers, followed by all the zeros, 
followed by all the positive integers.
'''

if __name__ == "__main__":
    numbers = list()
    count = int(input("Enter the count value to have values in user list : "))
    for i in range(1,1+count):
        num = int(input("Enter {} element : ".format(i)))
        numbers.append(num)
        
    numbers.sort()
    print("\ncollection of integers",numbers)