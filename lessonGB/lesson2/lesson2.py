# # 1
# list_user = [25, [print(), map], True, map, EOFError, print]
# for i in list_user:
#     print(type(i))
#
# # 2
# list_user_input = [i for i in input().split()]
# for i in range(0, len(list_user_input) - 1, 2):
#     list_user_input[i], list_user_input[i + 1] = list_user_input[i + 1], list_user_input[i]
#
# # 3
# # list version
# list_times = ["Spring", "Summer", "Autumn", "Winter"]
# num_user = int(input())
# if num_user in [12, 1, 2]:
#     print("It's {}".format(list_times[3]))
# elif num_user in [3, 4, 5]:
#     print("It's {}".format(list_times[0]))
# elif num_user in [6, 7, 8]:
#     print("It's {}".format(list_times[1]))
# elif num_user in [9, 10, 11]:
#     print("It's {}".format(list_times[2]))
# # dictionary version
# dict_user = {"Spring": [3, 4, 5], "Summer": [6, 7, 8],
#              "Autumn": [9, 10, 11], "Winter": [12, 1, 2]}
# num_user = int(input())
# for i, j in dict_user.items():
#     if num_user in j:
#         print("It's {}".format(i))
#
# # 4
# list_words = [i for i in input().split()]
# for i, j in enumerate(list_words):
#     print("line is {} -> {}".format(i + 1, j[0:10]))
#
# # 5
# numbers_user = [7, 5, 3, 3, 2]
# num_input_user = input()
# while num_input_user != "STOP":
#     numbers_user.append(int(num_input_user))
#     numbers_user.sort()
#     numbers_user.reverse()
#     print("Пользователь ввел число {}. Результат : {}.".format(num_input_user,
#                                                                numbers_user))
#     num_input_user = input()

# 6
hi_string = '''Вводите названия, цены, количества и названия еденицы товара
в одну строчку, разделяя слова пробелами'''

str_1 = "Введите количество строк в структуре >>> "

num_str_1 = int(input(str_1))
print(hi_string)
struct_user = []

for i in range(num_str_1):
    name, price, amount, name_s = [i for i in input().split()]
    struct_user.append((i + 1, {"название": name, "цена": price,
                                "количество": amount, "ед": name_s}))
print(struct_user)
struct_user_result = {}
for i in struct_user[i][1].keys():
    result = []
    for j in range(num_str_1):
        result.append(struct_user[j][1][i])
    struct_user_result[i] = result

print(struct_user_result)