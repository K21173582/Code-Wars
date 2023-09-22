# -*- coding: utf-8 -*-
"""
Created on Fri Sep 22 17:41:28 2023

@author: rakes
"""
#7 kyu Bingo ( Or Not )

#DESCRIPTION:
#For this game of BINGO, you will receive a single array of 10 numbers from 1 to 26 as an input. Duplicate numbers within the array are possible.

#Each number corresponds to their alphabetical order letter (e.g. 1 = A. 2 = B, etc). Write a function where you will win the game if your numbers can spell "BINGO". They do not need to be in the right order in the input array. Otherwise you will lose. Your outputs should be "WIN" or "LOSE" respectively.


def bingo(array):
    # Create a dictionary to map numbers to their corresponding letters
    alphabet_dict = {i: chr(i + 64) for i in range(1, 27)}
    
    # Initialize a set to keep track of the letters we have
    letter_set = set()
    
    # Loop through the input array and add the corresponding letters to the set
    for num in array:
        if num in alphabet_dict:
            letter_set.add(alphabet_dict[num])
    
    # Check if we have all the letters needed to spell "BINGO"
    if set("BINGO").issubset(letter_set):
        return "WIN"
    else:
        return "LOSE"

