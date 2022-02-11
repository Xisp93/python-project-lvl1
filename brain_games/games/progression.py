#!/usr/bin/env python3
"""Логика игры с прогрессией."""
import random


def answer_and_question():
    """Функция, которая реализует логику игры."""
    number_range_border = 50
    step_border = 7
    index, lst = 0, []
    number_range = random.randrange(0, number_range_border)
    step_range = random.randrange(2, step_border)
    while index <= 9:
        index += 1
        number_range += step_range
        lst.append(str(number_range))
    secret_number = random.randrange(0, len(lst))
    correct_answer = lst[secret_number]
    lst[secret_number] = '..'
    question = ' '.join(lst)
    return correct_answer, question


DESCRIPTION = 'What number is missing in the progression?'
