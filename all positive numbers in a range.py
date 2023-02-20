# -*- coding: utf-8 -*-
"""
Created on Mon Feb 20 19:57:53 2023

@author: priya
"""

def print_positive_numbers(lst):
    positive_numbers = [num for num in lst if num > 0]
    print(positive_numbers)
list1 = [12, -7, 5, 64, -14]
print_positive_numbers(list1)  

list2 = [12, 14, -95, 3]
print_positive_numbers(list2)  