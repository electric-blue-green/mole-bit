__author__ = "@electric-blue-green"
from microbit import *
import random
gamemode = 0
mole_number = 0
score = 0
mole_tl  = Image("99000:"   ## mole_number = 1
                 "99000:"
                 "00000:"
                 "00000:"
                 "00000")

mole_tr = Image("00099:"    ## mole_number = 2
                "00099:"
                "00000:"
                "00000:"
                "00000")

mole_br = Image("00000:"    ## mole_number = 3
                "00000:"
                "00000:"
                "00099:"
                "00099")

mole_bl = Image("00000:"    ## mole_number = 4
                "00000:"
                "00000:"
                "99000:"
                "99000")
def show_mole_tl(mole_number, gamemode, score):
    while True:
        display.show(mole_tl)
        if button_a.is_pressed():
            display.clear()
            score += 1
            global score
            score_display = str(score)
            display.show(score_display)
            sleep(300)
            return
        elif button_b.is_pressed():
            display.clear()
            score = score
            global score
            score_display = str(score)
            display.show(score_display)
            sleep(300)
            return
        sleep(1000)
        display.clear()
        return

def show_mole_tr(mole_number, gamemode, score):
    while True:
        display.show(mole_tr)
        if button_b.is_pressed():
            display.clear()
            score += 1
            global score
            score_display = str(score)
            display.show(score_display)
            sleep(300)
            return
        elif button_a.is_pressed():
            display.clear()
            score = score
            global score
            score_display = str(score)
            display.show(score_display)
            sleep(300)
            return
        sleep(1000)
        display.clear()
        return

def show_mole_br(mole_number, gamemode, score):
    while True:
        display.show(mole_br)
        if button_b.is_pressed():
            display.clear()
            score += 1
            global score
            score_display = str(score)
            display.show(score_display)
            sleep(300)
            return
        elif button_a.is_pressed():
            display.clear()
            score = score
            global score
            score_display = str(score)
            display.show(score_display)
            sleep(300)
            return
        sleep(1000)
        display.clear()
        return

def show_mole_bl(mole_number, gamemode, score):
    while True:
        display.show(mole_br)
        if button_a.is_pressed():
            display.clear()
            score += 1
            global score
            score_display = str(score)
            display.show(score_display)
            sleep(300)
            return
        elif button_b.is_pressed():
            display.clear()
            score = score
            global score
            score_display = str(score)
            display.show(score_display)
            sleep(300)
            return
        sleep(1000)
        display.clear()
        return

def main(mole_number, gamemode, score):
    while gamemode == 0:
        mole_number = random.randint(1, 4)
        if mole_number == 1:
            show_mole_tl(mole_number, gamemode, score)
        elif mole_number == 2:
            show_mole_tr(mole_number, gamemode, score)
        elif mole_number == 3:
            show_mole_br(mole_number, gamemode, score)
        elif mole_number == 4:
            show_mole_bl(mole_number, gamemode, score)

main(mole_number, gamemode, score)
