"""Mодуль по созданию героя РПГ."""
from random import randint


# Новый импорт.
# Из модуля start_game_banner, который расположен в папке graphic_arts,
# импортируем функцию run_screensaver().
from graphic_arts.start_game_banner import run_screensaver

def attack(char_name: str, char_class: str) -> str:
    """Вычисляет урон в зависимости от класса."""
    if char_class == 'warrior':
        attack_warrior: float = 5 + randint(3, 5)
        return (f'{char_name} нанёс урон противнику равный '
                f'{attack_warrior}')
    if char_class == 'mage':
        attack_mage: float = 5 + randint(5, 10)
        return (f'{char_name} нанёс урон противнику равный '
                f'{attack_mage}')
    if char_class == 'healer':
        attack_healer: float = 5 + randint(-3, -1)
        return (f'{char_name} нанёс урон противнику равный '
                f'{attack_healer}')


def defence(char_name: str, char_class: str) -> str:
    """Вычисляет показатель защиты в зависимости от класса."""
    if char_class == 'warrior':
        defence_warrior: float = 10 + randint(5, 10)
        return (f'{char_name} блокировал '
                f'{defence_warrior} урона')
    if char_class == 'mage':
        defence_mage: float = 10 + randint(-2, 2)
        return (f'{char_name} блокировал'
                f'{defence_mage} урона')
    if char_class == 'healer':
        defence_healer: float = 10 + randint(2, 5)
        return (f'{char_name} блокировал'
                f'{defence_healer} урона')


def special(char_name: str, char_class: str) -> str:
    """Вычисляет урон от спец. атаки в зависимости от класса."""
    if char_class == 'warrior':
        special_warrior: float = 80 + 25
        return (f'{char_name} применил специальное умение '
                f'«Выносливость {special_warrior}»')
    if char_class == 'mage':
        special_warrior: float = 5 + 40
        return (f'{char_name} применил специальное умение '
                f'«Атака {special_warrior}»')
    if char_class == 'healer':
        special_healer: float = 10 + 30
        return (f'{char_name} применил специальное умение '
                f'«Защита {special_healer}»')


def start_training(char_name: str, char_class: str) -> str:
    """Выбор действий атака, защита, спец. прием и пропустить."""
    if char_class == 'warrior':
        print(f'{char_name}, ты Воитель — отличный боец ближнего боя.')
    if char_class == 'mage':
        print(f'{char_name}, ты Маг — превосходный укротитель стихий.')
    if char_class == 'healer':
        print(f'{char_name}, ты Лекарь — чародей, способный исцелять раны.')
    print('Потренируйся управлять своими навыками.')
    print('Введи одну из команд: '
          'attack — чтобы атаковать противника, '
          'defence — чтобы блокировать атаку противника или '
          'special — чтобы использовать свою суперсилу.')
    print('Если не хочешь тренироваться, введи команду skip.')
    cmd = None
    while cmd != 'skip':
        cmd: str = input('Введи команду: ')
        if cmd == 'attack':
            print(attack(char_name, char_class))
        if cmd == 'defence':
            print(defence(char_name, char_class))
        if cmd == 'special':
            print(special(char_name, char_class))
    return 'Тренировка окончена.'


def choice_char_class() -> str:
    """Проверка выбора класса."""
    approve_choice: str = ''
    char_class: str = ''
    while approve_choice != 'y':
        char_class: str = input('Введи название персонажа, '
                                'за которого хочешь играть: '
                                'Воитель — warrior, '
                                'Маг — mage, '
                                'Лекарь — healer:')
        if char_class == 'warrior':
            print('Воитель — дерзкий воин ближнего боя. '
                  'Сильный, выносливый и отважный.')
        if char_class == 'mage':
            print('Маг — находчивый воин дальнего боя.'
                  'Обладает высоким интеллектом. ')
        if char_class == 'healer':
            print('Лекарь — могущественный заклинатель. '
                  'Черпает силы из природы, веры и духов. ')
        approve_choice: str = input('Нажми (Y), чтобы подтвердить выбор, '
                                    'или любую другую кнопку, чтобы выбрать '
                                    'другого персонажа.').lower()
    return char_class


if __name__ == '__main__':
    """Проверка имени корректности значений"""
    run_screensaver()
    print('Приветствую тебя, искатель приключений! ')
    print('Прежде чем начать игру... ')
    char_name: str = input('...назови себя: ')
    print(f'Здравствуй, {char_name}! '
          'Сейчас твоя выносливость — 80, атака — 5 и защита — 10.')
    print('Ты можешь выбрать один из трёх путей силы: ')
    print('Воитель, Маг, Лекарь')
    char_class: str = choice_char_class()
    print(start_training(char_name, char_class))



# Тестовые данные.
# TEST_DATA: list[tuple[int, str, bool]] = [
#     (44, 'success', True),
#     (16, 'failure', True),
#     (4, 'success', False),
#     (21, 'failure', False),
# ]

# BONUS: float = 1.1
# ANTIBONUS: float = 0.8


# def add_rep(current_rep: float, rep_points: int, buf_effect: bool) -> float:
#     current_rep += rep_points
#     if buf_effect:
#         return current_rep * BONUS
#     return current_rep


# def remove_rep(
#         current_rep: float, rep_points: int, debuf_effect: bool
# ) -> float:
#     current_rep -= rep_points
#     if debuf_effect:
#         return current_rep * ANTIBONUS
#     return current_rep


# def main(duel_res: str):
#     current_rep = 0.0
#     for rep, result, effect in duel_res:
#         if result == 'success':
#             current_rep = add_rep(current_rep, rep, effect)
#         if result == 'failure':
#             current_rep = remove_rep(current_rep, rep, effect)
#     return (f'После {len(duel_res)} поединков, ',
#             'репутация персонажа — {current_rep:.3f} очков.')


# # Тестовый вызов функции main.
# print(main(TEST_DATA))


# from math import sqrt

# message = ('Добро пожаловать в самую лучшую программу для вычисления '
#            'квадратного корня из заданного числа')


# def CalculateSquareRoot(Number):
#     """Вычисляет квадратный корень."""
#     return sqrt(Number)


# def calc(your_number):
#     """Проверка значения на условие >=0."""
#     if your_number <= 0:
#         return 'Веди положительное число больше 0'
#     znach = CalculateSquareRoot(your_number)
#     return (f'Мы вычислили квадратный корень из введённого вами числа.'
#             f' Это будет: {znach}')


# print(message)
# print(calc(25.5))
