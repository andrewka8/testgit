from random import *
import os
clear = lambda: os.system('cls')
class word():
    def __init__(self):
        self.words = [i[:-1] for i in open("BAS.txt", encoding="utf8").readlines()]
        self.wi = randint(0, 1000)
        self.word = self.words[self.wi - 1].split(f'{self.wi} ')[1].split(' - ')[0]
        self.words_wtf = self.words[self.wi - 1].split(f'{self.wi} ')[1].split(' - ')[1]

    def IO(self, out):
        clear()
        print(out)
        if self.fallcount == 7:
            print("Вы проиграли", self.word)
            return
        if self.ws.count("_") == 0:
            print('Вы победили', ''.join(self.ws))
            return
        self.sym = input(f'Введите букву (stop - выйти, Нет букв{set(self.sfn)}, Попыток {7 - self.fallcount}):')
        sl = self.sym.lower()
        wl = self.word.lower()
        if sl == wl:
            print('Вы победили', self.word)
            return
        if self.sym == 'stop':
            return
        self.check_symbol()

    def check_symbol(self):
        print(self.sym)
        if len(self.sym) != 1:
            self.IO(f"{''.join(self.ws), self.words_wtf, 'Неправильный символ', self.sym}")
        else:
            try:
                t = int(self.sym)
                self.IO(f"{''.join(self.ws), self.words_wtf, 'Неправильный символ', self.sym}")
            except:
                sl = self.sym.lower()
                su = self.sym.upper()
                if su in self.word or sl in self.word:
                    c = -1
                    for i in self.word:
                        c += 1
                        if i == sl or i == su:
                            self.ws[c] = i
                    self.IO(f"{''.join(self.ws), self.words_wtf, 'ОТКРОЙТЕ БУКВУ!!', su}")

                else:
                    self.sfn.append(su)
                    self.fallcount = len(set(self.sfn))
                    self.IO(f"{''.join(self.ws), self.words_wtf, 'Нет такой буквы', self.sym}")

    def start(self):
        self.ws = []
        self.fallcount = 0
        self.sfn = []
        for i in self.word:
            self.ws.append("_")
        self.IO(f"{''.join(self.ws), self.words_wtf}")

game = word()
game.start()
while True:
    a = input("Продолжить? y/n:")
    if a == "y":
        game = word()
        game.start()
    elif a == 'n':
        break
    else:
        continue
