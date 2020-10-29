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
    value_list = list()
    out_dictionary = dict()
    
    for value in dictionary.values():
        value_list.append(value)
        
    value_list.sort()
    
    for value in value_list:
        for key in dictionary.keys():
            if(value == dictionary.get(key)):
                out_dictionary[key]=value
            else:
                continue
            
    print("sorted dictionary based on dict values : ")
    print("Before sorting : {} \nAfter sorting : {} ".format(dictionary,out_dictionary))
        
    


if __name__ == "__main__":
    #provide the dictionary below 
    dictionary = {'a':5,'b':6,'c':3,'d':2,'e':1,'f':5}
    sort_out(dictionary)