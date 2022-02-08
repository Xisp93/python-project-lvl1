#!/usr/bin/env python3
"""Простое ли число."""
import random

import prompt
from brain_games.scripts.function import prime


def brain_prime():
    """Логика игры."""
    flag, rang = '', 100
    number = random.randrange(1, rang)
    print('Question: {0}'.format(number))
    answ = prompt.string('You answer: ')
    flag = prime(number)
    return answ, flag
