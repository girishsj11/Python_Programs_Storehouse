# -*- coding: utf-8 -*-
"""
Created on Sun Nov  8 13:03:38 2020

@author: giri
"""
'''
where program will only writes the 'buffersize' bytes of data from 'infile' to 'outfile'.
to cross verify you can check the size of both 'infile' and 'outfile' files.
'''



infile = "large_text.txt"
outfile = "large_text_copy.txt"
buffersize = 10000 

with open(infile,"r") as file_i:
    with open(outfile,"w") as file_o:
        data_buffer = file_i.read(buffersize) #reading chunk of data from input file & storing in variable
		file_o.write(data_buffer) #writing a chunks of data to the output file
        print("Writing to a file is done !....")
