# -*- coding: utf-8 -*-
"""

6 kyu
Simple Fun #15: Addition without Carrying

Task
A little boy is studying arithmetics. He has just learned how to add two integers, written one below another, column by column. But he always forgets about the important part - carrying.

Given two integers, find the result which the little boy will get.

Example
For param1 = 456 and param2 = 1734, the output should be 1180

    456
   1734
+ ____
   1180
The little boy goes from right to left:

6 + 4 = 10 but the little boy forgets about 1 and just writes down 0 in the last column

5 + 3 = 8

4 + 7 = 11 but the little boy forgets about the leading 1 and just writes down 1 under 4 and 7.

There is no digit in the first number corresponding to the leading digit of the second one, so the little boy imagines that 0 is written before 456. Thus, he gets 0 + 1 = 1.

Input/Output
[input] integer a

A non-negative integer.

Constraints: 0 ≤ a ≤ 99999.

[input] integer b

A non-negative integer.

Constraints: 0 ≤ b ≤ 59999.

[output] an integer

The result that the little boy will get.

"""

def addition_without_carrying(a,b):
    a_str = str(a)  # Convert a to a string
    b_str = str(b)  # Convert b to a string

    # Make the lengths of a_str and b_str equal by adding leading zeros
    max_len = max(len(a_str), len(b_str))
    a_str = a_str.zfill(max_len)
    b_str = b_str.zfill(max_len)

    result_str = ""

    for i in range(max_len):
        digit_a = int(a_str[i])
        digit_b = int(b_str[i])

        # Add the digits and take the last digit of the sum
        sum_digits = (digit_a + digit_b) % 10

        # Add the last digit of the sum to the result
        result_str += str(sum_digits)

    return int(result_str)