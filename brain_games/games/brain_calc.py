#!/usr/bin/env python3
"""Игра с калькулятором."""
import random

import prompt


def brain_calc():
    """Логика игры."""
    operat, res, rang = ['+', '*', '-'], 0, 25
    operat_res = random.choice(operat)
    num_one = random.randrange(0, rang)
    num_two = random.randrange(0, rang)
    print('Question: {0} {1} {2}'.format(num_one, operat_res, num_two))
    if operat_res == '+':
        res = num_one + num_two
    elif operat_res == '-':
        res = num_one - num_two
    else:
        res = num_one * num_two
    answ = prompt.string('Your answer: ')
    return (int(answ), res)
