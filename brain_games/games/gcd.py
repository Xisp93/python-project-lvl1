#!/usr/bin/env python3
"""Игра ,в которой находят НОД."""
import random


def nod(num_one, num_two):
    """Вычисление НОД.

    Args:
        num_one: первое случайное число
        num_two: второе случайное число
    """
    index, index1, lst1, lst2 = 0, 0, [], []
    while index <= num_one:
        index += 1
        if num_one % index == 0:
            lst1.append(index)
    while index1 <= num_two:
        index1 += 1
        if num_two % index1 == 0:
            lst2.append(index1)
    res = list(set(lst1) & set(lst2))
    res.sort(reverse=True)
    return res.pop(0)


def answer_and_question():
    """Функция,которая реализует логику игры."""
    rang = 100
    number_one = random.randrange(1, rang)
    number_two = random.randrange(1, rang)
    question = '{0} {1}'.format(number_one, number_two)
    return nod(number_one, number_two), question


description = 'Find the greatest common divisor of given numbers.'
