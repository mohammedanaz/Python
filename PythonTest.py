
# find longest substring in a string without repeating chars

s = 'abcabcdabc'

result = 0
sub_string_arr = []
flag = 0

length = 0
sub_string_arr = []
flag = 0

for i in range(len(s)):
    if s[i] not in sub_string_arr:
        sub_string_arr.append(s[i])
        length = max(length, len(sub_string_arr))
    else:
        j = sub_string_arr.index(s[i])
        while j >= 0:
            sub_string_arr.pop(j)
            j -= 1
        
        sub_string_arr.append(s[i])
        length = max(length, len(sub_string_arr))
