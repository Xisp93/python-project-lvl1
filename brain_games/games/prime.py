#!/usr/bin/env python3
"""Простое ли число."""
import random

RULE = 'Answer "yes" if given number is prime. Otherwise answer "no".'
RIGHT_BORDER = 100
REFERENCE_POINT = 1


def is_prime(number):
    """Проверяет простое ли число.

    Args:
        number: заданное число
    """
    number_of_divisors = 0
    for index in range(REFERENCE_POINT, number + 1):
        if number % index == 0:
            number_of_divisors += 1
            if number_of_divisors == 3:
                return False
    return True


def generates_answer_and_question():
    """Логика игры."""
    number = random.randint(REFERENCE_POINT, RIGHT_BORDER)
    if is_prime(number):
        return "yes", number
    else:
        return "no", number
