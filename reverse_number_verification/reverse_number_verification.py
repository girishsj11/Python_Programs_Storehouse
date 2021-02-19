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

    
#Which is similar to check the given string has a palindrome in it or not 

def palindrome(string):
    string_list = list()
    for char in string:
        if(string.count(char)!=1):
            string_list.append(char)
    length = len(string_list)
    #print("String list {} and its length is : {}".format(string_list,length))
    if(length==0):
        return "Not a palindrome !!"
    if(length % 2 ==0):
        if(len(set(string_list))==(length//2)):
            return ("its palindrome!!")
        else:
            return ("Not a palindrome")




if __name__ == "__main__":
    string = str(input("Enter the string which you wanted check whether its palindrome in it : "))
    print(palindrome(string))
