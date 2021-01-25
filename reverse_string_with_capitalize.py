# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 20:53:39 2021

@author: giri
"""

'''

Checking the entered string is palindrome or not :

def checkPalindrome(inputString):
    emptystring = ''
    for char in inputString:
        emptystring = char + emptystring
    
    if(emptystring == inputString):
        return True
    return False




''''



def main():
    '''
    Accepts a string from user 
    
    Returns
    -------
    reversing of each words in a complete string by capitalizing it

    '''
    string = str(input("Enter the string to make it reverse each words with capitalizing : "))
    out_string = ''
    
    string_split = string.lower().split()
    
    for words in string_split:
        empty = ''
        for char in words:
            empty = char+empty
            
        out_string += empty.capitalize()+' '
        
    print(out_string)


if __name__ == "__main__":
    main()
