def rcs(st):
    if len(st) <= 1:
        return True
    elif st[0].lower() != st[-1].lower():
        return False
    else:
        return rcs(st[1:-1])

print(rcs('malaxdyalam'))
