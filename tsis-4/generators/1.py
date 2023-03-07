def square(n):
    yield[i ** 2 for i in range(n)]
print(*list(*square(int(input()))))
