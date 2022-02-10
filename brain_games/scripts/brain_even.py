#!/usr/bin/env python3
"""Скрипт для вызова игры."""
from brain_games.engine import run_games
from brain_games.games import even


def main():
    """Функция вызова игры."""
    run_games(even)


if __name__ == '__main__':
    main()
