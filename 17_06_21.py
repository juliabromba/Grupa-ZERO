from psychopy import visual, core, event
import random
import csv
import os, sys
from random import shuffle
from pathlib import Path
import codecs

# okno glowne
win = visual.Window(units="pix", color="white", fullscr=True)

# sciezki do plikow w dwoch folderach happy i angry na dysku
happypath = "C:/Users/Laptop/Desktop/Informatyka projekt/happy"
happy_pictures = list(os.listdir(happypath))
angrypath = "C:/Users/Laptop/Desktop/Informatyka projekt/angry"
angry_pictures = list(os.listdir(angrypath))


def happy_zgodny(happy_pictures):  # warunek happy zgodny, w srodku happy, po bokach happy
    shuffle(happy_pictures)
    center = happy_pictures[0]
    left = happy_pictures[1]
    right = happy_pictures[1]
    happy1 = [left, center, right]
    return happy1


def angry_zgodny(angry_pictures):  # warunek angry zgodny, w srodku angry, po bokach angry
    shuffle(angry_pictures)
    center = angry_pictures[0]
    left = angry_pictures[1]
    right = angry_pictures[1]
    angry1 = [left, center, right]
    return angry1


def angry_niezgodny(angry_pictures, happy_pictures):  # warunek angry niezgodny, w srodku angry, po bokach happy
    shuffle(angry_pictures)
    shuffle(happy_pictures)
    center = angry_pictures[0]
    left = happy_pictures[1]
    right = happy_pictures[1]
    angry2 = [left, center, right]
    return angry2


def happy_niezgodny(angry_pictures, happy_pictures):  # warunek happy niezgodny, w srodku happy, po bokach angry
    shuffle(angry_pictures)
    shuffle(happy_pictures)
    center = happy_pictures[0]
    left = angry_pictures[1]
    right = angry_pictures[1]
    happy2 = [left, center, right]
    return happy2


def createBlock():  # tworzenie listy z osmioma warunkami, kazdy z 4 podwojnie na koncu liste mieszamy
    block = [happy_zgodny(happy_pictures),
             happy_zgodny(happy_pictures),
             angry_zgodny(angry_pictures),
             angry_zgodny(angry_pictures),
             angry_niezgodny(angry_pictures, happy_pictures),
             angry_niezgodny(angry_pictures, happy_pictures),
             happy_niezgodny(angry_pictures, happy_pictures),
             happy_niezgodny(angry_pictures, happy_pictures)]
    shuffle(block)
    return block


def displaySet(picturesSet):  # wyswietlanie blokow
    trial1_center = os.path.abspath(picturesSet[1])
    trial1_left = os.path.abspath(picturesSet[0])
    trial1_right = os.path.abspath(picturesSet[2])

    srodek = visual.ImageStim(win, image=trial1_center, pos=(0.0, 0.0), size=[300, 377], colorSpace='rgb')
    lewy = visual.ImageStim(win, image=trial1_left, pos=(-310.0, 0.0), size=[300, 377], colorSpace='rgb')
    prawy = visual.ImageStim(win, image=trial1_right, pos=(310.0, 0.0), size=[300, 377], colorSpace='rgb')
    srodek.draw()
    prawy.draw()
    lewy.draw()
    win.flip()
    core.wait(1)


def breake():
    img = visual.TextStim(win, text='Przerwa, aby przejść do następnego bloku naciśnij spacje', pos=(0.0, 0.0),
                          color="black")
    img.draw()
    win.flip()
    clicked = event.waitKeys(keyList=['space'])
    if clicked == ["space"]:
        core.wait(0)
    img.draw()
    win.flip()


def end():
    img = visual.TextStim(win, text='Koniec, dziękujemy za udział w badaniu', pos=(0.0, 0.0),
                          color="black")
    img.draw()
    win.flip()
    core.wait(4)

def hello_text():
    f = codecs.open('C:/Users/Laptop/Desktop/Informatyka projekt/welcome.txt', encoding='utf-8')
    text_file = f.read()
    img = visual.TextStim(win, text=text_file, pos=(0.0, 0.0), color="black")
    img.draw()
    win.flip()
    clicked = event.waitKeys(keyList=['space'])
    if clicked == ["space"]:
        core.wait(0)
    img.draw()
    win.flip()


# wyswietlania 4 blokow plus przerwa, po ostatnim bloku - 'dziękujemy'
hello_text()
i = 4
while i > 0:
    for picturesSet in createBlock():
        displaySet(picturesSet)
    if i > 1:
        breake()
    else:
        end()
    i-=1

win.flip()
win.close()
