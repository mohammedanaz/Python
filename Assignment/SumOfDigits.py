def sum_of_digits(num):
    num_str = str(num)
    print(sum([int(x) for x in num_str]))

sum_of_digits(123456)