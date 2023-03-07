import os

path = '/home/bekzat/Development/python/PP2_2022/lab6/dir-and-files.md/4.py'

a = path.split('/')
if os.path.exists(path):
    print('this path is exists')
    print('file name:', os.path.basename(path))
    print('dir name:', os.path.dirname(path))
    print('directory is:',a[-2], 'and file is:',a[-1])
else:
    print('this path is not exists')
