def amstrong_check(num):
    num_str = str(num)
    sum = 0

    for x in num_str:
        sum += int(x)**len(num_str)
    
    if num == sum:
        print(f"{num} is an Amstrong")
    else:
        print(f"{num} is not an Amstrong")

amstrong_check(9474)