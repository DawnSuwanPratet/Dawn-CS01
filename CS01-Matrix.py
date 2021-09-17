import numpy as np

print("Enter your columns and rows:")

Columns, Rows = list(map(int, input().split()))
First = []
Second = []

print("Enter your First group of numbers:")

for Column in range(Columns):
    First.append(list(map(int, input().split(maxsplit = Rows - 1))))

print("Enter your Second group of numbers:")

for Column in range(Columns):
    Second.append(list(map(int, input().split(maxsplit = Rows - 1))))

print("Result:")

for Column in range(Columns):
    for Row in range(Rows):
        Result = np.add(First[Column][Row], Second[Column][Row])
        print(Result, end = " ")
    print()