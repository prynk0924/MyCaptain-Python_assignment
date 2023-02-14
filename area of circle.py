# -*- coding: utf-8 -*-
"""
Created on Tue Feb 14 19:36:34 2023

@author: priyanga
"""
"""
write a python program which accepts the radius of a circle from the user and compute the area

area = pi * (radius^2)

pi=3.1415
"""

from math import pi

radius = float(input("Enter Radius of circle: "))
area = pi * (radius ** 2)

print("Area of circle is: %.2f" %area)
