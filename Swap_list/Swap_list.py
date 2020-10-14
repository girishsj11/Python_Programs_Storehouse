# -*- coding: utf-8 -*-
"""
Created on Sun Aug 23 20:13:18 2020

@author: giri
"""


'''

Program Motive :- Swap two user input list.

'''



'''

Way 1 : without using third/tempervary variable 

'''

first_list=list()
second_list=list()
element_count=int(input("Enter the number of elements wanted to be in list:\n"))

def list_elements(lists,element_count):
    for i in range(element_count):
        lists.append(int(input()))
    print("Element entries are done")
    print('\n')

def swap_list(first_list,second_list):
    if(len(first_list)==len(second_list)):
        first_list.extend(second_list)
        first_list.reverse()
        for i in range(element_count):
            second_list[i]=first_list.pop()
        first_list.reverse()
        print("After swap fucntion , The lists are : ")
        print(first_list)
        print(second_list)
    else:
        print("can't swap due to difference in size of lists ")

print("Enter the first list elements here:")
list_elements(first_list,element_count)
print("Enter the second list elements here:")
list_elements(second_list,element_count)        
print("Before swap fucntion , The lists are : ")
print(first_list)
print(second_list)
swap_list(first_list,second_list)






'''

Way 2 : with using Tempervary variable 

'''

first_list=list()
second_list=list()
temp_list=list()
element_count=int(input("Enter the number of elements wanted to be in list:\n"))

def list_elements(lists,element_count):
    for i in range(element_count):
        lists.append(int(input()))
    print("Element entries are done")
    print('\n')

print("Enter the first list elements here:")
list_elements(first_list,element_count)
print("Enter the second list elements here:")
list_elements(second_list,element_count)        
print("Before swap fucntion , The lists are : ")
print(first_list)
print(second_list)
print("After swap fucntion , The lists are : ")
temp_list = first_list
first_list = second_list
second_list = temp_list
print(first_list)
print(second_list)



'''

Way 3 : without using any third variable . 

'''

first_list=list()
second_list=list()
element_count=int(input("Enter the number of elements wanted to be in list:\n"))

def list_elements(lists,element_count):
    for i in range(element_count):
        lists.append(int(input()))
    print("Element entries are done")
    print('\n')
    
print("Enter the first list elements here:")
list_elements(first_list,element_count)
print("Enter the second list elements here:")
list_elements(second_list,element_count)        
print("Before swap fucntion , The lists are : ")
print(first_list)
print(second_list)

print("After swap , The lists are : ")
first_list , second_list = second_list , first_list
print(first_list)
print(second_list)
