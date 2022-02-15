#!/usr/bin/env python3
"""Простое ли число."""
import random


RULE = 'Answer "yes" if given number is prime. Otherwise answer "no".'
RIGHT_BORDER = 100


def is_prime(number):
    """Проверяет простое ли число.

    Args:
        number: заданное число
    """
    count, flag = 0, True
    for index in range(1, number + 1):
        if number % index == 0:
            count += 1
        if count >= 2:
            flag = False
    return flag


def generates_answer_and_question():
    """Логика игры."""
    number = random.randrange(1, RIGHT_BORDER)
    correct_answer = ""
    if is_prime(number):
        correct_answer = "yes"
    else:
        correct_answer = "no"
    return correct_answer, number
