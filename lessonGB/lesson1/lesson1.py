# 1
string_var = "String"
bool_var = True
int_var = 56

user_string_var_first = input("Enter the String1")
user_string_var_second = input("Enter the String2")
user_int_var_first = input("Enter a integer number1")
user_int_var_second = input("Enter a integer number2")

print("Number 1 : {}".format(user_int_var_first))
print("Number 2 : {}".format(user_int_var_second))

# 2
user_time = int(input())
# следущая строчка если количество секунд будет больше чем в одном дне
user_time = user_time % 86400
print("Time -> {hours}:{minutes}:{seconds}".format(hours=user_time // 3600,
                                                   minutes=(user_time % 3600) // 60,
                                                   seconds=(user_time % 3600) % 60))
# 3
n = input()
print(int(n) + int(n * 2) + int(n * 3))

# 4
user_var_input = [int(i) for i in input()]
counter = 0
max_element = user_var_input[0]
while counter < len(user_var_input):
    if max_element < user_var_input[counter]:
        max_element = user_var_input[counter]
    counter += 1
print(max_element)

# 5

valueFirst = int(input())
valueSecond = int(input())
if valueFirst >= valueSecond:
    print("Profit!")
    print("Revenue profitability: {0:.2f} %".format((valueFirst - valueSecond) / valueFirst * 100))
    valueFourth = int(input())
    print("Revenue profitability: {0:.0f}".format((valueFirst - valueSecond) / valueFourth))
else:
    print("не Profit...")

# 6
a, b = map(float, input().split())
day = 1
while a < b:
    print("{}-й день: {:.2f}".format(day, a))
    day += 1
    a *= 1.1
else:
    print("{}-й день: {:.2f}".format(day, a))
