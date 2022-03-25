# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 21:18:48 2020

@author: giri
"""

'''
Write a python script to sort a dictionary by value.
'''

def sort_out(dictionary):
    '''
    Write a python script to sort a dictionary by value.
    '''
    list_items = list(dictionary.items())
    list_items.sort(key=lambda x:x[1])
    print("Sorted Dictionary based on value is : ",dict(list_items))
        

if __name__ == "__main__":
    #provide the dictionary below 
    dictionary = {'a':5,'b':6,'c':3,'d':2,'e':1,'f':5}
    sort_out(dictionary)
