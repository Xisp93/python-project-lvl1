#!/usr/bin/env python3
"""Первое что видит пользователь."""
from brain_games.cli import welcome_user


def main():
    """С этого начинает работать скрипт."""
    #print('Welcome to the Brain Games!')
    name = welcome_user()
    #print('Hello, {0}!'.format(name))


if __name__ == '__main__':
    main()
