"""Игра ,в которой находят НОД."""
import random

import prompt
from brain_games.scripts.function import name


def main():
    """Функция,которая реализует логику игры."""
    index1 = 0
    while index1 < 3:
        index, key, lst1, lst2 = 0, 0, [], []
        rang = 100
        num_one = random.randrange(1, rang)
        num_two = random.randrange(1, rang)
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
        print('Question: {0} {1}'.format(num_one, num_two))
        answ = prompt.string('You answer: ')
        if int(answ) == int(res[0]):
            print('Correct!')
            index1 += 1
        else:
            print(f"'{answ}'is wrong answer ;(.Correct answer was '{res[0]}'.")
            print("Let's try again, {0}!".format(name))
            break
    if index1 == 3:
        print('Congratulations, {0}!'.format(name))


print('Find the greatest common divisor of given numbers.')
