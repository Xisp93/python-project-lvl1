#!/usr/bin/env python3
"""Логика игры с прогрессией."""
import random


def answer_and_question():
    """Функция, которая реализует логику игры."""
    limit_number = 50
    step_limit = 7
    index, lst = 0, []
    range_number = random.randrange(0, limit_number)
    step = random.randrange(2, step_limit)
    while index <= 9:
        index += 1
        range_number += step
        lst.append(str(range_number))
    secret_number = random.randrange(0, len(lst))
    right_answer = lst[secret_number]
    lst[secret_number] = '..'
    question = ' '.join(lst)
    return right_answer, question


description = 'What number is missing in the progression?'
