import random

from random import *


def game():
    l = 0
    difficult = input('Уровень сложности: сложный - введите "3" '
                      '\n средний - введите "2" '
                      '\n новичок - введите "1"')
    if difficult.strip() == '3':
        l = 3
    elif difficult.strip() == '2':
        l = 5
    elif difficult.strip() == '1':
        l = 7
    with open("reco.txt", mode="r", encoding="utf8") as f:
        reco = int(str(f.read()))
    record = 0
    with open('words.txt', encoding='utf8') as text:  
        words = text.read().splitlines()
        words = [i.lower() for i in words]
    tryin = True
    while tryin != False:
        life = l
        word = str(choice(words))
        words.remove(word)
        guess = ['*'] * len(word)
        end = True
        print(f"Слово загадно: {''.join(guess)}, количество жизней: {life}")
        while end != False:
            letter = input('Введите букву или слово целиком: ').strip()
            if letter.lower() in word and len(letter) == 1 and not letter.upper() in ''.join(guess):
                for i in range(len(word)):
                    if word[i] == letter.lower():
                        guess[i] = letter.upper()
                print(f"Откройте букву: '{letter.upper()}'")
                if ''.join(guess).lower() == word:
                    print(f"Вы угадали слово '{word.upper()}'! Вы выиграли!")
                    record += 1
                    end = False
            elif letter.upper() in ''.join(guess):
                life -= 1
            elif not letter.lower() in word:
                life -= 1
                print(f"Такой буквы нет в слове(. Вы теряете жизнь.")
                if life == 0:
                    print('')
                    print(f"Жизни закончились, вы проиграли(. Загаданное слово было: {word}")
                    print(f"Ваш рекорд: {max(reco, record)}")
                    end = False
            elif letter.lower() == word:
                print(f"Вы угадали слово '{word.upper()}' целиком и вы выиграли ничего!")
                 guess = [x for x in word]
                record += 1
                end = False
            if end == True:
                print(f"{''.join(guess)}, количество жизней: {life}")
        print('')
        if len(words) != 0:
            cont = input("Хотите ли вы сыграть ещё раз? Если да, то нажмите цифру '1', если нет то '0'. ")
            if cont == '1':
                tryin = True
            elif cont == '0':
                print(f"До следующей игры! Ваш рекорд {max(reco, record)}")
                tryin = False
            elif cont != '1' or cont != '0':
                f = False
                while f != True:
                    cont = input("Мы не поняли ваш ответ, введите '1', если хотите сыграть ещё, или '0', если нет.")
                    if cont == '1':
                        tryin = True
                        f = False
                    elif cont == '0':
                        print(f"До следующей игры! Ваш рекорд {record}")
                        tryin = False
                        f = False
        else:
            print(f'Слова в списке закончились. Вы просто гений этой игры! Ваш рекорд: {max(reco, record)}')
            tryin = False
    with open("reco.txt", mode="w", encoding="utf8") as file:
        file.write(str(max(record, reco)))

 game()
