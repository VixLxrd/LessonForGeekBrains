def my_func(a, b, c):
    spisok = [a, b, c]
    spisok.remove(min(spisok))
    return sum(spisok)


a, b, c = map(int, input().split())
print(my_func(a, b, c))
