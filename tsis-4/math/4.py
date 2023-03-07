# Write a Python program to calculate the area of a parallelogram.
# Length of base: 5
# Height of parallelogram: 6
# Expected Output: 30.0
from operator import length_hint


def  area_of_parallelogram(length, height):
    return length * height
length = float(input())
height = float(input())
print(area_of_parallelogram(length, height))