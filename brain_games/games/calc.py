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
    right_answer = eval(question)
    return right_answer, question


DESCRIPTION = 'What is the result of the expression?'
