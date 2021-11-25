def my_func(a, b):
    return a ** b


def my_func_2(a, b):
    counter = 1
    for i in range(abs(b)):
        a *= a
    return 1 / a
