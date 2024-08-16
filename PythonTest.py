
# find longest substring in a string without repeating chars

s = 'abcabcdabc'

result = 0
sub_sting_arr = []

for x in s:
    if x not in sub_sting_arr:
        sub_sting_arr.append(x)
        if len(sub_sting_arr) > result:
            result = len(sub_sting_arr)
    else:
        flag = 1
        if len(sub_sting_arr) > result:
            result = len(sub_sting_arr)
        sub_sting_arr.clear()
        sub_sting_arr.append(x)


