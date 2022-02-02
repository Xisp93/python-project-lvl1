#!/usr/bin/env python3
"""Игра ,в которой находят НОД."""
import random

import prompt
from brain_games.scripts.dvizhok import NAME, answer, nod


def main():
    """Функция,которая реализует логику игры."""
    print('Find the greatest common divisor of given numbers.')
    index = 0
    while index <= 2:
        index += 1
        rang = 100
        num_one = random.randrange(1, rang)
        num_two = random.randrange(1, rang)
        res = nod(num_one, num_two)
        print('Question: {0} {1}'.format(num_one, num_two))
        answ = prompt.string('You answer: ')
        if answer(int(answ), int(res)):
            break
        if index == 3:
            print('Congratulations, {0}!'.format(NAME))
