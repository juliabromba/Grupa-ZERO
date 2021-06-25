# -*- coding: utf-8 -*-
"""
Created on Sun Jun 20 21:00:52 2021

@author: Julia
"""

from psychopy import visual, core, event
import random
import csv
import os, sys
from random import shuffle
from pathlib import Path
import codecs
N_TRIALS_TRAIN = 1
N_TRIALS_EXP = 1
hello_info = 'C:/Users/Julia/PycharmProjects/pythonProject/welcome.txt'
breake_info = "Przerwa, aby przejść do następnego bloku naciśnij spacje"
aft_train_info = "Koniec treningu, nacinij spację, żeby przejsć do zadania."
end_info = "Koniec, dziękujemy za udział w badaniu"
REACTION_KEYS = ['left', 'right']
RESULTS = [["NR", "EXPERIMENT", "REACTION_KEY", "ACC"]]
# okno glowne
win = visual.Window(units="pix", color="white", fullscr=False)

# sciezki do plikow w dwoch folderach happy i angry na dysku
happypath = "C:/Users/Julia/PycharmProjects/pythonProject/happy"
happy_pictures = list(os.listdir(happypath))
angrypath = "C:/Users/Julia/PycharmProjects/pythonProject/angry"
angry_pictures = list(os.listdir(angrypath))

#punkt fiksacji
fix = visual.TextStim(win, text="+", color = "black", height=40)

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


def angry_niezgodny(angry_pictures,
                    happy_pictures):  # warunek angry niezgodny, w srodku angry, po bokach happy
    shuffle(angry_pictures)
    shuffle(happy_pictures)
    center = angry_pictures[0]
    left = happy_pictures[1]
    right = happy_pictures[1]
    angry2 = [left, center, right]
    return angry2


def happy_niezgodny(angry_pictures,
                    happy_pictures):  # warunek happy niezgodny, w srodku happy, po bokach angry
    shuffle(angry_pictures)
    shuffle(happy_pictures)
    center = happy_pictures[0]
    left = angry_pictures[1]
    right = angry_pictures[1]
    happy2 = [left, center, right]
    return happy2


def createBlock():
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

for center in happy_zgodny(happy_pictures) and happy_niezgodny(angry_pictures,happy_pictures) and angry_niezgodny(angry_pictures, happy_pictures) and angry_zgodny(angry_pictures):
    stim = {"left": happy_pictures, "right": angry_pictures}
stim_type = list(stim.keys())

def displaySet(picturesSet):
    reaction = event.getKeys(keyList=list(REACTION_KEYS))
    key = reactions(REACTION_KEYS)
    win.flip()
    acc = stim_type == key
        
    trial1_center = os.path.abspath(picturesSet[1])
    trial1_left = os.path.abspath(picturesSet[0])
    trial1_right = os.path.abspath(picturesSet[2])

    srodek = visual.ImageStim(win, image=trial1_center, pos=(0.0, 0.0), size=[300, 377], colorSpace='rgb')
    lewy = visual.ImageStim(win, image=trial1_left, pos=(-310.0, 0.0), size=[300, 377], colorSpace='rgb')
    prawy = visual.ImageStim(win, image=trial1_right, pos=(310.0, 0.0), size=[300, 377], colorSpace='rgb')
    fix.draw()
    win.flip()
    core.wait(1)
    srodek.draw()
    prawy.draw()
    lewy.draw()
    win.flip()
    core.wait(1)
    RESULTS.append([reaction, key, acc])



def reactions(keys):
    event.clearEvents()
    key = event.waitKeys(keyList=keys)
    return key[0]

def show_text(win, info, wait_key=["space"]):
    info.draw()
    win.flip()
    reactions(wait_key)
   
def hello_text():
    text_file = codecs.open(hello_info, encoding='utf-8').read()
    show_text(win, info = visual.TextStim(win, text=text_file, pos=(0.0, 0.0), color="black"))
    
def breake():
    show_text(win, info = visual.TextStim(win, text= breake_info, pos=(0.0, 0.0), color="black"))
    
def after_training():
    show_text(win, info = visual.TextStim(win, text= aft_train_info, pos=(0.0, 0.0), color="black"))
    
    
def end():
    img = visual.TextStim(win, text= end_info, pos=(0.0, 0.0), color="black")
    img.draw()
    win.flip()
    core.wait(4)



  
def part_of_exp(n_trials, exp):
    for i in range (n_trials): 
        for picturesSet in createBlock():
            displaySet(picturesSet)
        
        if exp == True:
            if i < (N_TRIALS_EXP - 1):
                breake()
            else:
                end()
        else:
            if i <(N_TRIALS_TRAIN - 1):
                breake()
            else:
                after_training()
        
        RESULTS.append([i+1, exp,])

hello_text()
part_of_exp(N_TRIALS_TRAIN, exp = False)
part_of_exp(N_TRIALS_EXP, exp = True)

with open("result.csv", "a", newline='') as f:
    write = csv.writer(f)
    write.writerows(RESULTS)

win.flip()
win.close()