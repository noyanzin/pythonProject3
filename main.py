def division(val1: float, val2: float) -> float:
    return val1 / val2 if val2 != 0 else print("Ошибка. Деление на 0")


def set_person(firstname, secondname, year, sity, email, phone):
    print(
        f"имя: {firstname}, фамилия: {secondname}, год рождения: {year}, город проживания: {sity}, email: {email}, телефон: {phone}.")


def my_func(a: float, b: float, c: float) -> float:
    l: list[float] = [a, b, c]
    l.sort()
    return l[1] + l[2]


def my_func1(x: float, y: int) -> float:
    if y < 0:
        return 1 / (x ** abs(y))
    else:
        return x ** y


def my_func2(x: float, y: int) -> float:
    if y < 0:
        first = x
        for i in range(abs(y)):
            # x = x * first
            return x
    else:
        print(" Второе число должно быть больше 0.")


def list_numbers():
    result = []
    try:
        while True:
            l = input("Введите числа через пробел: ").split(' ')

            for x in l:
                result.append(float(x))
            print(f'l = {l}, result = {result}, cумма = {sum(result)}')
    except:
        print(f'КОНЕЦ')
    finally:
        print(f'l = {l}, result = {result}, cумма = {sum(result)}')


def int_func(a: str):
    b = list(a)
    b[0] = a[0].upper()
    return "".join(b)


def word_func(s: str):
    l = s.split(" ")
    l_out = []
    for c in l:
        l_out.append(int_func(c))
    return " ".join(l_out)


print(division(float(input("Введите число1:")), float(input("Введите число 2:"))))
print(set_person("Марк", "Ноянзин", 1974, "Петропавловск-Камчатский", "noyanzin@inbox.ru", "79247911946"))
print(my_func(2, 20, 8))
list_numbers()
print(int_func("qwerty"))
print(word_func("fhhfg reghughtrguht ehgue rehgurehg reughtg reghrugre"))

