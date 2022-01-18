"""Функции для игр."""


def nod(num_one, num_two):
    """Рассчитывает НОД для игры gcd.

    Args:
        num_one: первое число
        num_two: 2 число
    """
    index, key, lst1, lst2 = 1, 1, [], []
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
    return res[0]


print('Welcome to the Brain Games!')
name = input('Make I have your name?')
print('Hello, {0}!'.format(name))
