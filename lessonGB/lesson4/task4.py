list_user = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
print([list_user[j] for j in range(len(list_user)) if
       list_user[j] not in list_user[:j] and list_user[j] not in list_user[j + 1:]])
