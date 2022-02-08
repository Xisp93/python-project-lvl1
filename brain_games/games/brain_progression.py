#!/usr/bin/env python3
"""Логика игры с прогрессией."""
import random

import prompt


def brain_progression():
    """Функция, которая реализует логику игры."""
    right_range = 50
    step_range = 7
    index1, lst = 0, []
    secret_num = random.randrange(0, 10)
    rang = random.randrange(0, right_range)
    step = random.randrange(2, step_range)
    while index1 <= 9:
        index1 += 1
        rang += step
        lst.append(rang)
    r_answ = lst[secret_num]
    lst[secret_num] = '..'
    print('Question:', *lst)
    answ = int(prompt.string('You answer: '))
    return answ, r_answ
