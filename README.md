# Python_Exercises


**Program1.py**

   Given a two list of numbers create a new list such that new list should contain only odd numbers from the first list and even numbers from the second list



**Program2.py**

   Convert two equal length lists into a dictionary


**Program3.py**

   **Leetcode :- First Program**
    Given an array of integers nums and and integer target, return the indices of the two numbers such that they add up to target.You may assume that each input would have exactly one solution, and you may not use the same element twice.You can return the answer in any order.
 
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
 
Constraints:
1 <= nums.length <= 105
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.



**Program4.py**

   John works at a clothing store. He has a large pile of socks that he must pair by color for sale. Given an array of integers representing the color of each sock, 
determine how many pairs of socks with matching colors there are.

For example, there are n=7 socks with colors ar=[1,2,1,2,1,3,2]. 
There is one pair of color 1 and one of color 2 . 
There are three odd socks left, one of each color. The number of pairs is 2 .

   *Function Description

Complete the sockMerchant function in the editor below. It must return an integer representing the number of matching pairs of socks that are available.

sockMerchant has the following parameter(s):

n: the number of socks in the pile
ar: the colors of each sock
    *Input Format

The first line contains an integer n , the number of socks represented in ar .
The second line contains n space-separated integers describing the colors ar[i] of the socks in the pile.

   *Constraints

1<=n<=100
1<=ar[i]<=100 where 0<=i<=n

    where 
   *Output Format

Return the total number of matching pairs of socks that John can sell.

Sample Input

9
10 20 20 10 10 30 50 10 20

Sample Output

3


