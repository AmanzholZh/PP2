import os
print('Exist:', os.access('/home/bekzat/Development/python/PP2_2022/lab6/dir-and-files.md/text.txt', os.F_OK))
print('Readable:', os.access('/home/bekzat/Development/python/PP2_2022/lab6/dir-and-files.md/text.txt', os.R_OK))
print('Writable:', os.access('/home/bekzat/Development/python/PP2_2022/lab6/dir-and-files.md/text.txt', os.W_OK))
print('Executable:', os.access('/home/bekzat/Development/python/PP2_2022/lab6/dir-and-files.md/text.txt', os.X_OK))