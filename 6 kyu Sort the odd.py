"""
6 kyu
Sort the odd

DESCRIPTION:
Task
You will be given an array of numbers. You have to sort the odd numbers in ascending order while leaving the even numbers at their original positions.

Examples
[7, 1]  =>  [1, 7]
[5, 8, 6, 3, 4]  =>  [3, 8, 6, 5, 4]
[9, 8, 7, 6, 5, 4, 3, 2, 1, 0]  =>  [1, 8, 3, 6, 5, 4, 7, 2, 9, 0]

"""

def sort_array(source_array):

    # Extract odd numbers using a for loop
    odd_numbers = []
    for num in source_array:
        if num % 2 != 0:
            odd_numbers.append(num)
    odd_numbers.sort()
    
    # Create an iterator for the sorted odd numbers
    odd_iter = iter(odd_numbers)
    
    # Replace odd numbers in the original array with the sorted ones
    sorted_array = []
    for num in source_array:
        if num % 2 != 0:
            sorted_array.append(next(odd_iter))
        else:
            sorted_array.append(num)
    return sorted_array
