def my_func(lines):
    result, k = 0, 0
    for i in lines:
        try:
            surname, cash = i.split()
            cash = float(cash)
            if cash >= 20000:
                print(f"{surname}")
                result += cash
                k += 1
        except ValueError:
            print("В файле встретилось некрректное значение. Оно не учитывается")
    print(f'Средний оклад -> {result / k}')


str_hi = "Введите фамилию и оклад через пробел >>> "
try:
    with open('folder_test/text3.txt', 'a', encoding='utf-8') as f:
        while True:
            line = input(str_hi)
            if line == "":
                break
            f.writelines(line + '\n')
except FileNotFoundError:
    print("Файла не сущетвует")

with open('folder_test/text3.txt', 'r', encoding='utf-8') as f:
    data = f.readlines()
    my_func(data)
