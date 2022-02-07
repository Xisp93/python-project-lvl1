"""Движок для игр."""


def welcome_user():
    """Приветствие игрока."""
    print('Welcome to the Brain Games!')
    name = input('Make I have your name? ')
    print('Hello, {0}!'.format(name))
    return name


def answer(r_answ, u_answ):
    """Проверка правильности введенного ответа.

    Args:
        r_answ: правильный ответ
        u_answ: ответ пользователя
    """
    if r_answ == u_answ:
        print('Correct!')
    else:
        print(f"'{u_answ}'is wrong answer;(.Correct answer was'{r_answ}'.")
        print(f"Let's try again, {NAME}!")
        return True


NAME = welcome_user()
