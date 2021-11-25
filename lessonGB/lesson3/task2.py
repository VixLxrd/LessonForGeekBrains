def print_inf(v1, v2, v3, v4, v5, v6):
    return "Имя: {}, Фамилия: {}, Год: {}, Город: {}, Email: {}, Телефон: {}".format(v1, v2, v3, v4, v5, v6)


name, surname, year, city, email, phone = [i for i in input().split()]
print(print_inf(v1=name, v2=surname, v3=year, v4=city, v5=email, v6=phone))
