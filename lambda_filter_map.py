#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 10 19:26:43 2021

@author: giri
"""

'''
lambda :
 
    In Python, an anonymous function is a function that is defined without a name.
While normal functions are defined using the def keyword in Python, anonymous functions are defined using the lambda keyword.
Hence, anonymous functions are also called lambda functions.
    
    Syntax :
        
        lambda agruments : expression
        
        Lambda functions can have any number of arguments but only one expression. 
        The expression is evaluated and returned. Lambda functions can be used wherever function objects are required.

'''

#Example 1

square = lambda x:x*x
print(square(5))


#Example 2

(lambda x:x/2)(8)
(lambda x:x*x*x)(10)
(lambda fname,lname : f"{fname.upper()} {lname.upper()}")('python','program')


#Example 3

out_function = lambda x , inner_function : x + inner_function(x)
out_function(2,lambda x:x*x)

out_function(3,lambda x:x+2)



'''

filter :
    
    The filter() function in Python takes in a function and a list as arguments.
The function is called with all the items in the list and a new list is returned which contains items for which the function evaluates to True.
Here is an example use of filter() function to filter out only even numbers from a list.

    Syntax :
        
        filter(function, iterable)
        
        - filter() method takes two parameters:

            function - function that tests if elements of an iterable return true or false
            If None, the function defaults to Identity function - which returns false if any elements are false

            iterable - iterable which is to be filtered, could be sets, lists, tuples, or containers of any iterators

'''

#Example 1

chars  = ['a' , 'e' , 'n' , 'o' , 'u' , 'p' , 'y' , 'z' , 'm']

def vowel_search(char):
    vowels = ['a' , 'e' , 'i' , 'o' , 'u']
    
    if(char in vowels):
        return True
    else:
        return False
    
filter_vowels = list(filter(vowel_search,chars))
print(filter_vowels)


#Example 2

print(list(filter(lambda x:x%2==0 , [1,2,3,4,8,9,10,12])))


#Example 3

randomlist = [1,0,'0','1',True,False]

print(list(filter(None,randomlist)))



'''

map :
    
    The map() function applies a given to function to each item of an iterable and returns a list of the results.
The returned value from map() (map object) can then be passed to functions like list() (to create a list), set() (to create a set) and so on.


    Syntax : 
        
        map(function, iterable)
        
        The function is called with all the items in the list and 
        a new list is returned which contains items returned by that function for each item.
        
'''

#Example 1

randomlist = [1,0,'0','1',True,False]

print(list(map(lambda x:int(x)==1,randomlist)))

print(list(map(lambda x:int(x),randomlist)))


#Example 2

num_list = [0,1,2,3,4,5,6,7,8,9,10]

print(list(map(lambda x:x*2 , num_list)))

print(list(map(lambda x:x*x , num_list)))


#Example 3

print(list(map(lambda x:x.upper(),['python','java','c','c++','ruby'])))


    
    

