import re 
print(re.sub(r'(.)([A-Z]{1})', r'\1_\2', "iTriedToWriteNicely").lower())