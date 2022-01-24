#!/usr/bin/env python3
"""Игра с калькулятором."""
import random

import prompt
from brain_games.scripts.function import name


def main():
    """My game."""
    print('What is the result of the expression?')
    operat, res, index, rang = ['+', '*', '-'], 0, 0, 25
    while index <= 2:
        operat_res = random.choice(operat)
        num_one = random.randrange(0, rang)
        num_two = random.randrange(0, rang)
        print('Question:{0} {1} {2}'.format(num_one, operat_res, num_two))
        if operat_res == '+':
            res = num_one + num_two
        elif operat_res == '-':
            res = num_one - num_two
        else:
            res = num_one * num_two
        answer = prompt.string('Your answer: ')
        if int(answer) == res:
            print('Correct!')
            index += 1
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{res}'.")
            print("Let's try again, {0}!".format(name))
            break
    if index == 3:
        print('Congratulations, {0}!'.format(name))
