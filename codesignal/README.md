## CodeSignal app Python challenges 

### amendTheSentence.py

You have been given a string s, which is supposed to be a sentence. However, 
someone forgot to put spaces between the different words, and for some reason they capitalized the first letter of every word. 
Return the sentence after making the following amendments:

Put a single space between the words.
Convert the uppercase letters to lowercase.

***Example:***
> For s = "CodesignalIsAwesome", the output should be - amendTheSentence(s) = "codesignal is awesome";

> For s = "Hello", the output should be - amendTheSentence(s) = "hello"


### firstDuplicate.py

Given an array a that contains only numbers in the range from 1 to a.length, 
find the first duplicate number for which the second occurrence has the minimal index. 
In other words, if there are more than 1 duplicated numbers, return the number for which the second occurrence has a smaller index than the second occurrence of the other number does. If there are no such elements, return -1.

***Example:***
> For a = [2, 1, 3, 5, 3, 2], the output should be firstDuplicate(a) = 3.

There are 2 duplicates: numbers 2 and 3. The second occurrence of 3 has a smaller index than the second occurrence of 2 does, so the answer is 3.

> For a = [2, 2], the output should be firstDuplicate(a) = 2;

> For a = [2, 4, 3, 5, 1], the output should be firstDuplicate(a) = -1.

***Input/Output***

[execution time limit] 4 seconds (py3)

[input] array.integer a

***Guaranteed constraints:***
1 ≤ a.length ≤ 105,
1 ≤ a[i] ≤ a.length.

***[output] integer***

The element in a that occurs in the array more than once and has the minimal index for its second occurrence. If there are no such elements, return -1.


### strstr.py

Avoid using built-in functions to solve this challenge. Implement them yourself, since this is what you would be asked to do during a real interview.
Implement a function that takes two strings, s and x, as arguments and finds the first occurrence of the string x in s. 
The function should return an integer indicating the index in s of the first occurrence of x. If there are no occurrences of x in s, return -1.

***Example:***
> For s = "CodefightsIsAwesome" and x = "IA", the output should be - strstr(s, x) = -1;

> For s = "CodefightsIsAwesome" and x = "IsA", the output should be - strstr(s, x) = 10.

***Input/Output***

[execution time limit] 4 seconds (py3)

***[input] string s & string x***

A string containing only uppercase or lowercase English letters.

***Guaranteed constraints:***
1 ≤ s.length ≤ 106.
1 ≤ x.length ≤ 106.

***[output] integer***

An integer indicating the index of the first occurrence of the string x in s, or -1 if s does not contain x.

