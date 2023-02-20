# -*- coding: utf-8 -*-
"""
Created on Mon Feb 20 20:10:02 2023

@author: priya
"""

my_string = input("Enter a string : ")
count = {}

for letter in my_string:
    if letter in count:
        count[letter] += 1
    else:
        count[letter] = 1

print("Count Frequency is ...")
for key, value in count.items():
    print(f"{key} occurs {value} times")