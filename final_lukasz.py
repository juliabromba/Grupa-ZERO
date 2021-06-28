from psychopy import visual, core, event, gui, logging
import random
import csv
import os, sys
from random import shuffle
from pathlib import Path
import codecs
import yaml

# plik konfiguracyjny
conf = yaml.safe_load(open('config.yaml', encoding='utf-8'))

# zmienne globalne
clock = core.Clock()
N_TRIALS_TRAIN = conf['N_BLOCKS_TRAIN']
N_TRIALS_EXP = conf['N_BLOCKS_EXPERIMENT']
hello_info = conf['HELLO_INFO']
breake_info = conf['BREAKE_INFO']
aft_train_info = conf['AFTER_TRAIN_INFO']
end_info = conf['END_INFO']
FIX_TIME = conf['FIX_CROSS_TIME']
TRIAL_TIME = conf['IMAGE_SET_TIME']
# lista z wynikami
RESULTS = []
RESULTS.append(["IDENTYFIKATOR", "Plec", "Wiek"])

    
"""okno startowe w ktorym trzeba podac kilka danych, ID, plec, wiek, ono musi być na poczatku, bo 
inaczej full screen win nam wszystko przysloni, podobno znany problem na forum"""


def poop_up():
    info = {'IDENTYFIKATOR': '', u'P\u0141EC': ['M', "K"], 'WIEK': ''}
    hello_dlg = gui.DlgFromDict(dictionary=info, title='Grupa Zero')
    if not hello_dlg.OK:
        abort_with_error('Info dialog terminated.')
    list = [info['IDENTYFIKATOR'], info['PŁEC'], info['WIEK']]
    RESULTS.append(list)

def abort_with_error(err):
    logging.critical(err)
    raise Exception(err)

poop_up()

# okno glowne
win = visual.Window(units="pix", color=conf['BACKGROUND_COLOR'], fullscr=True)
# punkt fiksacji
fix = visual.TextStim(win, text="+", color=conf['FIX_CROSS_COLOR'], height=40)

# listy ścieżek do plikow w dwoch folderach - happy i angry
happypath = conf['HAPPY_FOLDER']
happy_pictures = list(os.listdir(happypath))
angrypath = conf['ANGRY_FOLDER']
angry_pictures = list(os.listdir(angrypath))


# tworzy plik wynikowy
def save_result():
    with open("result.csv", "a", newline='', encoding='utf-8') as f:
        write = csv.writer(f)
        write.writerows(RESULTS)


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

# tworzenie listy z osmioma warunkami, kazdy z 4 podwojnie. Liste mieszamy, dodajemy nazwy plików zdjęciowych do wyników
# i dodajemy nagłówki do wyników, które przyjdą z PicturesSet
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
    RESULTS.append(block)
    RESULTS.append(["REACTION", "CONDITION", "ACC", "TIME"])
    return block


""" funkcja, ktora wyswietla jeden blok, pctureset to zmienna zadeklarowana przez nas, trial1_center to jakas
zmienna i wskazanie sciezki do niej z listy pictureset (tej listy nie mamy w ogole w programie, uzywamy jej tylko tutaj,
prawdziwe dane wskazemy pozniej w petli!, na koncu tworzymy 3 zmienne, do ktorej trafiaja nasze pliki i te zmienne sa 
wyswietlane w oknie win"""


def displaySet(picturesSet):
    win.callOnFlip(clock.reset)
    trial1_center = os.path.abspath(picturesSet[1])
    trial1_left = os.path.abspath(picturesSet[0])
    trial1_right = os.path.abspath(picturesSet[2])
    
    if picturesSet[1] in happy_pictures: #zdefiniowanie poprawnej 'reakcji' na trial
        key = ['left']
    else:
        key = ['right']
        
    reaction = event.getKeys(keyList=list(conf['REACTION_KEYS'])) #zebranie reakcji badanego
    srodek = visual.ImageStim(win, image=trial1_center, pos=(0.0, 0.0), size=[300, 377], colorSpace='rgb')
    lewy = visual.ImageStim(win, image=trial1_left, pos=(-310.0, 0.0), size=[300, 377], colorSpace='rgb')
    prawy = visual.ImageStim(win, image=trial1_right, pos=(310.0, 0.0), size=[300, 377], colorSpace='rgb')
    fix.draw()
    win.flip()
    core.wait(FIX_TIME)
    srodek.draw()
    prawy.draw()
    lewy.draw()
    win.flip()
    core.wait(TRIAL_TIME)
    rt = clock.getTime() #czas reakcji z czasem core.waitów (do wyników dopisuje się pomniejszony o TRIAL i FIX_TIME)

    acc = key == reaction #sprawdzenie poprawności reakcji
    RESULTS.append([reaction, key, acc, rt-(TRIAL_TIME+FIX_TIME)]) #dopisanie do wyników


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
    show_text(win, info=visual.TextStim(win, text=text_file, pos=(0.0, 0.0), color="black"))


def breake():
    show_text(win, info=visual.TextStim(win, text=breake_info, pos=(0.0, 0.0), color="black"))


def after_training():
    show_text(win, info=visual.TextStim(win, text=aft_train_info, pos=(0.0, 0.0), color="black"))


def end():
    img = visual.TextStim(win, text=end_info, pos=(0.0, 0.0), color="black")
    img.draw()
    win.flip()
    core.wait(1)


"""model eksperymentu - dla 'exp=False' robi trening, jeśli trening ma więcej, niż 1 blok, to pomiędzy blokami 
robi przerwę, a po ostatnim mówi, że pora na eksperyment dla 'exp = True' robi eksperyment z przerwami i informacją 
o zakończeniu po ostatnim bloku"""


def part_of_exp(n_trials, exp):
    for i in range(n_trials):
        for picturesSet in createBlock():
            displaySet(picturesSet)
        if exp == True:
            exp1 = "EKSPERYMENT WLASCIWY"
            if i < (N_TRIALS_EXP - 1):
                breake()
            else:
                end()
        else:
            exp1 = "TRIAL PROBNY"
            if i < (N_TRIALS_TRAIN - 1):
                breake()
            else:
                after_training()
        RESULTS.append([exp1])  # dodaje wyniki do pliku wynikowego


hello_text()
part_of_exp(N_TRIALS_TRAIN, exp=False)
part_of_exp(N_TRIALS_EXP, exp=True)
save_result()

win.flip()
win.close()
