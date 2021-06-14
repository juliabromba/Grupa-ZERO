# -*- coding: utf-8 -*-
"""
Created on Mon Jun 14 11:18:51 2021

@author: Julia
"""
#PLIK Z DZIAŁAJĄCYM WARUNKIEM NIEZGODNYM - HAPPY + 2 ANGRY <3
from psychopy import visual, core, event
import random
import csv
import os, sys

win = visual.Window(units="pix", color="gray", fullscr=False)

#TWORZENIE LISTY Z PLIKÓW W FOLDERACH 'HAPPY' I 'ANGRY'. ŻEBY PÓŹNIEJ DZIAŁAŁO,
# PLIKI MUSZĄ BYĆ TEŻ LUŹNO WRZUCONE DO FOLDERU, W KTÓRYM JEST TEN KOD. DO OGARNIĘCIA/ZROZUMIENIA.
happypath = "C:/Users/Julia/PycharmProjects/pythonProject/happy"
happy = list(os.listdir(happypath))
angrypath = "C:/Users/Julia/PycharmProjects/pythonProject/angry"
angry = list(os.listdir(angrypath))
#print(happy, angry)

from pathlib import Path

#WARUNEK NIEZGODNY HAPPY
n = 4 # liczba losowań
m = 12 #liczba zdjęć w folderze
p = 12 # liczba zdjęć w folderze
while n>0:
    #losowanie randomowej liczby z dwunastu, później można to wsadzić w 'pop'
    s = random.randrange(m)
    r = random.randrange(p)
    # wyjmowanie randomowej foty (będącej w folderach na miejscach s i r) z listy plików -
    # - usuwa ją z listy i zaraz nam ją wyswietli :>
    happy_pop = happy.pop(s)
    angry_pop = angry.pop(r)
    #tworzenie sciezki dostępu do pliku z nazwy pliku - potrzebne w 'visual.ImageStim'
    #tutaj pojawia się ten problem, że sciezka tworzy się do folderu, w którym jest plik z kodem, nawet jesli pliku,
    #od którego robimy scieżkę nie ma w tym folderze. Ale jak się wrzuci te pliki też do folderu z kodem, to jest OK xD
    happy_sciezka = os.path.abspath(happy_pop)
    angry_sciezka = os.path.abspath(angry_pop)
    #te printy na później do usunięcia, ale teraz wolę widzieć, co się dzieje
    print(happy_sciezka)
    print(angry_sciezka)
    print('HAPPY NOWE =', happy, 'ANGRY NOWE=', angry)
    
    happy_photo = visual.ImageStim(win,image= happy_sciezka, pos=(0.0, 0.0), size=[200, 200], colorSpace = 'rgb')
    angry_photo_a = visual.ImageStim(win,image= angry_sciezka, pos=(-250.0, 0.0), size=[200, 200], colorSpace = 'rgb')
    angry_photo_b = visual.ImageStim(win,image= angry_sciezka, pos=(250.0, 0.0), size=[200, 200], colorSpace = 'rgb')
    happy_photo.draw()
    angry_photo_a.draw()
    angry_photo_b.draw()
    win.flip()
    core.wait(2)
    n-=1
    m-=1


win.flip()
win.close()