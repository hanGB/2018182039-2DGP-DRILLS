from pico2d import *
import random

KPU_WIDTH, KPU_HEIGHT = 1280, 1024

open_canvas(KPU_WIDTH, KPU_HEIGHT)

kpu = load_image("KPU_GROUND.png")
character = load_image("animation_sheet.png")


def cancle():
    global game

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game = False

game = True

face = 1
frame = 0

pointx = [random.randint(0, KPU_WIDTH) for n in range(10)]
pointy = [random.randint(0, KPU_HEIGHT) for n in range(10)]

while game:
    for n in range(0, 10):
        for i in range(0, 100, 2):
            clear_canvas()
            kpu.draw(KPU_WIDTH / 2, KPU_HEIGHT / 2)
            t = i / 100
            character_x = ((-t ** 3 + 2 * t ** 2 - t) * pointx[n % 10] + (3 * t ** 3 - 5 * t ** 2 + 2) * pointx[(n + 1) % 10] + (-3 * t ** 3 + 4 * t ** 2 + t) * pointx[(n + 2) % 10] + (t ** 3 - t ** 2) * pointx[(n + 3) % 10]) / 2
            character_y = ((-t ** 3 + 2 * t ** 2 - t) * pointy[n % 10] + (3 * t ** 3 - 5 * t ** 2 + 2) * pointy[(n + 1) % 10] + (-3 * t ** 3 + 4 * t ** 2 + t) * pointy[(n + 2) % 10] + (t ** 3 - t ** 2) * pointy[(n + 3) % 10]) / 2
            if pointx[n % 9] - pointx[n + 1 % 9] < 0:
                face = 0
            else:
                face = 1
            character.clip_draw(frame * 100, 100 * face, 100, 100, character_x, character_y)
            frame = (frame + 1) % 8
            update_canvas()

            cancle()
            if game == False:
                break
                
            delay(0.05)


