'''
Program to run 'nslookup <url>' cmd on command prompt , so once it ran it will give us the DNS IP address we have to store it in another output file with specific
url & IP address . 

Pre-requisite : 
    1. Internet connection
    2. Python installed
    3. input.txt file where all urls are being stored



Requirement: 
   Get the IP Address of a given url(from input file) using nslookup and write to a file

Precondition: 
    Have a text file with few web site urls.
e.g. input.txt
        google.com
        facebook.com

Steps:
      1. Read each url
      2. Run command "nslookup <url>"
      3. Filter Out only IP address
      4. Write to an output file with web urls and IP Address

Result
    e.g. output.txt
    google.com:142.250.71.46
    facebook.com:157.240.13.35

'''

import os 

def DnsIpFilter(url_file):
    out_file = 'output.txt'
    pre_command = 'nslookup '
    with open(url_file,'r') as url:
        lines = url.readlines()
        for line in lines:
            line = line.strip('\n')
            command_out = os.popen(pre_command+line)
            with open(out_file,'a+') as out:
                out.write(line+' : '+command_out.read().split()[-1]+'\n')
    print("Check the out_file & input file for the reference")
                

if __name__ == "__main__":
    url_file = str(input("Provide the input text file where all url's are  being stored : "))
    DnsIpFilter(url_file)
