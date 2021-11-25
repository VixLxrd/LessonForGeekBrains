def int_func(word):
    return chr(ord(word[0]) - 32) + word[1:]

# Для одного слова
print(int_func('text'))

# Для строки из слов
print(*[int_func(i) for i in input().split()])