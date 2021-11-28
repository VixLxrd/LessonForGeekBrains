words = {
    'One': "Один",
    "Two": "Два",
    "Three": "Три",
    "Four": "Четыре"
}

with open("folder_test/test4a.txt", "r", encoding="utf-8") as file_1:
    data_ex = file_1.readlines()
    with open("folder_test/test4b.txt", "w", encoding="utf-8") as file_2:
        for i in data_ex:
            for j in words.keys():
                    if j in i:
                        bif = i.replace(j, words[j])
                        file_2.write(bif)
