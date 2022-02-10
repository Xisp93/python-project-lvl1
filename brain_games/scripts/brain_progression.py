#!/usr/bin/env python3
"""Скрипт для вызова игры."""
from brain_games.engine import run_games
from brain_games.games import progression


def main():
    """Функция вызова игры."""
    run_games(progression, progression.description)


if __name__ == '__main__':
    main()
