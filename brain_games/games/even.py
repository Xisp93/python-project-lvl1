#!/usr/bin/env python3
"""Игра,которая определяет четность."""
import random

RULE = 'Answer "yes" if the number is even, otherwise answer "no".'
RIGHT_BORDER = 100


def is_even(number):
    """Проверяет четное ли число.
    Args:
        number - число ,которое проверяем.
    """
    if number % 2 == 0:
        return True
    else:
        return False


def generates_answer_and_question():
    """Games."""
    number = random.randint(0, RIGHT_BORDER)
    if is_even(number):
        correct_answer = "yes"
    else:
        correct_answer = "no"
    return correct_answer, number
