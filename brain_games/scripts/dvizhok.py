#!/usr/bin/env python3
"""Движок для игр."""
from brain_games.games.brain_calc import brain_calc
from brain_games.games.brain_even import brain_even
from brain_games.games.brain_gcd import brain_gcd
from brain_games.games.brain_prime import brain_prime
from brain_games.games.brain_progression import brain_progression
from brain_games.scripts.function import answer, welcome_user


def main_calc():
    """Игра в калькулятор."""
    name = welcome_user()
    index = 0
    print('What is the result of the expression?')
    while index <= 2:
        answ, res = brain_calc()
        index += 1
        if answer(answ, res, name, index):
            break


def main_prime():
    """Игра для определения простого числа."""
    name = welcome_user()
    index = 0
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    while index <= 2:
        answ, res = brain_prime()
        if answer(answ, res, name, index):
            break
        index += 1
    if index == 3:
        print('Congratulations, {0}!'.format(name))


def main_even():
    """Игра определяющая четность."""
    name = welcome_user()
    index = 0
    print('Answer "yes" if the number is even, otherwise answer "no".')
    while index <= 2:
        answ, res = brain_even()
        if answer(answ, res, name, index):
            break
        index += 1


def main_gcd():
    """Игра на НОД."""
    name = welcome_user()
    index = 0
    print('Find the greatest common divisor of given numbers.')
    while index <= 2:
        answ, res = brain_gcd()
        if answer(answ, res, name, index):
            break
        index += 1


def main_progression():
    """Игра в прогрессию."""
    name = welcome_user()
    index = 0
    print('What number is missing in the progression?')
    while index <= 2:
        answ, res = brain_progression()
        if answer(answ, res, name, index):
            break
        index += 1
