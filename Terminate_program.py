'''
We can run the python files or script or code on notepad++ , we have plugin called 'PyNPP' install it & use it.
write a code in python & save it as .py , run it with alt+shift+F5 key.

By terminating the whole program for certain condition , we can call 'os' module & call exit function from it.
'''

import os
def main():
    print("Hello world!")
    print("Bye to main function !!")

if __name__ == "__main__":
    main()
    if("exit"==str(input("type exit to from the cmd window : ")).lower()):
        os._exit(1)
    
