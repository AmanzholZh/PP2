# import os
# BASE_URL = os.getcwd()

# for target in os.listdir('.'):
#     target_path = os.path.join(BASE_URL, target)
#     print(target_path)
#     if os.path.isfile(target_path):
#         print(f'file:{target_path}')
#     if os.path.isdir(target_path):
#         print(f'dir:{target_path}')
#         for t in os.listdir(target_path):
#             t_path = os.path.join(BASE_URL, target, t)
#             if os.path.isfile(t_path):
#                 print(f'    file:{t_path}')
#             else:
#                 print(f'    dir:{t_path}')
import os
path = '/home/bekzat/Development/python/'
print("Only directories:")
print([ name for name in os.listdir(path) if os.path.isdir(os.path.join(path, name)) ])
print("\nOnly files:")
print([ name for name in os.listdir(path) if not os.path.isdir(os.path.join(path, name)) ])
print("\nAll directories and files :")
print([ name for name in os.listdir(path)])