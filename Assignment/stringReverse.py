def reverse_str(st):
    if len(st) == 1:
        return st
    return st[-1] + reverse_str(st[:-1])

print(reverse_str('Hello'))
