#!/usr/bin/env python3
"""Логика игры с прогрессией."""
import random

import prompt
from brain_games.scripts.function import welcome_user


def main():
    """Функция, которая реализует логику игры."""
    name = welcome_user()
    index = 0
    print('What number is missing in the progression?')
    while index <= 2:
        index += 1
        right_range = 50
        step_range = 7
        index1, lst = 0, []
        secret_num = random.randrange(0, 10)
        rang = random.randrange(0, right_range)
        step = random.randrange(2, step_range)
        while index1 <= 9:
            index1 += 1
            rang += step
            lst.append(rang)
        r_answ = lst[secret_num]
        lst[secret_num] = '..'
        print('Question: ', *lst)
        answ = int(prompt.string('You answer: '))
        if answ == r_answ:
            print('Correct!')
        else:
            print(f"'{answ}' is wrong answer ;(.Correct answer was '{r_answ}'.")
            print("Let's try again,{0}!".format(name))
            break
    if index == 3:
        print('Congratulations,{0}!'.format(name))
