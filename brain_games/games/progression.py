#!/usr/bin/env python3
"""Логика игры с прогрессией."""
import random

RULE = "What number is missing in the progression?"
RANGE_BORDER = 50
STEP_LIMIT = 7
LENGTH_PROGRESSION = 10
REFERENCE_POINT = 0


def calculate_next_member(first_progression_member, progression_step):
    """Расчитывает следующий после пеового член прогрессии.

    Args:
        first_progression_member: первый член арифметической прогрессии.
        progression_step: шаг арифметической прогрессии.
    """
    return first_progression_member + progression_step


def returns_arithmetic_progression(progression_term, step):
    """Получение строкового представления прогрессии."""
    result, index = [], 0
    while index < LENGTH_PROGRESSION:
        result.append(str(progression_term))
        progression_term = calculate_next_member(progression_term, step)
        index += 1
    return result


def generates_answer_and_question():
    """Функция, которая реализует логику игры."""
    first_progression_member = random.randint(REFERENCE_POINT, RANGE_BORDER)
    progression_step = random.randint(REFERENCE_POINT, STEP_LIMIT)
    progression = returns_arithmetic_progression(
        first_progression_member, progression_step
    )
    secret_number = random.randint(REFERENCE_POINT, LENGTH_PROGRESSION - 1)
    correct_answer = progression[secret_number]
    progression[secret_number] = ".."
    question = " ".join(progression)
    return correct_answer, question
