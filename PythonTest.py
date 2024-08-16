
# find longest substring in a string without repeating chars

s = 'abcabcdabc'

result = 0
sub_sting_arr = []

for i in range(len(s)):
    if s[i] not in sub_sting_arr:
        sub_sting_arr.append(s[i])
        if len(sub_sting_arr) > result:
            result = len(sub_sting_arr)
    else:
        if len(sub_sting_arr) > result:
            result = len(sub_sting_arr)
        sub_sting_arr.clear()
        sub_sting_arr.append(s[i-1])
        sub_sting_arr.append(s[i])



