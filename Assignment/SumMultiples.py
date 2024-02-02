def sum_multiples(limit):
    sum = 0
    for i in range(1, limit+1):
        if i % 3 == 0 or i % 5 ==0:
            sum += i
    print(f"The sum is: {sum}")

sum_multiples(50)