#!/usr/bin/env python3
"""Игра с калькулятором."""
import random


def answer_and_question():
    """Логика игры."""
    operat, right_answer, rang = ['+', '*', '-'], 0, 25
    operat_res = random.choice(operat)
    number_one = random.randrange(0, rang)
    number_two = random.randrange(0, rang)
    question = '{0} {1} {2}'.format(number_one, operat_res, number_two)
    if operat_res == '+':
        right_answer = number_one + number_two
    elif operat_res == '-':
        right_answer = number_one - number_two
    else:
        right_answer = number_one * number_two
    return right_answer, question


description = 'What is the result of the expression?'
