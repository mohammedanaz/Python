def my_gen(n):
    a, b = 0, 1
    yield a
    for i in range(n-1):
        yield b
        a, b = b, a + b

for num in my_gen(2):
    print(num, end=' ')
