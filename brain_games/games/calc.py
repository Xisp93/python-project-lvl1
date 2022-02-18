#!/usr/bin/env python3
"""Игра с калькулятором."""
import random

RULE = "What is the result of the expression?"
OPERATORS = ["+", "*", "-"]
RIGHT_BORDER = 25
REFERENCE_POINT = 0


def generates_answer_and_question():
    """Логика игры."""
    random_operators = random.choice(OPERATORS)
    first_number = random.randint(REFERENCE_POINT, RIGHT_BORDER)
    second_number = random.randint(REFERENCE_POINT, RIGHT_BORDER)
    question = f"{first_number} {random_operators} {second_number}"
    correct_answer = eval(question)
    return str(correct_answer), question
