#!/usr/bin/env python3
"""Простое ли число."""
import random


def prime(number):
    """Проверяет простое ли число.

    Args:
        number: заданное число
    """
    count, correct_answer = 0, ''
    for index in range(1, number):
        if number % index == 0:
            count += 1
        if count >= 2:
            correct_answer = 'no'
            break
        else:
            correct_answer = 'yes'
    return correct_answer


def answer_and_question():
    """Логика игры."""
    right_border = 100
    number = random.randrange(1, right_border)
    return prime(number), number


DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'
