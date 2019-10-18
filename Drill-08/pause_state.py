import random
import json
import os

from pico2d import *

import game_framework
import main_state

name = "Pause_state"

pause = None
grass = None


class Pause:
    def __init__(self):
        self.frame = 0
        self.image = load_image('pause.png')

    def update(self):
        self.frame = (self.frame + 1) % 200

    def draw(self):
        if self.frame < 100:
            self.image.draw(400, 300, 200, 200)


def enter():
    global pause

    global grass
    global boy

    pause = Pause()
    grass = main_state.Grass()
    boy = main_state.Boy()


def exit():
    global pause
    del (pause)


def pause():
    pass


def resume():
    pass


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_p:
            game_framework.pop_state()


def update():
    pause.update()

def draw():
    clear_canvas()
    grass.draw()
    main_state.boy.draw()
    pause.draw()
    update_canvas()
