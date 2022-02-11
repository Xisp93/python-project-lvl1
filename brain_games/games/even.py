#!/usr/bin/env python3
"""Игра,которая определяет четность."""
import random


def answer_and_question():
    """Games."""
    correct_answer = ''
    right_border = 100
    number = random.randrange(0, right_border)
    if (number % 2 == 0):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return correct_answer, number


DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'
