def area_of_trapezoid(height, first_value, second_value):
    area = (first_value + second_value) / 2 * height
    return area
height = int(input())
first_value = int(input())
second_value = int(input())
print(area_of_trapezoid(height, first_value, second_value))