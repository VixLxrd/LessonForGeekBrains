with open('folder_test/test1.txt', 'w', encoding='utf-8') as f:
    try:
        while True:
            line = input("Введите строку >>> ")
            if line == "":
                break
            f.writelines(line + '\n')
    except EOFError:
        print("Ввод окончен")

with open('folder_test/test1.txt', 'r', encoding='utf-8') as f:
    print(f.read()[:-1])
