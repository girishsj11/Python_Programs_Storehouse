#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 10 12:20:37 2021

@author: giri
"""

def main():
    string = str(input("Enter the string : "))
    lower_letters = [chr(x) for x in range(97,97+26)]
    special_char = dict()
    for i in string.lower():
        if (i in lower_letters):
            continue
        else:
            try :
                special_char[i] += 1
                #if the key/special character present on dictionary , then we need to increment the value of it
            except KeyError :
                special_char[i] = 1
                #if the key/special character is not present then, creating a key with it & putting value with 1 
        
    print("Toatl count of special characters in input string is : {}".format(sum(special_char.values())))
    print("Number of special characters in input string is : {}".format(len(special_char.keys())))
    print("Special characters are : {}".format([x for x in special_char.keys()]))


if __name__ == "__main__":
    main()