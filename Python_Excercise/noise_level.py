# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 22:53:10 2020

@author: giri
"""

'''

The following table lists the sound level in decibels for several common noises.

Noise Decibel level (dB)
Jackhammer 130
Gas lawnmower 106
Alarm clock 70
Quiet room 40

Write a python program that reads a sound level in decibels from the user. If the user enters a 
decibel level that matches one of the noises in the table then your program should display a 
message containing only that noise. If the user enters a number of decibels between the noises 
listed then your program should display a message indicating which noises the level is between. 
Ensure that your program also generates reasonable output for a value smaller than the quietest 
noise in the table, and for a value larger than the loudest noise in the table

'''

def noise_level(noise_table,decibel):
    noise_values = list()
    
    for noise in noise_table.values():
        noise_values.append(noise)
        
    noise_values.sort()
    
    if (decibel<40):
        return ("Sounds good !!")
    elif(decibel>130):
        return ("horrible/loudest sound !!")
    else:
        for key,value in noise_table.items():
            if(decibel==value):
                return ("noise level is : {} ".format(key))
            else:
                continue


if __name__ == "__main__":
    decibel = int(input("Enter the decibel value , program will checks its noise position : "))
    noise_table = {'Jackhammer':130,'Gas lawnmower':106,'Alarm clock':70,'Quiet room':40}
    print(noise_level(noise_table, decibel))