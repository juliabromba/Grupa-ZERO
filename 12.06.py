# -*- coding: utf-8 -*-
"""
Created on Sun Jun 13 12:41:58 2021

@author: Julia
"""

# -*- coding: utf-8 -*-
"""
Created on Mon May 24 17:46:10 2021

@author: Julia
"""


# instrukcja
#przechodzenie spacją

from psychopy import visual, core, event
import random
import csv

REACTION_KEYS = ['left', 'right']
# dodać czas reakcji, numer proby, czy zgodna, czy niezgodna
RESULTS = [["ACC", "REACTION"]]
def reactions(keys):
    event.clearEvents()
    key = event.waitKeys(keyList=keys)
    return key[0]

win = visual.Window(units="pix", color="white", fullscr=False)

#adding stimuli
# TO JEST WERSJA Z TRZEMA HAPPY I TRZEMA ANGRY BUŹKAMI, ŻEBY NIE DODAWAĆ 24x3, COBY LEPIEJ SIĘ PRACOWAŁO PÓKI CO.
# 'h' to zadowolone, 'a' to angry. 1a i 1b to ta sama buźka, zakładając, że każdą trzeba wrzucić trzy razy - to chcę jakos ogarnąć, żeby móc wrzucić jedną buźkę tylko raz, ale z tego, co zrozumiałam od Michała, może się nie udać.
# może visual.ElementArrayStim cos tu pomoże, ale nie ogarniam jeszcze do końca jak działa. Ewentualnie myslałam jeszcze o opcji losowania pliku z folderu /dwa foldery - ANGRY, HAPPY/, ale nie wiem, czy w ogóle istnieje taka opcja w kodzie.


h1 = visual.ImageStim(win,image="C:/Users/Julia/PycharmProjects/pythonProject/happy/004_o_m_h_a.jpg", pos=(0.0, 0.0), size=[200, 200
                                                                                                                   ], colorSpace = 'rgb')
h2 = visual.ImageStim(win,image="C:/Users/Julia/PycharmProjects/pythonProject/happy/004_o_m_h_b.jpg", pos=(0.0, 0.0), size=[200, 200
                                                                                                                   ], colorSpace = 'rgb')
h3 = visual.ImageStim(win,image="C:/Users/Julia/PycharmProjects/pythonProject/happy/066_y_m_h_a.jpg", pos=(0.0, 0.0), size=[200, 200
                                                                                                                   ], colorSpace = 'rgb')
h1a = visual.ImageStim(win,image="C:/Users/Julia/PycharmProjects/pythonProject/happy/004_o_m_h_a.jpg", pos=(-250.0, 0.0), size=[200, 200
                                                                                                                   ], colorSpace = 'rgb')
h2a = visual.ImageStim(win,image="C:/Users/Julia/PycharmProjects/pythonProject/happy/004_o_m_h_b.jpg", pos=(-250.0, 0.0), size=[200, 200
                                                                                                                   ], colorSpace = 'rgb')
h3a = visual.ImageStim(win,image="C:/Users/Julia/PycharmProjects/pythonProject/happy/066_y_m_h_a.jpg", pos=(-250.0, 0.0), size=[200, 200
                                                                                                                   ], colorSpace = 'rgb')
h1b = visual.ImageStim(win,image="C:/Users/Julia/PycharmProjects/pythonProject/happy/004_o_m_h_a.jpg", pos=(250.0, 0.0), size=[200, 200
                                                                                                                   ], colorSpace = 'rgb')
h2b = visual.ImageStim(win,image="C:/Users/Julia/PycharmProjects/pythonProject/happy/004_o_m_h_b.jpg", pos=(250.0, 0.0), size=[200, 200
                                                                                                                   ], colorSpace = 'rgb')
h3b = visual.ImageStim(win,image="C:/Users/Julia/PycharmProjects/pythonProject/happy/066_y_m_h_a.jpg", pos=(250.0, 0.0), size=[200, 200
                                                                                                                   ], colorSpace = 'rgb')
a1 = visual.ImageStim(win,image="C:/Users/Julia/PycharmProjects/pythonProject/angry/004_o_m_a_a.jpg", pos=(0.0, 0.0), size=[200, 200
                                                                                                                 ], colorSpace = 'rgb')
a2 = visual.ImageStim(win,image="C:/Users/Julia/PycharmProjects/pythonProject/angry/004_o_m_a_b.jpg", pos=(0.0, 0.0), size=[200, 200
                                                                                                                 ], colorSpace = 'rgb')
a3 = visual.ImageStim(win,image="C:/Users/Julia/PycharmProjects/pythonProject/angry/066_y_m_a_a.jpg", pos=(0.0, 0.0), size=[200, 200
                                                                                                                 ], colorSpace = 'rgb')
a1a = visual.ImageStim(win,image="C:/Users/Julia/PycharmProjects/pythonProject/angry/004_o_m_a_a.jpg", pos=(-250.0, 0.0), size=[200, 200
                                                                                                                 ], colorSpace = 'rgb')
a2a = visual.ImageStim(win,image="C:/Users/Julia/PycharmProjects/pythonProject/angry/004_o_m_a_b.jpg", pos=(-250.0, 0.0), size=[200, 200
                                                                                                                 ], colorSpace = 'rgb')
a3a = visual.ImageStim(win,image="C:/Users/Julia/PycharmProjects/pythonProject/angry/066_y_m_a_a.jpg", pos=(-250.0, 0.0), size=[200, 200
                                                                                                                 ], colorSpace = 'rgb')
a1b = visual.ImageStim(win,image="C:/Users/Julia/PycharmProjects/pythonProject/angry/004_o_m_a_a.jpg", pos=(250.0, 0.0), size=[200, 200
                                                                                                                 ], colorSpace = 'rgb')
a2b = visual.ImageStim(win,image="C:/Users/Julia/PycharmProjects/pythonProject/angry/004_o_m_a_b.jpg", pos=(250.0, 0.0), size=[200, 200
                                                                                                                 ], colorSpace = 'rgb')
a3b = visual.ImageStim(win,image="C:/Users/Julia/PycharmProjects/pythonProject/angry/066_y_m_a_a.jpg", pos=(250.0, 0.0), size=[200, 200
                                                                                                                 ], colorSpace = 'rgb')
# listy happy & angry
# pomyslałam, żeby wrzucić dwie listy, z których będzie losowanie konkretnej buźki, bo na zajęciach losowalismy z listy.
happy = [h1, h2, h3]
angry = [a1, a2, a3]
# both zrobiłam, żeby najpierw losowało, z której listy wylosuje. Ale to wszystko jest w ramach jednej z kilku koncepcji, które mi się zrobiły w głowie, więc jesli będzie inny sposób, to to też będzie wyglądało inaczej.
both = [happy, angry]

#fixation point - creating
fix = visual.TextStim(win, text="+", height=40)

#to jest zerżnięte z jednego z zadań na zajęciach - przypisuje przycisk do konkretnej buźki. W tej starej wersji z githuba działa, tutaj zaryzykowałam przypisanie całej listy - nie wiem, czy to by zadziałało, bo z resztą kodu mam problem, więc nie otworzę.
stim = {"up": happy,
        "down": angry}

#tego nie zmieniałam chyba z poprzedniej wersji. To jest ten fragment, w którym przy jednej usmiechniętej i jednej angry nadpisuje się happy buźka /wysyłałam Wam z tego filmik/
def part_of_exp(n_trials, exp, fix):
        for i in range(n_trials):
            imag2 = random.choice(both)
            
            if imag2 == happy:
                imag1 = angry1
                imag3 = angry3
#tu był problem z filmiku. Ale przy założeniu losowania z listy jw., to totalnie cała częsc kodu 'part_of_exp' nie odnosi się do niczego, co jest wyżej.
            else:
                imag1 = happy1
                imag3 = happy3
    
        #punkt fiksacji
            fix.draw()
            win.flip()
            core.wait(1)
        
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