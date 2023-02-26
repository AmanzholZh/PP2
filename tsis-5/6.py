import re

text = 'my, .name_is Bekzat. '
y = re.sub("\." , ":", text)
x = re.sub(" " , ",", text)

print(y)
print(x)