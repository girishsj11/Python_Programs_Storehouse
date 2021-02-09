import os

file1_size = os.path.getsize('sample1.txt')
file2_size = os.path.getsize('sample2.txt')

if(file1_size != file2_size):
    print("Contents are vary as bcz size itself is different : file1 {} & file2 {} ".format(file1_size,file2_size))
else:
    with open('sample1.txt','r') as file1 :
        file1_contents = file1.read()
    with open('sample2.txt','r') as file2 :
        file2_contents = file2.read()

    if(file1_contents == file2_contents):
        print("Both file size is same & content also")
    else:
        print("Size is same , but not the contents")

