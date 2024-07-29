import re
txt = 'This is a sample text to test regex.'
pattern = re.compile(r'\bsa')

result = pattern.search(txt)

print(result.string,'\n', result.span(),'\n', result.start(),'\n', result.group())

sub = re.sub(r' ', '-', txt)

print(sub)

txt1 = 'Adam is here'

result1 = re.search(r'\bA[a,d,m]{3}', txt1)

print(result1.group())