def kratnie_3_and_4(n):
    yield [i for i in range(n) if i % 4 == 0 or i % 3 == 0]
n = int(input())
print(*kratnie_3_and_4(n))