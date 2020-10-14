# -*- coding: utf-8 -*-
"""
Created on Sat Jul 25 09:39:15 2020

@author: gshambul
"""

'''

input = 1234
given number = 9
output= 12349 , 12394, 12934, 19234,91234

print the max of output list

'''

input_number=int(input("Enter the input number here : " ))
user_num=int(input("Enter the number where it will inserting into the start & end of each digit of input_num which is declared eralier : "))
empty=list()
output_list=list()

# storing the input number as a list of strings 
def string_of_number(empty_list,input_number):
    for i in str(input_number):
        empty_list.append(i)
    return empty_list



if __name__ == "__main__":
    #the below loop will insert the user_num to start & end of each didgits of input_num
    for i in range(0,len(str(input_number))+1,1):
        empty_list=list()
        empty_list=string_of_number(empty_list,input_number)
        empty_list.insert(i,str(user_num))
        empty.append(empty_list)    
    #printing the max number out of empty_list to integer formate
    for i in empty:
        output_list.append(int(''.join(i)))
        
    print("Print the numbers : ",output_list)
    print("Print the maximum number out of output list",max(output_list))