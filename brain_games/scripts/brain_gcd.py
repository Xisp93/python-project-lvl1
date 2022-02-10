#!/usr/bin/env python3
"""Скрипт для вызова игры."""
from brain_games.engine import run_games
from brain_games.games import gcd


def main():
    """Функция вызова игры."""
    run_games(gcd, gcd.description)


if __name__ == '__main__':
    main()
