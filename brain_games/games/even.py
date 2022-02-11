#!/usr/bin/env python3
"""Игра,которая определяет четность."""
import random


def answer_and_question():
    """Games."""
    right_answer = ''
    num = random.randrange(0, 100)
    if (num % 2 == 0):
        right_answer = 'yes'
    else:
        right_answer = 'no'
    return right_answer, num


DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'
