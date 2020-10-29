# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 20:56:51 2020

@author: giri
"""

'''
Write a Python Program which accepts a sequence of comma separated numbers from user and 
generate a list and tuple with those numbers.
'''

def list_tuple_generation(numbers):
    '''
    Write a Python Program which accepts a sequence of comma separated numbers from user and 
    generate a list and tuple with those numbers.
    '''
    list_of_numbers = list()
    numbers = numbers.strip(',')
    
    for num in numbers.split(','):
        list_of_numbers.append(int(num))
        
    print("List of numbers : {} \ntuple of numbers : {} ".format(list_of_numbers,tuple(list_of_numbers)))


if __name__=="__main__":
    numbers = str(input("Enter the numbers with a comma separated between each numbers : "))
    list_tuple_generation(numbers)