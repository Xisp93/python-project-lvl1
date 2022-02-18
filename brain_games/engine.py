#!/usr/bin/env python3
"""Движок для игр."""
import prompt

NUMBER_OF_ROUNDS = 3


def run_game(game):
    """Движок игры.

    Args:
        game: модуль игры
    """
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}")
    index = 0
    print(game.RULE)
    while index < NUMBER_OF_ROUNDS:
        index += 1
        right_answer, question = game.generates_answer_and_question()
        print(f"Question: {question}")
        answer = prompt.string("You answer: ")
        if answer == right_answer:
            print("Correct!")
        else:
            # noinspection TaskProblemsInspection
            print(
                f"'{answer}' is wrong answer ;(. Correct answer was\
 '{right_answer}'."
            )
            print(f"Let's try again, {name}!")
            break
        if index == NUMBER_OF_ROUNDS:
            print(f"Congratulations, {name}!")
