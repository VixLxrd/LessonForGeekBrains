# Генерация файла
# from random import choice
# from random import randrange
#
# l = ["ИП", "ООО", "АО", "ПАО", "НКО", "ОП"]
# with open("folder_test/text7.txt", "w", encoding="utf-8") as f:
#     for i in range(15):
#         data = f.writelines(f'firm_{i + 1} {choice(l)} {randrange(8000, 100000)} {randrange(5000, 10000)}' + '\n')
#
import json
from json import dump
from json import load

list_output = []
with open("folder_test/text7.txt", "r", encoding="utf-8") as f:
    data = f.readlines()
    result = [0, 0]
    profit, average_profit, loss = {}, {}, {}
    for i in data:
        name_firm, name_form, var1, var2 = i.split()
        inter_res = int(var1) - int(var2)
        if inter_res < 0:
            loss[name_firm] = abs(inter_res)
        else:
            profit[name_firm] = inter_res
            result[0] += inter_res
            result[1] += 1
    average_profit["average_profit"] = float("{0:.2f}".format(result[0] / result[1]))
    list_output.append({"profit": profit})
    list_output.append(average_profit)
    list_output.append({"loss": loss})
    with open("folder_test/text7.json", "w", encoding="utf-8") as j:
        dump(list_output, j)

# Вывод для проверки, что все супер (так же в этом можно убедиться, если помотреть text7.json)
with open("folder_test/text7.json", "r", encoding="utf-8") as j:
    print(load(j))
