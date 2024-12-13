from random import *
import os
clear = lambda: os.system('cls')
words = [i[:-1] for i in open("BAS.txt", encoding="utf8").readlines()]
start = input("Любой символ начать, stop - Выйти: ")

while True:
    mom = []
    if start == 'stop':
        break
    wi = randint(0, 1000)
    word = words[wi-1].split(f'{wi} ')[1].split(' - ')[0]
    words_wtf = words[wi-1].split(f'{wi} ')[1].split(' - ')[1]
    w = []
    for i in word:
        w.append("_")
    print(''.join(w), words_wtf, f'({len(w)})')
    while w.count('_') != 0:
        char = input('Буква или слово (stop - Выйти): ')
        cu = char.upper()
        cd = char.lower()
        wd = word.lower()
        if char == "stop":
            start = 'stop'
            break
        elif cd == wd:
            c = 0
            for i in word:
                w[c] = i
                c+=1
        elif cu in word or cd in word:
            c = 0
            for i in word:
                if cu == i or cd == i:
                    w[c] = cd
                c+=1
            clear()
            print(f"откройте букву {cu}")
        else:
            if len(cu) == 1:
                clear()
                mom.append(cu)
                if len(set(mom)) <= 7:
                    print("такого символа нет", set(mom), f'осталось попыток: {8 - len(set(mom))}')
                else:
                    print("Вы проиграли!")
                    break
                    start = 'stop'
            else:
                clear()
                print("неверный ввод")
        if w.count('_') == 0:
            print("Победа!!")
        print(''.join(w), words_wtf)