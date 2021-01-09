#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  9 10:23:53 2021

@author: giri

Sorting the list elements without using builtin functions
"""

def list_creation():
    element_count=int(input("Enter the number of elements wanted to be in list:\n"))
    in_list = list()
    if(element_count>0):
        for i in range(element_count):
            print("Enter the {} element : ".format(i+1))
            in_list.append(int(input()))
    
    else:
        print("Please enter the element count more than 0")
        
    return in_list
        
    

def main():
    in_list = list_creation()
    print("list created by user Before sorting: {}  ".format(in_list))
    out_list = list()
    if(len(in_list)>0):
        while in_list:
            minimum = in_list[0]
            for i in in_list:
                if i < minimum:
                    minimum = i
            
            out_list.append(minimum)
            in_list.remove(minimum)
            
        print("list created by user After sorting : {} ",format(out_list))
        
    else:
        print()

if __name__ == "__main__":
    main()