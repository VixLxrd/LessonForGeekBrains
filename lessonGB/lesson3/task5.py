# специальный символ: %

def sum_func():
    sum_number = 0
    spisok = [i for i in input().split()]
    while "%" not in spisok:
        for i in spisok:
            sum_number += int(i)
        spisok = [i for i in input().split()]
    else:
        for i in spisok:
            if i == "%":
                return sum_number
            sum_number += int(i)


print(sum_func())
