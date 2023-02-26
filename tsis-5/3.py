import re

pattern = r'[a-z]_[a-z]'
text = 'ab a abb  b_ab_b  _a_b_b_b_ b_d  _a_k a_s_  f_ab'

if re.search(pattern, text):
    print(re.findall(pattern, text))
else:
    print('Not Found')