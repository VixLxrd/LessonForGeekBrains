from functools import reduce


def my_func_multi(a, b):
    return a * b


print(reduce(my_func_multi, [i for i in range(100, 1001) if i % 2 == 0]))
