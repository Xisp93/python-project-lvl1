#!/usr/bin/env python3
"""Простое ли число."""
import random


def prime(number):
    """Проверяет простое ли число.

    Args:
        number: заданное число
    """
    count, right_answer = 0, ''
    for index in range(1, number):
        if number % index == 0:
            count += 1
        if count >= 2:
            right_answer = 'no'
            break
        else:
            right_answer = 'yes'
    return right_answer


def answer_and_question():
    """Логика игры."""
    rang = 100
    number = random.randrange(1, rang)
    return prime(number), number


description = 'Answer "yes" if given number is prime. Otherwise answer "no".'
