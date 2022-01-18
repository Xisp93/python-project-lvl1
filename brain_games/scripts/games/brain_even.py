"""Игра,которая определяет четность."""
import random

import prompt
from brain_games.scripts.function import name


def main():
    """Games."""
    flag, index = '', 0
    while index <= 2:
        num = random.randrange(0, 100)
        print('Question: {0}'.format(num))
        answ = prompt.string('Your answer: ')
        if (num % 2 == 0 and answ == 'yes'):
            print('Correct!')
            index += 1
        elif (num % 2 != 0 and answ == 'no'):
            print('Correct!')
            index += 1
        else:
            break
    if index == 3:
        print('Congratulations, {0}!'.format(name))
    else:
        if num % 2 == 0:
            flag = 'yes'
        else:
            flag = 'no'
        print(f"'{answ}'is wrong answer;(.Correct answer was'{flag}'.")
        print(f"Let's try again, {name}!")
