# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 22:16:37 2020

@author: giri
"""

'''
WAP to swap two numbers without using temporary variable. (Hint Use data structures)
'''

if __name__ == "__main__":
    var1 = int(input("Enter the first variable : "))
    var2 = int(input("Enter the second variable : "))
    print("Beofre swapping : ")
    print("Var1 {} , Var2 {}".format(var1,var2))
    var1,var2 = var2,var1
    print("After swapping : ")
    print("Var1 {} , Var2 {}".format(var1,var2))
    