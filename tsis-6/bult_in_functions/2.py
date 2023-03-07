import re
text = input()
pattern = r'[a-z]'
pattern_ = r'[A-Z]'
low = re.findall(pattern, text)
upp = re.findall(pattern_, text)

print(len(low), len(upp))
