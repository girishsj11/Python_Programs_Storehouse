'''
Program to find out the permutations for the given string or numbers(*type : str) by two methods :

method 1 : without builtin function/package 

method 2 : with using builtin package to get permutation

mathematical formual : npr = n!/(n-r)!
but in programming way it has to be : n! (*lenght of input string)

Example : input_string = 'ABC'
          length = len(input_string) = 3
          output_string = 3! = 6 = ['ABC' , 'ACB' , 'BAC' , 'BCA' , 'CAB' , 'CBA'] 
'''

#method 1 : without builtin function/package 

def permutations(input_string, step = 0):

    # if we've gotten to the end, print the permutation
    if step == len(input_string):
        output_string.append("".join(input_string))

    # everything to the right of step has not been swapped yet
    for i in range(step, len(input_string)):

        # copy the string (store as array)
        string_copy = [character for character in input_string]
        print(string_copy)

        # swap the current index with the step
        string_copy[step], string_copy[i] = string_copy[i], string_copy[step]

        # recurse on the portion of the string that has not been swapped yet (now it's index will begin with step + 1)
        permutations(string_copy, step + 1)

if __name__ == "__main__":
    input_string = str(input("Enter your favourite string/number to get its all possible permutations : "))
    output_string = list()
    permutations(input_string)
    print("Total permutations possible is : ",len(output_string))
    print(output_string)
    
    
    
#method 2 : with using builtin package to get permutations

from itertools import permutations

if __name__ == "__main__":
    input_string = str(input("Enter your favourite string/number to get its all possible permutations : "))
    output_string = list()
    for perm in permutations(input_string):
        output_string.append(''.join(perm))
    print("Total permutations possible is : ",len(output_string))
    print(output_string)
                             
