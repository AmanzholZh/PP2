def squares(a, b):
    yield [i ** 2 for i in range(a, b)]
a, b = int(input()), int(input())
arr = squares(a, b)
for num in arr:
    print(num)