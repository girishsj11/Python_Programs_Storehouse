# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 12:22:02 2020

@author: gshambul
"""


number = int(input("Enter the number , for which you wanted the program to print its factorial answer : "))



#function to calculate the factorial given user input integer number 
def factorial(number):
    factorial = 1 #initial value for the answer is 1 , as we know 0! & 1! is 1
    #and also anything multiply with 1 is anything .
    if(number<=1):
        return factorial
    else:
        factorial = number * factorial(number-1)
    return factorial


if __name__ == "__main__":
    factorial_answer = factorial(number)
    print("The given number is : {} and its equivalent factorial answer is : {}".format(number,factorial_answer))
    

