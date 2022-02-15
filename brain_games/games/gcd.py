#!/usr/bin/env python3
"""Игра ,в которой находят НОД."""
import random


RULE = "Find the greatest common divisor of given numbers."
RIGHT_BORDER = 100


def calculates_gcd(first_number, second_number):
    """Вычисление НОД.

    Args:
        first_number: первое случайное число
        second_number: второе случайное число
    """
    index, index1, divider_first_num, divider_second_num = 0, 0, [], []
    while index <= first_number:
        index += 1
        if first_number % index == 0:
            divider_first_num.append(index)
    while index1 <= second_number:
        index1 += 1
        if second_number % index1 == 0:
            divider_second_num.append(index1)
    common_divisors = list(set(divider_first_num) & set(divider_second_num))
    common_divisors.sort(reverse=True)
    return str(common_divisors.pop(0))


def generates_answer_and_question():
    """Функция,которая реализует логику игры."""
    first_number = random.randrange(1, RIGHT_BORDER)
    second_number = random.randrange(1, RIGHT_BORDER)
    question = f"{first_number} {second_number}"
    return calculates_gcd(first_number, second_number), question
