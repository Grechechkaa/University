import random
from random import *
def monty(n):
    count_second_choice_win = 0
    count_first_choice_win = 0
    win = 0
    for i in range(n):
        priz = randint(1, 3)
        computer = randint(1, 3)
        not_here = [int(x) for x in range(1, 4) if x != priz and x != computer]
        lose_door = choice(not_here)
        second_choice_computer = choice(['да', 'нет'])
        if second_choice_computer == 'да':
            if 6 - computer - lose_door == priz:
                count_second_choice_win += 1
                win += 1
        else:
            if computer == priz:
                count_first_choice_win += 1
                win += 1
    return win, (int((count_first_choice_win / win) * 100)), (int((count_second_choice_win / win) * 100))

