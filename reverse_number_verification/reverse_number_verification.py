# -*- coding: utf-8 -*-
"""
Created on Sat Aug 22 20:39:51 2020

@author: giri
"""

#Which is similar to palindrome verification

def reverseCheck(number):
    print("original number is : ", number)
    originalNum = number
    reverseNum = 0
    while (number > 0):
        reminder = number % 10
        reverseNum = (reverseNum * 10) + reminder
        number = number // 10
    if (originalNum == reverseNum):
        return True
    else:
        return False




if __name__ == "__main__":
    number = int(input("Enter the integer number to check whether original & its reversal is same or not :"))
    print("The original and reverse number is the same:", reverseCheck(number))
