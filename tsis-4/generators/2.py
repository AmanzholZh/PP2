def even(n):
    yield[i for i in range(n) if i % 2 == 0]
n = int(input())
print(*even(n))