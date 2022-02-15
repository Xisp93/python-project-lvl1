#!/usr/bin/env python3
"""Игра,которая определяет четность."""
import random


RULE = 'Answer "yes" if the number is even, otherwise answer "no".'
RIGHT_BORDER = 100


def is_even(number):
    """Проверяет четное ли число."""
    return True if number % 2 == 0 else False


def generates_answer_and_question():
    """Games."""
    correct_answer = ""
    number = random.randint(0, RIGHT_BORDER)
    if is_even(number):
        correct_answer = "yes"
    else:
        correct_answer = "no"
    return correct_answer, number
