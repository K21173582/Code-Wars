# -*- coding: utf-8 -*-
"""
6 kyu Almost Even

DESCRIPTION:
We need the ability to divide an unknown integer into a given number of even parts - or at least as even as they can be. The sum of the parts should be the original value, but each part should be an integer, and they should be as close as possible.

Complete the function so that it returns an array of integers representing the parts. If the input number is too small to split it into requested amount of parts, the additional parts should have value 0. Ignoring the order of the parts, there is only one valid solution for each input to your function!

Example:
split_integer(20, 6)  # returns [3, 3, 3, 3, 4, 4]
Inputs
The input to your function will always be valid for this kata.

"""

def split_integer(num, parts):
    
    # Calculate the integer value that each part should ideally have by round down the number divided by it's parts
    x = num // parts
    # Initialise a list to store the parts
    y = []
    
    a = 1
    b = 1
    
    # Fill the list with the integer values calculated earlier
    while a < (parts + 1):
        y.append(int(x))
        a += 1
    
    # Check if the sum of the parts equals the original number
    if sum(y) == num:
        return y
    else:
        # If the sum of parts is less than the original number, adjust the parts by adding 1 to the last part
        while sum(y) < num:
            y[-b] = y[-b] + 1
            b += 1 # Move to the next part
        return y