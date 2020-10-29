# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 21:12:07 2020

@author: giri
"""

'''
WAP which accepts a filename from the user and print the extension of that.
'''

if __name__ == "__main__":
    file = str(input("Give us the file name with its path or type manually : "))
    print("The extension of file is : ",file.split('.')[1])