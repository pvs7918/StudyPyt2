# Доработайте прошлую задачу добавив декоратор wraps в каждый из декораторов.

from functools import wraps
import json
import os
import random
from typing import Callable


def checker(func) -> Callable:
    @wraps(func)
    def wrapper(guess: int, attempts: int):
        guess = guess if 1 < guess < 100 else random.randint(1, 100)
        attempts = attempts if 1 < attempts < 10 else random.randint(1, 10)
        return func(guess, attempts)

    return wrapper


def writer(file_name):
    def inner(func):
        @wraps(func)
        def wrapper(number, tries):
            my_dict = {str(func(number, tries)): (number, tries)}
            if os.path.exists(file_name):
                with open(file_name, 'a', encoding="utf-8") as f:
                    json.dump(my_dict, f, ensure_ascii=False)
            else:
                with open(file_name, 'w', encoding="utf-8") as f:
                    json.dump(my_dict, f, ensure_ascii=False)
            return func(number, tries)

        return wrapper

    return inner


def counter(number):
    def dec(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            results = []
            for i in range(number):
                print(f"Игра началась! {i + 1}")
                results.append(func(*args, **kwargs))
            return tuple(results)

        return wrapper

    return dec


@writer('guess_game.json')
@counter(3)
@checker
def game_guess(num_sc, attempts):
    """Игра - угадайка"""
    result_attempts = 1
    while attempts:
        print(f'left {attempts} attempts.', end=' ')
        attempts -= 1
        num = int(input('Input a number: '))
        if num == num_sc:
            print(f'Number found: {num}')
            return result_attempts
        else:
            advice = ['lesser', 'greater']
            print(f'Your number is {advice[num > num_sc]} then right')
            result_attempts += 1
    else:
        print(f'You loose. Right number is {num_sc}')

    return result_attempts


help(game_guess)