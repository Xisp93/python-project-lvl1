#!/usr/bin/env python3
"""Простое ли число."""
import random

import prompt
from brain_games.scripts.function import prime, welcome_user


def main():
    """Логика игры."""
    name = welcome_user()
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    flag, index, rang = '', 0, 100
    while index <= 2:
        index += 1
        number = random.randrange(1, rang)
        print('Question: {0}'.format(number))
        answ = prompt.string('You answer: ')
        flag = prime(number)
        if flag == answ:
            print('Correct!')
        else:
            print(f"'{answ}'is wrong answer;(.Correct answer was'{flag}'.")
            print(f"Let's try again, {name}!")
            break
        if index == 3:
            print('Congratulations, {0}!'.format(name))
