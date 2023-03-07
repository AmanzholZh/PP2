file = open('text.txt', 'r')
# while file.readline():
#     cnt += 1
# print(cnt)
print(len(file.readlines()))
file.close()
