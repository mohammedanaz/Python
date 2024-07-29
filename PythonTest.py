import re
txt = 'This is a sample text to test regex.'
pattern = re.compile(r'\bsa')

result = pattern.search(txt)

print(result)