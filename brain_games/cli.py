"""Скрипт для имени пользоватедя."""

import prompt


def welcome_user():
    """Запрашивает имя пользователя,и говорит привет ."""
    name = prompt.string('Make I have your name?')
    print('Hello,{0}!'.format(name))
