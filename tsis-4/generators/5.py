def rev(n):
    yield [i for i in range(n, 0, -1)]
n = int(input())
num = rev(n)
print(*num)