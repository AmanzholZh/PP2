import re
text = 'this_is_snake_case'
ar = text.split('_')
s = ''
for i in range(len(ar)):
    s += str(ar[i][0].upper()) + str(ar[i][1:])
print(s)

# import re 

# text = 'this_is_camel_case'

# print(re.sub(r'(.)_([a-z])',r'\1\2.upper()',text).lower())

