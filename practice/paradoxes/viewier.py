from MontyHall import *
from Birthday_paradox import *
def show():
    mont = (input("Парадокс Монти Холла: введите кол-во экспериментов: "))
    if str(mont).strip() == '':
        print(f"Побед, % побед с первого хода,  % побед со 2-го хода соответственно: {monty(10000)}")
    else:
        print(f"Побед, % побед с первого хода,  % побед со 2-го хода соответственно: {monty(int(mont))}")
    c = (input("Парадокс дней рождения: введите количество людей в группе: "))
    ce = (input("Введите количество экспериментов: "))
    if str(c) == '':
        print(f"Парадокс дней рождения в группе из 23 человек среди 10000 экспериментов: {birthday(10000, 23)}")
        print(f"Парадокс дней рождения в группе из 60 человек среди 10000 экспериментов: {birthday(10000, 60)}")
    else:
        print(f"Парадокс дней рождения в группе из {c} человек среди {ce} экспериментов: {birthday(int(ce), int(c))}")


if __name__ == "__main__":
    from MontyHall import *
    from Birthday_paradox import *

    show()
else:
    from MontyHall import *
    from Birthday_paradox import *