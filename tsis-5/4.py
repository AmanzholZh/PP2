import re

pattern = r'[A-Z][a-z]'
text = 'Aty zhonym bolady Toregaly Torali'

if re.search(pattern, text):
    print(re.findall(pattern, text))
else:
    print('Not Found')

# import re
# my_string = 'Aty zhonym bolady Toregaly Torali'
# p = re.compile('[A-Z]+[a-z]+')
# m = p.search(my_string)
# if m:
#     print(p.findall(my_string))
#     print('it\'s a match')
# else:
#     print('no match found')