#!/usr/bin/env python3
"""Игра,которая определяет четность."""
import random

RULE = 'Answer "yes" if the number is even, otherwise answer "no".'
RIGHT_BORDER = 100
REFERENCE_POINT = 1


def is_even(number):
    """Проверяет четное ли число.
    Args:
        number - число ,которое проверяем.
    """
    return True if number % 2 == 0 else False


def generates_answer_and_question():
    """Games."""
    number = random.randint(REFERENCE_POINT, RIGHT_BORDER)
    if is_even(number):
        return "yes", number
    else:
        return "no", number
