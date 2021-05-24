# -*- coding: utf-8 -*-
"""
Created on Wed May 19 23:58:10 2021

@author: Julia
"""
# zrobic po 2, póki co, przykłady obu kongruentnych i niekongruentnych, żeby się losowo wywietlały.
from psychopy import visual, core, event
import random
import csv

REACTION_KEYS = ['up', 'down']
RESULTS = [["ACC", "REACTION"]]
def reactions(keys):
    event.clearEvents()
    key = event.waitKeys(keyList=keys)
    return key[0]

win = visual.Window(units="pix", color="gray", fullscr=False)

img1 = visual.ImageStim(win,image="C:/Users/Julia/PycharmProjects/pythonProject/synyyy.png", pos=(0.0, 0.0), size=[200, 200
                                                                                                                   ], colorSpace = 'rgb')
img2 = visual.ImageStim(win,image="C:/Users/Julia/PycharmProjects/pythonProject/atari.JPG", pos=(250.0, 0.0), size=[200, 200
                                                                                                                   ], colorSpace = 'rgb')
#warunek zgodny HAPPY
img1.pos = (0.0,0.0) 
#nie wiem, czy da się 3x wrzucic ten sam obrazek, czy muszę załadować 6 i wybierać do poszczególnych triali odpowiednie.

#warunek zgodny ANGRY
#warunek niezgodny HAPPY
#warunek niezgodny ANGRY
for i in range(2):
#CHYBA CHCE TU PRZYLACZYC POPRAWNĄ REAKCJĘ DO OBRAZU
    stim = {"up": img1,
            "down": img2}
#no tu jest generalnie wyswietlanie randomowo img1/img2 i wypisuje do wyników poprawna/niepoprawna reakcje
    stim_type = random.choice(list (stim.keys()))
    stim[stim_type].draw()
    win.flip()
    key = reactions(REACTION_KEYS)
    acc=stim_type == key
    RESULTS.append([acc, key])

#img2.draw()

#tworzy plik z wynikami
with open("res.csv", "w", newline='') as f:
    write = csv.writer(f)
    write.writerows(RESULTS)

win.flip()

    

win.close()