"""Первое что видит пользователь."""
from brain_games import cli


def main():
    """С этого начинает работать скрипт."""
    print('Welcome to the Brain Games!')
    print('Hello, {0}!'.format(cli.welcome_user()))


if __name__ == '__main__':
    main()
