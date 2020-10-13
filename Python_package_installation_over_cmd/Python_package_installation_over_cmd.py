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
    
