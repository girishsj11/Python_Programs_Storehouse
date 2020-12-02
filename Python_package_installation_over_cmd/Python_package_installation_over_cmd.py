#Windows Platform 

import os 

package_file = r'C:\Users\giri\.spyder-py3\Python_Programs\package_installation_over_cmd\Python_Packages.txt'
#provide the file path on the above variable
prerequisite_command = 'pip install '
#pip install string is stored in above variable to do the installation via pip package manager



with open(package_file,'r') as file:
    lines = file.readlines()
    for line in lines:
        package_name = line.split('==')[0]
        print(prerequisite_command+package_name)
        os.system(command=(prerequisite_command+package_name))
        input("click Enter to continue : ") 
        #the above statement is just to keep user eye on the screen , if user doesn't he/she can remove/comment the  above line.
    input("Click Enter to exit ") 
    
   
'''

# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


#Linux Platform 

import os 

#where package file can be taken from other person
package_file = r"/home/giri/.config/spyder-py3/Python_Programs/package_list.txt"

#to install packages in linux we should start with pip3 
pip_command = "pip3 install "

with open(package_file,'r') as file:
    lines = file.readlines()
    for line in lines:
        package_name = line.split('==')[0]
        print(pip_command+package_name)
        os.system(command=(pip_command+package_name))
        #input("click Enter to continue : ") 
        #the above statement is just to keep user eye on the screen , if user doesn't he/she can remove/comment the  above line.
    input("Click Enter to exit ") 

'''
