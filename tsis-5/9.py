import re

text = 'LawraInaraFloraElena'
x = re.sub("(.)([A-Z])+?" , r"\1 \2", text)
print(x)
