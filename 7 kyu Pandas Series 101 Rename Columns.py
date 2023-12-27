"""
7 kyu - Pandas Series 101: Rename Columns

DESCRIPTION:
    
Rename Columns

Input parameters
pandas.DataFrame object
sequence

Task
Your function must return a new pandas.DataFrame object with same data than the original input but now its column names are the elements of the sequence. You must not modify the original input.

The number of columns of the input will always be equal to the size of the sequence.

Examples
   0  1  2
0  1  2  3
1  4  5  6

names = ['A', 'B', 'C']
   A  B  C
0  1  2  3
1  4  5  6

"""


import pandas as pd

def rename_columns(df, names):
    for i in range(len(df.columns)):
        df = df.rename(columns = {df.columns[i] : list(names)[i]})
        i += 1
    return df