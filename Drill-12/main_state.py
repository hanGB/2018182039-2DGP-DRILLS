import random
import json
import os

from pico2d import *
import game_framework
import game_world

from boy import Boy
from ground import Ground
from zombie import Zombie
from ball import BigBall
from ball import SmallBall

name = "MainState"

boy = None
zombie = None
bigBall = None
smallBall = None
end = None


def collide(a, b):
    # fill here
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()

    if left_a > right_b: return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False

    return True

def get_boy():
    return boy


def enter():
    global end
    end = False

    global boy
    boy = Boy()
    game_world.add_object(boy, 1)

    global zombie
    zombie = Zombie()
    game_world.add_object(zombie, 1)

    ground = Ground()
    game_world.add_object(ground, 0)

    global bigBall
    bigBall = [BigBall() for i in range(5)]

    for i in range(5):
        game_world.add_object(bigBall[i], 0)

    global smallBall
    smallBall = [SmallBall() for i in range(5)]

    for i in range(5):
        game_world.add_object(smallBall[i], 0)


def exit():
    game_world.clear()


def pause():
    pass


def resume():
    pass


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
                game_framework.quit()
        else:
            boy.handle_event(event)


def update():
    for game_object in game_world.all_objects():
        game_object.update()
    global boy
    global zombie
    global bigBall
    global smallBall
    global end

    if not end:
        if collide(boy, zombie):
            end = True
            if (len(bigBall) + len(smallBall)) == 0:
                game_world.remove_object(boy)
            else:
                game_world.remove_object(zombie)

        else:
            if len(bigBall) > 0:
                for bb in bigBall:
                    if collide(bb, zombie):
                        bigBall.remove(bb)
                        game_world.remove_object(bb)
                        zombie.add_hp(100)

            elif len(smallBall) > 0:
                for sb in smallBall:
                    if collide(sb, zombie):
                        smallBall.remove(sb)
                        game_world.remove_object(sb)
                        zombie.add_hp(50)

def draw():
    clear_canvas()
    for game_object in game_world.all_objects():
        game_object.draw()
    update_canvas()






