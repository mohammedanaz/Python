import re

with open('SampleText.txt', 'r+') as f:
    content = f.read()
    f.seek(0)
    new_content = re.sub(r'^a', 'A', content)
    f.write(new_content)