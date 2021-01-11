#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 11 19:00:49 2021

@author: giri
"""

#method 1 

list_in = [1,2,3,4,5]
iterator = iter(list_in)        
dict_out = dict(zip(iterator,iterator))



#method 2

list_in = [1,2,3,4,5]
dict_out = dict()
for key,value in enumerate(list_in):
    dict_out[key] = value
print(dict_out)



#method 3 using dictionary builtin function

list_in=[1,2,3,4,5]
print(dict.fromkeys(list_in,'Value'))
