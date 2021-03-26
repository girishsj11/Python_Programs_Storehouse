'''
Program to identify the minimum number among the given list & it has to delete that minimum number by prompting on a sceen , 
then it has to prompt the length of list/array , and above procedure has to be repeat untill the length of an array is 0.

Example : 

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
'''

def min_removal():
    print("Enter the array elements & space between them : \n")
    #l = list(map(lambda x:int(x) , input().split()))
    l=[1,2,5,4,3,0,-2,8,2]
    while l:
        minimum = min(l)
        count = l.count(minimum)
        while(count>=1):
            l.remove(minimum)
            count-=1
        print("minimum value : ",minimum,",length of array : ",len(l))

if __name__ == "__main__":
    min_removal()
