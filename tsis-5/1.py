import re

pattern = r'ab*'
text = 'ab a abb babb abbb abbbbb bdak asfab'
if re.search(pattern, text):
    print(re.findall(pattern, text))
else:
    print('Not Found')