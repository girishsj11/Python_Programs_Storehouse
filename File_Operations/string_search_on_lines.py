#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  9 22:37:02 2021

@author: giri
"""

file = str(input("Please provide us the input file path here : "))
string = str(input("Enter the string to be search on each line of a file : "))
count = 0

with open(file,'r') as f:
    while True:
        line = f.readline()
        if(''==line):
            #print("File reached its EOF")
            print()
            break
        if(string in line):
            count+=1

print("The total count of a word '{}' in a file is : '{}' ".format(string,count))