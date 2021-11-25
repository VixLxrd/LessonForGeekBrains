def dividing(first, second):
    """
    Dividing first number by second number ;)

    :param first: First number
    :type first: float
    :param second: Second number
    :type second: float
    :return: result division
    """
    if second == 0:
        return ZeroDivisionError
    return first / second


a, b = map(float, input("Введите два числа >>> ").split())
dividing(a, b)
