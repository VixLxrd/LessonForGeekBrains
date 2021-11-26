list_user = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
print([list_user[j + 1] for j in range(len(list_user) - 1) if list_user[j] < list_user[j + 1]])
