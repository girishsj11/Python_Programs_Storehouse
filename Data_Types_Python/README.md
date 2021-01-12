# Data Types Explanation on Python Language

## String

   - A string is a sequence of characters.
   - A character is simply a symbol. For example, the English language has 26 characters.Computers do not deal with characters, they deal with numbers (binary). Even though you may see characters on your screen, internally it is stored and manipulated as a combination of 0s and 1s.

   	 This conversion of character to a number is called encoding, and the reverse process is decoding. ASCII and
   Unicode are some of the popular encodings used.

   1. Creation of strings :

   	  - Strings can be created by enclosing characters inside a single quote or double-quotes. Even triple quotes can be used in Python but generally used to represent multiline strings and docstrings.

	  > 	# defining strings in Python
	  >	# all of the following are equivalent
	  >	my_string = 'Hello'
	  >		print(my_string)

	  >		my_string = "Hello"
	  >		print(my_string)

	  >		my_string = '''Hello'''
	  >		print(my_string)

	  >		# triple quotes string can extend multiple lines
	  >		my_string = """Hello, welcome to
	  >		           the world of Python"""
	  >		print(my_string)


