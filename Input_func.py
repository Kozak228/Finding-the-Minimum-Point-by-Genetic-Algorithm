from Proverka import proverka_brekets

def input_func(f):
    f = f.strip().lower()
    x = f.count("x")
    y = f.count("y")

    if x == 0 and y == 0:
        return False, "У функції немає невідомих змінних! Перевірте функцію!"
    elif proverka_brekets(f) == False:
        return False, "У функції є не закриті дужки! Перевірте функцію!"
    else:
        return True, f 