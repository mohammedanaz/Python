import re
txt = 'This is a sample text to test regex.'
pattern = re.compile(r'\bsa')

result = pattern.search(txt)

print(result.string,'\n', result.span(),'\n', result.start(),'\n', result.group())

sub = re.sub(r' ', '-', txt)

print(sub)

txt1 = 'this is a sample text. this contains this.'

pattern = r'(\w+)i(\w+)'
grp1 = re.findall(pattern, txt1)

print(grp1)

first, last = grp1[0]
print(first, last)