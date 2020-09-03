# -*- coding: utf-8 -*-
"""
Created on Thu Sep  3 19:47:18 2020

@author: giri
"""


'''

John works at a clothing store. He has a large pile of socks that he must pair by color for sale. 
Given an array of integers representing the color of each sock, 
determine how many pairs of socks with matching colors there are.


For example, there are n=7 socks with colors ar=[1,2,1,2,1,3,2]. 
There is one pair of color 1 and one of color 2 . 
There are three odd socks left, one of each color. The number of pairs is 2 .

Function Description

Complete the sockMerchant function in the editor below. It must return an integer representing the number of matching pairs of socks that are available.

sockMerchant has the following parameter(s):

n: the number of socks in the pile
ar: the colors of each sock
Input Format

The first line contains an integer n , the number of socks represented in ar .
The second line contains n space-separated integers describing the colors ar[i] of the socks in the pile.

Constraints

1<=n<=100
1<=ar[i]<=100 where 0<=i<=n

 where 
Output Format

Return the total number of matching pairs of socks that John can sell.



'''
def list_creation(element_count,input_list):
    print("Enter the elements to be present in list : ")
    for _ in range(element_count):
        input_list.append(int(input()))
    return input_list


def sockMerchant(element_count, input_list):
    elements = set()
    count = 0
    for i in range(element_count):
        if(input_list.count(input_list[i])>=2):
       
            if(input_list[i] in elements):
                continue
            
            else:
                count+=(input_list.count(input_list[i])//2)
                elements.add(input_list[i])
        else:
            continue
          
    return count
        



if __name__ == "__main__":
    element_count = int(input("Enter the count of elements to be present in a list : "))
    input_list = list()
    input_list = list_creation(element_count, input_list)
    output = sockMerchant(element_count, input_list)
    print("input user list is : ",input_list)
    print("pair count is : ",output)

