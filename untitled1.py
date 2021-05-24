# -*- coding: utf-8 -*-
"""
Created on Mon May 24 17:46:10 2021

@author: Julia
"""


# instrukcja
#przechodzenie spacją
# zrobic po 2, póki co, przykłady obu kongruentnych i niekongruentnych, żeby się losowo wywietlały.
from psychopy import visual, core, event
import random
import csv

REACTION_KEYS = ['up', 'down']
# dodać czas reakcji, numer proby, czy zgodna, czy niezgodna
RESULTS = [["ACC", "REACTION"]]
def reactions(keys):
    event.clearEvents()
    key = event.waitKeys(keyList=keys)
    return key[0]

win = visual.Window(units="pix", color="gray", fullscr=False)

happy = visual.ImageStim(win,image="C:/Users/Julia/PycharmProjects/pythonProject/happy.jpg", pos=(0.0, 0.0), size=[200, 200
                                                                                                                   ], colorSpace = 'rgb')
angry = visual.ImageStim(win,image="C:/Users/Julia/PycharmProjects/pythonProject/angry.jpg", pos=(0.0, 0.0), size=[200, 200
                                                                                                                 ], colorSpace = 'rgb')
fix = visual.TextStim(win, text="+", height=40)

stim = {"up": happy,
        "down": angry}

def part_of_exp(n_trials, exp, fix):
        for i in range(2):
            imag2 = random.choice(list(stim.keys()))
            if imag2 == happy:
                imag1 = angry
                imag3 = angry
            else:
                imag1 = happy
                imag3 = happy
    
            imag1.pos = (-250.0, 0.0)
            imag3.pos = (250.0, 0.0)
        #punkt fiksacji
            fix.draw()
            win.flip()
            core.wait(1)
        
#no tu jest generalnie wyswietlanie randomowo img1/img2 i wypisuje do wyników poprawna/niepoprawna reakcje
            imag1.draw()
            stim[imag2].draw()
            imag3.draw()
            win.flip()
            key = reactions(REACTION_KEYS)
            acc=imag2 == key
            RESULTS.append([acc, key])

#img2.draw()
part_of_exp(n_trials=2, exp=True, fix=fix)
#tworzy plik z wynikami
with open("wyniki.csv", "w", newline='') as f:
    write = csv.writer(f)
    write.writerows(RESULTS)

win.flip()

    

win.close()