# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 21:54:31 2020

@author: giri
"""
'''
Write a python script to merge two dictionaries
'''

if __name__ == "__main__":
    dict1 = {'a': 1, 'b': 2, 'c': 3}  #provide first dictionary here
    dict2 = {'a': 5, 'c': 5, 'f': 6}  #provide second dictionary here
    dict1.update(dict2)
    print("final merged dictionary is : ",dict1)
