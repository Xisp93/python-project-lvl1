#!/usr/bin/env python3
"""Логика игры с прогрессией."""
import random


RULE = "What number is missing in the progression?"
NUMBER_RANGE_BORDER = 50
STEP_BORDER = 7
LENGTH_PROGRESSION = 10


def generates_answer_and_question():
    """Функция, которая реализует логику игры."""
    first_progression_member = random.randint(0, NUMBER_RANGE_BORDER)
    progression_step = random.randint(2, STEP_BORDER)
    progression = returns_arithmetic_progression(
        first_progression_member, progression_step
    )
    secret_number = random.randint(0, len(progression))
    correct_answer = progression[secret_number]
    progression[secret_number] = ".."
    question = " ".join(progression)
    return correct_answer, question


def returns_arithmetic_progression(progression_member, progression_step):
    """Получение строкового представления прогрессии."""
    result, index = [], 0
    while index < 10:
        result.append(str(progression_member))
        progression_member = calculates_next_progression_member(
            progression_member, progression_step
        )
        index += 1
    return result


def calculates_next_progression_member(first_progression_member, progression_step):
    """Расчитывает следующий после пеового член прогрессии."""
    return first_progression_member + progression_step
