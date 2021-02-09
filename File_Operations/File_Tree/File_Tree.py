import os

def Tree(root_path):
	print(root_path)
	for path,dirs,files in os.walk(root_path):
		#print(path)
		if(len(dirs)!=0):
			for each in dirs:
				print('|')
				print(' -----',each)
				for file in files:
					print('     |')
					print('      -----',file)
		else:
			for file in files:
				print('|')
				print(' -----',file)
		#print('\n')

if __name__ == "__main__":
    root_path = str(input("Enter the root path here to get the folder structure on Tree format : "))
    Tree(root_path)