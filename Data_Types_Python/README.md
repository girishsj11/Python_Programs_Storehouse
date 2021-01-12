# Data Types Explanation on Python Language

## String

   - A string is a sequence of characters and immutable object in python.
   - A character is simply a symbol. For example, the English language has 26 characters.Computers do not deal with characters, they deal with numbers (binary). Even though you may see characters on your screen, internally it is stored and manipulated as a combination of 0s and 1s.

   	 This conversion of character to a number is called encoding, and the reverse process is decoding. ASCII and
   Unicode are some of the popular encodings used.

   1. **Creation of strings :**
   
      - Strings can be created by enclosing characters inside a single quote or double-quotes. Even triple quotes can be used in Python but generally used to represent multiline strings and docstrings.

		     # defining strings in Python
		     # all of the following are equivalent
	             my_string = 'Hello'
		     print(my_string)

		     my_string = "Hello"
		     print(my_string)

		     my_string = '''Hello'''
		     print(my_string)

	       	     # triple quotes string can extend multiple lines
		     my_string = """Hello, welcome to
				the world of Python"""
		     print(my_string)

   2. **Access characters in a string :**
      
      - We can access individual characters using indexing and a range of characters using *slicing*. Index starts from 0. Trying to access a character out of index range will raise an *IndexError*. The index must be an integer. We can't use floats or other types, this will result into *TypeError*.
	
      - Python allows negative indexing for its sequences.The index of -1 refers to the last item, -2 to the second last item and so on. We can access a range of items in a string by using the slicing operator :(colon).
      
		     str = 'programiz'
		     print('str = ', str)

		     #first character
		     print('str[0] = ', str[0])

		     #last character
		     print('str[-1] = ', str[-1])

		     #slicing 2nd to 5th character
		     print('str[1:5] = ', str[1:5])

		     #slicing 6th to 2nd last character
		     print('str[5:-2] = ', str[5:-2])
	
      - If we try to access an index out of the range or use numbers other than an integer, we will get errors.
      
      		 # index must be in range
		    str[15]  
		    ...
		    IndexError: string index out of range

		    # index must be an integer
		    str[1.5] 
		    ...
		    TypeError: string indices must be integers
   
   3. **change or delete a string**
   
      - Strings are immutable. This means that elements of a string cannot be changed once they have been assigned. We can simply reassign different strings to the same name, hence We cannot delete or remove characters from a string. But deleting the string entirely is possible using the del keyword.
      
      		 my_string = 'programiz'
		    my_string[5] = 'a'
		    ...
		    TypeError: 'str' object does not support item assignment
		    my_string = 'Python'
		    my_string
			'Python'
			
      - We cannot delete or remove characters from a string. But deleting the string entirely is possible using the del keyword.
      
      		 del my_string[1]
		    ...
		    TypeError: 'str' object doesn't support item deletion
		    del my_string
		    my_string
		    ...
		    NameError: name 'my_string' is not defined
		    
      - list of all the escape sequences supported by Python
      
	      | First Header  | Second Header |
	      | ------------- | ------------- |
	      | \newline or \n | Backslash and newline ignored |
	      | \\\ | Backslash  |
	      | \\' | Single quote  |
	      | \\" | double quote |
	      | \a | ASCII Bell  |
	      | \b | ASCII Backspace |
	      | \f | ASCII Formfeed |
	      | \n | ASCII Linefeed |
	      | \r | ASCII Carriage Return |
	      | \t | ASCII Horizontal Tab |
	      | \v | ASCII Vertical Tab |
	      | \ooo  | Character with octal value ooo |
	      | \xHH  | Character with hexadecimal value HH |
      
      
      
      
      
