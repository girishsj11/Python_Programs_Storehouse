# -*- coding: utf-8 -*-
"""
Created on Mon Oct 19 20:26:25 2020

@author: giri
"""
'''
Assignment: Find who tweeted the most

You will be given a list of tweets
Your program should find the user who has tweeted the most

Note:
If multiple users are having same number of tweets, then print all the users in alphabetical order of user names.
Use Python 3
Follow python coding style guide
Only <filename>.py file should be uploaded. Do not upload <filename>.ipnb file

Input format:
Read the input from console.
First line of input should be number of test cases
Remaining lines of input should contain each test case input. 

For each test case input:
First line should contain number of tweets.
Followed by N lines, each containing user name and tweet id separated by a space.

Output format:
Find the user with max number of tweets. Print user name and total number of tweets.


Sample 1:
Input 
1
4
sachin tweet_id_1
sehwag tweet_id_2
sachin tweet_id_3
sachin tweet_id_4

Output
sachin 3


Sample 2:
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



Sample 3:
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

Sample 4:
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

'''

def output_window(user_list):
    print("\nOutput : ")
    user_dict = dict()
    for i in set(user_list):
        user_dict[i]=user_list.count(i)
        
    value = max(user_dict.values())
    
    for i in set(user_list):
        if (user_list.count(i)==value):
            print(i+' '+str(value))
            
    
        
        
def input_window():
    number_of_tweets = int(input("Enter the number of tweets to make : "))
    tweet_id = "tweet_id_"
    
    for i in range(1,1+number_of_tweets):
        number_of_users = int(input("Enter the number of users to have tweet among in social network :"))
        user_list = list()
        for j in range(1,1+number_of_users):
            user = str(input("Enter {} tweeter user name : ".format(j)))
            user_list.append(user)
        
        print("\nInput : ")
        print(number_of_tweets)
        print(number_of_users)
        for index,name in enumerate(user_list):
            print(name+' '+tweet_id+str(index+1))
            
        output_window(user_list) 
        
        
if __name__ == "__main__":
    input_window()
    str(input("\n Press Enter to quit"))


