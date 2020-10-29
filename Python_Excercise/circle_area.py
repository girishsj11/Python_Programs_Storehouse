# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 20:16:30 2020

@author: giri
"""

'''
Write a python program which accept the radius of a circle from the user and compute the area

'''

import math

def circle_area(radius):
    '''
    Write a python program which accept the radius of a circle from the user and compute the area

    '''
    print("The area of a circle is : {} for a radius value {} ".format((math.pi*radius**2),radius))

if __name__ == "__main__":
    radius = float(input("Enter the radius value in a float format to calculate circle area : "))
    circle_area(radius)