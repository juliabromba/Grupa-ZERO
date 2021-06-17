from psychopy import visual, core, event
import random
import csv
import os, sys
from random import shuffle

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


print(happy_zgodny(happy))
print(angry_zgodny(angry))
print(angry_niezgodny(angry, happy))
print(happy_niezgodny(angry, happy))
