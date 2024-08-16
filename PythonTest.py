
# find longest substring in a string without repeating chars

s = 'abcabcdabc'

result = 0
sub_sting_arr = []
flag = 0

for i in range(len(s)):
    sub_sting_arr.append(s[i])
    if len(sub_sting_arr) > result:
        result = len(sub_sting_arr)
    for j in range(i+1, len(s)):
        if s[j] in sub_sting_arr:
            if j == len(s)-1:
                flag = 1
            sub_sting_arr.clear()
            break
        else:
            sub_sting_arr.append(s[j])
            if len(sub_sting_arr) > result:
                result = len(sub_sting_arr)
            if j == len(s)-1:
                flag = 1
    if flag == 1:
        break

