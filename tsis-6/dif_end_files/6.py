import os

def create_dir(path):
    if not os.path.exists(path):
        os.mkdir(path)
for i in range(65,91):
    os.makedirs(f'{chr(i)}.txt')
