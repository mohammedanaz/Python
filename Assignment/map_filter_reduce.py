from functools import reduce

lst  = [1, 2, 3, 4, 5]

thrice = map(lambda x: 3 * x, lst)

evens = filter(lambda X: X % 2 == 0, thrice)

sum = reduce(lambda x, y: x + y, evens)

print(sum)