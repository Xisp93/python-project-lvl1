#!/usr/bin/env python3
"""Движок для игр."""
import prompt


def welcome_user():
    """Приветствие для игрока."""
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, {0}'.format(name))
    return name


def answer(r_answ, u_answ, name, index):
    """Проверка правильности введенного ответа.

    Args:
        r_answ: правильный ответ
        u_answ: ответ пользователя
        name: имя игрока
        index: флаг цикла
    """
    if r_answ == u_answ:
        print('Correct!')
    else:
        print(f"'{u_answ}' is wrong answer ;(. Correct answer was '{r_answ}'.")
        print("Let's try again, {0}!".format(name))
        return True
    if index == 3:
        print('Congratulations, {0}!'.format(name))


def run_games(games):
    """Движок игры.

    Args:
        games: модуль игры
    """
    name = welcome_user()
    index = 0
    print(games.description)
    while index <= 2:
        index += 1
        res, question = games.answer_and_question()
        print('Question: {0}'.format(question))
        answ = prompt.string('You answer: ')
        if answer(str(res), answ, name, index):
            break
