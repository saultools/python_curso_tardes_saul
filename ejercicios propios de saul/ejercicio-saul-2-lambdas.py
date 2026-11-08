numeros = [1, 2, 3, 4, 5]
print(list(map(lambda x: x**2, numeros))) # [1, 4, 9, 16, 25]
print(list(filter(lambda x: x % 2 == 0, numeros))) # [2, 4]

from functools import reduce
print(reduce(lambda a, b: a + b, numeros)) # 15

