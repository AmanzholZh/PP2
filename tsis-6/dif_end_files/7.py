file1 = open('text.txt', 'r')
file2 = open('output.txt', 'w')
while file1.readline(): 
    file2.write(f'{file1.readline()}')
file1.close()
file2.close()