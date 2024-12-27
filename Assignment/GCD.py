#Greatest Common Divisor (GCD) b/w 2 numbers

def gdc(a, b):
    while b:
        a, b = b, a%b

    return a

print(gdc(12, 8))