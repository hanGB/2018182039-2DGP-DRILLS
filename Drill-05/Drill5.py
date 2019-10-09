from pico2d import *

KPU_WIDTH, KPU_HEIGHT = 1280, 1024

open_canvas(KPU_WIDTH, KPU_HEIGHT)

kpu = load_image("KPU_GROUND.png")
hand_arrow = load_image("hand_arrow.png")
character = load_image("animation_sheet.png")

def input_mouse():
    global game
    global x, y

    events = get_events()

    for event in events:
        if event.type == SDL_QUIT:
            game = False
        elif event.type == SDL_MOUSEMOTION:
            x, y = event.x, KPU_HEIGHT- 1 - event.y

game = True

x, y = KPU_WIDTH / 2, KPU_HEIGHT / 2

hide_cursor()

while game:
    clear_canvas()

    kpu.draw(KPU_WIDTH / 2, KPU_HEIGHT / 2)
    hand_arrow.draw(x, y)
    input_mouse()

    update_canvas()