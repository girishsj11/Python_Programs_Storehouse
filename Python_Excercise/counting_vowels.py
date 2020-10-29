# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 20:36:49 2020

@author: giri
"""

'''

Write a function which takes as an input string s and returns the total number of vowels (a, e, i, o, 
or u) that occur in the string

'''

def vowel_count(word):
    '''

    Write a function which takes as an input string s and returns the total number of vowels (a, e, i, o, 
    or u) that occur in the string

    '''
    vowels = ['a','e','i','o','u','A','E','I','O','U']
    count = 0
    for char in word:
        if(char in vowels):
            count+=1
        else:
            continue
    print("The input string '{}' has '{}' vowels in it.".format(word,count))


if __name__ == "__main__":
    word = str(input("Enter the string to know how many vowels in it : "))
    vowel_count(word)