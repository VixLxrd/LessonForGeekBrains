from sys import argv


def cash_for_person(hours, rate, bonus):
    try:
        return "Cash for person : (hours * rate) + bonus >>> {}".format(
            (hours * rate) + bonus
        )
    except TypeError:
        return "TypeError: input data is incorrect"


name_script, user_hours, user_rate, user_for_bonus = argv
print(cash_for_person(user_hours, user_rate, user_for_bonus))
