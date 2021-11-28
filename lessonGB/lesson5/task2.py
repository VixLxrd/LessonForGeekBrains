def lines_output(list_input):
    for i in list_input:
        print(f'Срока: {list_input.index(i) + 1}. Слов: {len(i.split())}')


with open('folder_test/text2.txt', 'r', encoding='utf-8') as f:
    try:

        lines = f.readlines()
        lines_output(lines)
    except FileNotFoundError:
        print("Файла не сущетвует")
