# -*- coding: utf-8 -*-
"""
Created on Mon Feb 20 19:21:58 2023

@author: priya
"""

# Write a program to print fibonacci series upto n terms in python
num = 10
n1, n2 = 0, 1
print("Fibonacci Series:", n1, n2, end=" ")
for i in range(2, num):
    n3 = n1 + n2
    n1 = n2
    n2 = n3
    print(n3, end=" ")

print()