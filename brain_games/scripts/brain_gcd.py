#!/usr/bin/env python3
"""Скрипт для вызова игры."""
from brain_games.engine import run_game
from brain_games.games import gcd


def main():
    """Функция вызова игры."""
    run_game(gcd)


if __name__ == "__main__":
    main()
