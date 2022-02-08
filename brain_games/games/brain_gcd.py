#!/usr/bin/env python3
"""Игра ,в которой находят НОД."""
import random

import prompt
from brain_games.scripts.function import nod


def brain_gcd():
    """Функция,которая реализует логику игры."""
    rang = 100
    num_one = random.randrange(1, rang)
    num_two = random.randrange(1, rang)
    res = nod(num_one, num_two)
    print('Question: {0} {1}'.format(num_one, num_two))
    answ = prompt.string('You answer: ')
    return int(answ), res
