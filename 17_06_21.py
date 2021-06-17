from psychopy import visual, core, event
import random
import csv
import os, sys
from random import shuffle
from pathlib import Path

win = visual.Window([1520, 880], units="pix", color="white", fullscr=False)

happypath = "C:/Users/Laptop/Desktop/Informatyka projekt/happy"
happy = list(os.listdir(happypath))
angrypath = "C:/Users/Laptop/Desktop/Informatyka projekt/angry"
angry = list(os.listdir(angrypath))


def happy_zgodny(happy):
    shuffle(happy)
    center = happy[0]
    left = happy[1]
    right = happy[1]
    happy1 = [left, center, right]
    return happy1


def angry_zgodny(angry):
    shuffle(angry)
    center = angry[0]
    left = angry[1]
    right = angry[1]
    angry1 = [left, center, right]
    return angry1


def angry_niezgodny(angry, happy):
    shuffle(angry)
    shuffle(happy)
    center = angry[0]
    left = happy[1]
    right = happy[1]
    angry2 = [left, center, right]
    return angry2


def happy_niezgodny(angry, happy):
    shuffle(angry)
    shuffle(happy)
    center = happy[0]
    left = angry[1]
    right = angry[1]
    happy2 = [left, center, right]
    return happy2


a = happy_zgodny(happy)
b = angry_zgodny(angry)
c = angry_niezgodny(angry,happy)
d = happy_niezgodny(angry, happy)

trial1_center = os.path.abspath(a[1])
trial1_left = os.path.abspath(a[0])
trial1_right = os.path.abspath(a[2])

srodek = visual.ImageStim(win, image=trial1_center, pos=(0.0, 0.0), size=[300, 377], colorSpace='rgb')
lewy = visual.ImageStim(win, image=trial1_left, pos=(-310.0, 0.0), size=[300, 377], colorSpace='rgb')
prawy = visual.ImageStim(win, image=trial1_right, pos=(310.0, 0.0), size=[300, 377], colorSpace='rgb')
srodek.draw()
prawy.draw()
lewy.draw()
win.flip()
core.wait(6)

win.flip()
win.close()
