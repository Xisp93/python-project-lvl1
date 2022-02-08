#!/usr/bin/env python3
"""Игра,которая определяет четность."""
import random

import prompt


def brain_even():
    """Games."""
    flag = ''
    num = random.randrange(0, 100)
    print('Question: {0}'.format(num))
    answ = prompt.string('Your answer: ')
    if (num % 2 == 0):
        flag = 'yes'
    else:
        flag = 'no'
    return answ, flag
