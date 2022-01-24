#!/usr/bin/env python3
"""Простое ли число."""
import random

import prompt
from brain_games.scripts.function import name


def main():
    """Логика игры."""
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    flag, index, rang = '', 0, 100
    while index <= 2:
        index += 1
        lst = []
        num = random.randrange(0, rang)
        print('Question: {0}'.format(num))
        answ = prompt.string('You answer: ')
        for chek in range(1, num + 1):
            if num % chek == 0:
                lst.append(chek)
            if len(lst) >= 3:
                flag = 'no'
            else:
                flag = 'yes'
        if flag == answ:
            print('Correct!')
        else:
            print(f"'{answ}'is wrong answer;(.Correct answer was'{flag}'.")
            print(f"Let's try again, {name}!")
            break
    if index == 3:
        print('Congratulations, {0}!'.format(name))
