dictionary_output = {}
with open("folder_test/text6.txt", "r", encoding="utf-8") as f:
    data = f.readlines()
    for i in data:
        data_ex = i.replace('(л)', '').replace('(пр)', '').replace('(лаб)', '').replace('—', '')
        course_name = data_ex.split(":")[0]
        total_hours = sum(map(int, data_ex.split(":")[1].split()))
        dictionary_output[course_name] = total_hours

print(dictionary_output)
