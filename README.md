# Python_Exercises
## Programs Motive


## ***Program1.py***

   Given a two list of numbers create a new list such that new list should contain only odd numbers from the first list and even numbers from the second list



## ***Program2.py***

   Convert two equal length lists into a dictionary


## ***Program3.py***

   **Leetcode :- First Program**
   
   Given an array of integers nums and and integer target, return the indices of the two numbers such that they add up to target.You may assume that each input would have exactly one solution, and you may not use the same element twice.You can return the answer in any order.
 
>Examples:

     Example 1:
        Input: nums = [2,7,11,15], target = 9
        Output: [0,1]
        Output: Because nums[0] + nums[1] == 9, we return [0, 1]
     Example 2:
        Input: nums = [3,2,4], target = 6
        Output: [1,2]
     Example 3:
        Input: nums = [3,3], target = 6
        Output: [0,1]
 
>Constraints:

    1 <= nums.length <= 105
    -109 <= nums[i] <= 109
    -109 <= target <= 109
    Only one valid answer exists.


## ***Program4.py***

   competition between user & system generated numbers to conculde who's winner among the random numbers which generates by user , system .
   
   
## ***Program5.py***

   Program is to display least/minimum number which randomly generated by a system . 
   
   
## ***Program6.py***

   Program will display the count of value which is present in a list/array.
   
## ***Program7.py***

   **Program motive :-** There is a saying that "Data scientists spend 80% of their time cleaning data, and 20% of their time complaining about cleaning data." Let's see if you can write a function to help clean US zip code data. Given a string, it should return whether or not that string represents a valid zip code. For our purposes, a valid zip code is any string consisting of exactly 5 digits.

## ***outlook_mail_send_automation***
   **Program motive :-** Sending an automatic mail via outlook app in windows platform

   **Pre-requisite things :**
   - outlook application with email id
 
   **Program execution :** 
   - dispatching the outlook application
   - create items based on request 
   - make the receiver id (To item)
   - have the subject line for the mail initiation 
   - Write the body for the mail automation 
   - if needed any attachment you can add it 
   - then final option is to send 


## ***Masking_user_password***
   **Program motive :-** Mask the user password which user enters on screen
   
   **Pre-requisite things :**
   - pip install getpass
   - pip install stdiomask
   
   **Program Description :**
   - Masking the user password we have 2 methods which can be implemented by using the 2 packages/modules :
     * getpass
       - Where getpass module will not echo's any password which being entered by user.
     * stdiomask
       - Where stdiomask will prompts the user password as asterix or '*'.

## ***Program8.py***

   Convert integer number to its equivalent binary code.
 
## ***Program9.py***

   Program to make the list with unique elements in it which means removing duplicates from it.
   
## ***Python_package_installation_over_cmd***

   **Program motive :-** Installing the required packages automatically via command prompt 
  
   **Pre-requisite things :**
   - Prerequisite file is package_files from another PC who has installed python on his/her system & with some extra packages/modules .
to get the all lists of packages list into a text file , just type " pip freeze > 'file_name.txt' " on your cmd/terminal.

   **Program Description :** 
   - Importing OS module , to run cmd with each package_name which is stored in a <python_packages.txt> file, os.system(command) #which results into a cmd with command
  
   **Useful commands of pip:**
    pip is a package manager for Python packages. When we install pip, it is added to the system as a command line program which can be run from the command line. We not only use pip to install and uninstall Python packages, it is rather a great tool to create Python virtual environment.
    
    - pip search <package_name>
            The above command useful to search a details/content about particular package which is installed on our machine. 
            
    - pip install <package_name>
            The above command useful to install new package onto our machine.
                     
    - pip install --no-cache-dir <package_name> 
            The above command will do the installation from the python package server , not from cache storage which is present on our machine.
         
    - pip show <package_name>
            The above command is usefull when we wanted to know the full info about a specific installed package.
            
    - pip uninstall <package_name>
            The above command useful to uninstall the installed package from our machine.
           
    - pip list
            The above command will list out all installed packages which is present at our machine.
            
    - pip freeze 
            The above command is also does the similar action as pip list does.
           
    - pip install -r <path_to_file>
            The above command will do the installation of each package & version from the file which user will specifies <path_to_file>.
            
    - pip install --upgrade <package_name>
            The above command will installs the upgraded version of package onto system.
            
    - pip check <package_name>
            The above command will shows the whether package is being installed without any issues & making sure that there is no breakage.
     
   ![Difference of show and search](/Python_package_installation_over_cmd/Capture.PNG)**   
   
## ***Program10.py***

   program to sort out only the positive numbers on the list , leave the negative numbers as it is.
display the list .

## ***Program11.py***

   separating the zero's from list to end of the array & sorting the other numbers
(*rather than 0) in a order.

> Ex : input = [1,5,0,3,0,0,2,4] output : [1,2,3,4,5,0,0,0]

## ***Program12.py***

   Program to find out the odd & even numbers from the list of numbers or range of numbers.
> Way1 : when the number is been anded with 1 (*binary) ,then if the LSB or last bit of element is 1 then it will be odd number, else even number.

> Way2 : when the number is been devided by 2 ,then if the gets remainder 1 then it will be odd number, else even number.

## ***Program13.py***
   
   A function should accepts a string as input &  output wants to either capitalize or decapitalize ,each letter based on whether its index number (its position within the string) is divisible by 2.

## ***FizzBuzz***

   **Program Description :** 
   - Program has to print 'Fizz' for the multiple of 3's , and should print 'Buzz' for the multiple of 5's
and if a number which is multiple of both 3&5 then it should print 'FizzBuzz'.
if not the program has to print number itself .

## ***Daily_coding_problems***

   **daily_coding_1.py**
   - Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
   
   **daily_coding_2.py**
   - Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6]
   
   **daily_coding_4.py**
   - Given an array of integers, find the first missing positive integer in linear time and constant space. In other words, 
find the lowest positive integer that does not exist in the array. The array can contain duplicates and negative numbers as well.
For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3


## ***reverse_number_verification or palindrome checks***

The program will ask user to enter a integer number , and will check the reverse of it is same as original or not.
Which is similar to check the given string has a palindrome in it or not .

## ***Swap list***

The program will do the swapping of 2 lists which is been provided by user .
   
## ***factorial_calculation***
   
Program will ask user to give input integer number to get a its equivalent factorial number .

## ***switch_case_implementation*** 

Switch_case_statement implemention as like as in C. 

using dictionary , we can declare 'n' number of operation or condition 
& we can use it as like a swicth case statement which C language & other language supports.
        
    Parameters
    ----------
    operator : TYPE -> String
        DESCRIPTION -> with help of operator the function will returns its operation. 
    num1 : TYPE -> int
        DESCRIPTION -> a integer number to do all mathematical operations
    num2 : TYPE -> int
        DESCRIPTION -> a integer number to do all mathematical operations

    Returns
    -------
            the function returns the expresions/operations from 2 input numbers with help of operator variable.
            

## ***integer_to_roman_conversion*** 

Program will do the conversion of real integers to equivalent roman numerals:
- it will ask user to enter the integer number.
- it will display its equivalent roman numerals


## ***quick_sort_algorithm***

Program will do the sorting algorithm on the list with out using an inbuilt 'list.sort()' method.

- it will ask the number of elemnents  to be present in a list 
- it will ask you enter the elements till hits the count of final (*step 1 result)
- program will displays the list before & after sorting algorthim .

## ***max_out_of_integers***

program will ask the user to enter one integer number & also ask user to enter one more digit number . 
where the second user input digit will be inserting into each start + end position of digits in the first user input number , prints out the max one .

>Example:

     input = 1234 
     given number = 9 
     output= 12349 , 12394, 12934, 19234,91234
     max_output = 91234
   

## ***student_ranking_series***

- The first python file is 'input_file_creation.py' will creates a student database by getting all required information fro user , if user doesnot know the name of a student & his/her subjects , then it will consider the defaults names into a 'student_database.txt' file.

- So after execution of 'input_file_creation.py' will get 'student_database.txt' file in this way:

   Student_name-[series],subject_name-[marks],subject_name-[marks],subject_name-[marks]
  
- Then we will use the above 'student_database.txt' file to create 'student_database_ranking.txt' file by using 'output_file_creation.py' file.
- So after execution of 'output_file_creation.py' will get 'student_database_ranking.txt' file in this way:

   Student_name-[series],subject_name-[marks],subject_name-[marks],subject_name-[marks],Total_marks-[total_score],Rank-[rankseries]

     **One more assumption that user have one input.txt file which contains students name , and his/her marks of 3 subjects , program has to find out his/her total marks & his/her rank series among all the other students.**

***Things:***
* main program is :- rank_series_calculation.py
* input file is :- input.txt
* output file is :-  output.txt

input.txt file looks like below :

![input_txt file](/student_ranking_series/input_txt.PNG) 




output.txt file should looks like below:

![output_txt file](/student_ranking_series/output_txt.PNG)


## ***Find who tweeted the most***

- You will be given a list of tweets, Your program should find the user who has tweeted the most.

   **Note:**
   - If multiple users are having same number of tweets, then print all the users in alphabetical order of user names.
   - Use Python 3
   - Follow python coding style guide

>Input format:

     - Read the input from console.
     - First line of input should be number of test cases
     - Remaining lines of input should contain each test case input. 

>For each test case input:

     - First line should contain number of tweets.
     - Followed by N lines, each containing user name and tweet id separated by a space.
     
>Output format:

     - Find the user with max number of tweets. Print user name and total number of tweets.
     
>Examples:
     
     - Example 1:
                  Input 
                  1
                  4
                  sachin tweet_id_1
                  sehwag tweet_id_2
                  sachin tweet_id_3
                  sachin tweet_id_4

                  Output
                  sachin 3
   
     - Example 2:
                  Input 
                  1
                  6
                  sachin tweet_id_1
                  sehwag tweet_id_2
                  sachin tweet_id_3
                  sehwag tweet_id_4
                  kohli tweet_id_5
                  kohli tweet_id_6

                  Output
                  kohli 2
                  sachin 2
                  sehwag 2
                  
     - Example 3:
                  Input 
                  2
                  4
                  sachin tweet_id_1
                  sehwag tweet_id_2
                  sachin tweet_id_3
                  sehwag tweet_id_4
                  5
                  dhoni tweet_id_10
                  dhoni tweet_id_11
                  kohli tweet_id_12
                  dhoni tweet_id_13
                  dhoni tweet_id_14

                  Output
                  sachin 2
                  sehwag 2
                  dhoni 4
                 
     - Example 4:
                  Input
                  3
                  4
                  sehwag tweet_id_2
                  sehwag tweet_id_4
                  sachin tweet_id_1
                  sachin tweet_id_3
                  7
                  sehwag tweet_id_10
                  sehwag tweet_id_11
                  kohli tweet_id_12
                  sachin tweet_id_13
                  sachin tweet_id_14
                  sachin tweet_id_1
                  sehwag tweet_id_4
                  5
                  sachin tweet_id_2
                  kohli tweet_id_4
                  kohli tweet_id_1
                  kohli tweet_id_3
                  sachin tweet_id_5

                  Output
                  sachin 2
                  sehwag 2
                  sachin 3
                  sehwag 3
                  kohli 3
          
## ***Python Excercise***

https://github.com/girishsj11/Python_Programs_Storehouse/blob/master/Python_Excercise/Python_Excercises_session1.pdf
   
## ***chunk_of_data_writing_to_file***

 Program takes input text file & buffersize which defines the how many bytes of program will writtens to the output text file.


## ***Fibonacci Series Evaluation***

Program to generate user defined set of numbers of fibonaci series.
    
## ***sorting_list_without_builtin_function***

Program is used to display the sorting elements from list with out using the builtin sort() method.

## ***File_Operations***

### string_search_on_lines.py

Where program will search for a user input string on each lines of file untill unless it reaches to its end of line(EOF).

### files_contents_verification

Where program will verifies the contents inside 2 files whether both are same or not.

### file tree

Where python program will try to print the file/directory structure in Tree way , like below :

![Tree Image](/File_Operations/File_Tree/tree.PNG)

## ***special_chars_in_string.py***

   Where program will asks user to enter the string with some special characters , then after that program will gives the total count of special characters are in string & which are those & how many are there.

## ***nslookup_cmd.py***

   Program to run 'nslookup <url>' cmd on command prompt , so once it ran it will give us the DNS IP address we have to store it in another output file with specific
url & IP address . 

Pre-requisite : 
1. Internet connection
2. Python installed
3. input.txt file where all urls are being stored
   
   
## ***lambda_filter_map.py***

- **lambda**

   In Python, an anonymous function is a function that is defined without a name.While normal functions are defined using the def keyword in Python, anonymous functions are defined using the lambda keyword.Hence, anonymous functions are also called lambda functions.
   
   Syntax :
   
   > lambda agruments : expression

- **filter**

   The filter() function in Python takes in a function and a list as arguments.
The function is called with all the items in the list and a new list is returned which contains items for which the function evaluates to True.
Here is an example use of filter() function to filter out only even numbers from a list.
   
   Syntax :
   
   > filter(function, iterable)
   

- **map**

   The map() function applies a given to function to each item of an iterable and returns a list of the results.
The returned value from map() (map object) can then be passed to functions like list() (to create a list), set() (to create a set) and so on.
   
   Syntax :
   
   > map(function, iterable)
   
   
## ***Conversion_of_list_to_dictionary.py***

   The program will converts input list to a dictionary with using inbuilt method & also with out using an inbuilt method.
   
## ***prime_numbers_generations.py***

   The program is used to generate a prime numbers in range of lower & upper values.

## ***reverse_string_with_capitalize.py***

   The program will asks user to enter a string & it will reverse the each words by capitalizing the first character.
   
   
## ***Adding_bullet_points_to_paragraph.py***

   Where program will adds a bullet * point to new line of text in a paragraph.

## ***finding_permutations.py***

   Program to display & calculate the all the possible permutations for the given user string.

## ***Terminate_program.py***

   By terminating the whole program for certain condition , we can call 'os' module & call exit function from it.

## ***String_validators.py***

   Program to check built-in string validation methods for basic data. It can check if a string is composed of alphabetical characters, alphanumeric characters, digits, etc.
   Task is to find out if the string contains: alphanumeric characters, alphabetical characters, digits, lowercase and uppercase characters. 
   
## ***Bubble_sort.py***

   Bubble Sort is the simplest sorting algorithm that works by repeatedly swapping the adjacent elements if they are in wrong order.
   
## ***Binary_search.py***

   This search algorithm takes advantage of a collection of elements that is already sorted by ignoring half of the elements after just one comparison. 

- Compare x with the middle element.
- If x matches with the middle element, we return the mid index.
- Else if x is greater than the mid element, then x can only lie in the right (greater) half subarray after the mid element. Then we apply the algorithm again for the right half.
- Else if x is smaller, the target x must lie in the left (lower) half. So we apply the algorithm for the left half.

## ***min_removal.py***

   Program to identify the minimum number among the given list & it has to delete that minimum number by prompting on a sceen , 
then it has to prompt the length of list/array , and above procedure has to be repeat untill the length of an array is 0.

> Example : 

input : 

    array = [1,2,5,4,3,0,-2,8,2]

output :

    minimum value : -2 ,length of array :  8
    minimum value :  0 ,length of array :  7
    minimum value :  1 ,length of array :  6
    minimum value :  2 ,length of array :  4
    minimum value :  3 ,length of array :  3
    minimum value :  4 ,length of array :  2
    minimum value :  5 ,length of array :  1
    minimum value :  8 ,length of array :  0

   
## ***anagram_check.py***   

   An anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once. 
> For example: the word anagram itself can be rearranged into nagaram, also the word binary into brainy and the word adobe into abode.
   
## ***start_up***
   
   A startup program has to run the python script on every restarts of machine based on the first time input counter value.
> We have written start_up.py script which shows few information before it restarts the local machine , and we have to place the start_up.cmd file in startup folder(shell:startup on run command).
