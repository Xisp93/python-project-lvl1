#!/usr/bin/env python3
"""Игра ,в которой находят НОД."""
import random

import prompt
from brain_games.scripts.function import nod, welcome_user


def main():
    """Функция,которая реализует логику игры."""
    name = welcome_user()
    print('Find the greatest common divisor of given numbers.')
    index = 0
    while index < 3:
        rang = 100
        num_one = random.randrange(1, rang)
        num_two = random.randrange(1, rang)
        res = nod(num_one, num_two)
        print('Question: {0} {1}'.format(num_one, num_two))
        answ = prompt.string('You answer: ')
        if int(answ) == int(res):
            print('Correct!')
            index += 1
        else:
            print(f"'{answ}'is wrong answer ;(.Correct answer was '{res}'.")
            print("Let's try again, {0}!".format(name))
            break
    if index == 3:
        print('Congratulations, {0}!'.format(name))
