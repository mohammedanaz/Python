
# find longest substring in a string without repeating chars

s = 'abcabcdabc'

result = 0
sub_sting_arr = []

for i in range(len(s)):
    sub_sting_arr.append(s[i])
    for j in range(i+1, len(s)):
        


