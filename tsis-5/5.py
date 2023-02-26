import re

pattern = r'\ba{1}.*b\b'
text = 'ab a abb babb abbb abbbbb bdak asfab'
if re.search(pattern, text):
    print(re.findall(pattern, text))
else:
    print('Not Found')