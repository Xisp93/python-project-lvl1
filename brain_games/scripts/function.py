"""Функции для игр."""
import prompt


def prime(number):
    """Показывает простое ли число.

    Args:
        number: заданное число
    """
    count, flag = 0, ''
    for index in range(1, number):
        if number % index == 0:
            count += 1
        if count >= 2:
            flag = 'no'
            break
        else:
            flag = 'yes'
    return flag


def nod(num_one, num_two):
    """Вычисление НОД.

    Args:
        num_one: первое случайное число
        num_two: второе случайное число
    """
    index, key, lst1, lst2 = 0, 0, [], []
    while index <= num_one:
        index += 1
        if num_one % index == 0:
            lst1.append(index)
    while key <= num_two:
        key += 1
        if num_two % key == 0:
            lst2.append(key)
    res = list(set(lst1) & set(lst2))
    res.sort(reverse=True)
    return res.pop(0)


def welcome_user():
    """Приветствие для игрока."""
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, {0}'.format(name))
    return name


def answer(r_answ, u_answ, name, index):
    """Проверка правильности введенного ответа.

    Args:
        r_answ: правильный ответ
        u_answ: ответ пользователя
        name: имя игрока
        index: флаг цикла
    """
    if r_answ == u_answ:
        print('Correct!')
    else:
        print(f"'{u_answ}' is wrong answer ;(. Correct answer was '{r_answ}'.")
        print("Let's try again, {0}!".format(name))
        return True
    if index == 3:
        print('Congratulations, {0}!'.format(name))
