"""
Created on Mon Sep  7 21:38:35 2020

@author: giri
"""

'''

printing the least number which is generated by system randomly & tracking those numbers too.

'''


import random
if __name__ == "__main__" :
    user_list = list()
    final_range = int(input("Enter the count of elements to be generated by stsem randomly : "))
    random_range = int(input("Enter the final range value to be taken out for genearting a integer numbers randomly : "))
    for _ in range(final_range):
        user_list.append(random.randint(1,random_range))
    print("minimum/least number from the system generated numbers : ",min(user_list))
