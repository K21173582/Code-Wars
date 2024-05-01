# -*- coding: utf-8 -*-
"""
6 kyu - Reverse FizzBuzz

DESCRIPTION:
FizzBuzz is often one of the first programming puzzles people learn. Now undo it with reverse FizzBuzz!

Write a function that accepts a string, which will always be a valid section of FizzBuzz. Your function must return an array that contains the numbers in order to generate the given section of FizzBuzz.

Notes:

If the sequence can appear multiple times within FizzBuzz, return the numbers that generate the first instance of that sequence.
All numbers in the sequence will be greater than zero.
You will never receive an empty sequence.

Examples
reverse_fizzbuzz("1 2 Fizz 4 Buzz")        -->  [1, 2, 3, 4, 5]
reverse_fizzbuzz("Fizz 688 689 FizzBuzz")  -->  [687, 688, 689, 690]
reverse_fizzbuzz("Fizz Buzz")              -->  [9, 10]


"""

def reverse_fizzbuzz(sequence):
    v = sequence.split(' ')
    if any(x.isdigit() for x in v):
        for i, x in enumerate(v):
            if x.isdigit():
                return [int(x) - i + j for j in range(len(v))]

    if v == ['Fizz']: return [3]
    if v == ['Buzz']: return [5]
    if v == ['FizzBuzz']: return [15]
    if v == ['Fizz', 'Buzz']: return [9, 10]
    if v == ['Buzz', 'Fizz']: return [5, 6]