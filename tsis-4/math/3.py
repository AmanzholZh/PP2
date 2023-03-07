from math import *
from operator import le
def regular_polygon(size, length):
    return int((size * pow(length, 2) / 4) * (cos(pi / size) / sin(pi / size)))
print(regular_polygon(int(input()), int(input())))  
