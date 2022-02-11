#!/usr/bin/env python3
"""Игра с калькулятором."""
import random


def answer_and_question():
    """Логика игры."""
    operators, correct_answer, right_border = ['+', '*', '-'], 0, 25
    random_operators = random.choice(operators)
    first_num = random.randrange(0, right_border)
    second_num = random.randrange(0, right_border)
    question = '{0} {1} {2}'.format(first_num, random_operators, second_num)
    correct_answer = eval(question)
    return correct_answer, question


DESCRIPTION = 'What is the result of the expression?'
