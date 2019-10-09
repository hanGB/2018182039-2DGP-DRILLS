from pico2d import *

KPU_WIDTH, KPU_HEIGHT = 1280, 1024

open_canvas(KPU_WIDTH, KPU_HEIGHT)

kpu = load_image("KPU_GROUND.png")
hand_arrow = load_image("hand_arrow.png")
character = load_image("animation_sheet.png")

def input_mouse():
    global game
    global mouse_x, mouse_y
    global start_x, start_y
    global end_x, end_y
    global character_x, character_y
    events = get_events()

    for event in events:
        if event.type == SDL_QUIT:
            game = False
        elif event.type == SDL_MOUSEMOTION:
            mouse_x, mouse_y = event.x + 25, KPU_HEIGHT- 1 - event.y - 26
        elif event.type == SDL_MOUSEBUTTONDOWN:
            start_x = character_x
            start_y = character_y
            end_x = mouse_x
            end_y = mouse_y



game = True

mouse_x, mouse_y = KPU_WIDTH / 2, KPU_HEIGHT / 2

hide_cursor()

face = 1
aniType = 0
frame = 0
moving = False
character_x, character_y = KPU_WIDTH / 2, KPU_HEIGHT / 2
start_x, start_y = KPU_WIDTH / 2, KPU_HEIGHT / 2
end_x, end_y = KPU_WIDTH / 2, KPU_HEIGHT / 2

while game:
    clear_canvas()

    kpu.draw(KPU_WIDTH / 2, KPU_HEIGHT / 2)
    hand_arrow.draw(mouse_x, mouse_y)

    if moving == False:
        if face == 1:
            aniType = 3
        elif face == -1:
            aniType = 2
    else:
        if face == 1:
            aniType = 1
        elif face == -1:
            aniType = 0

    character_x = end_x
    character_y = end_y

    character.clip_draw(frame * 100, 100 * aniType, 100, 100, character_x, character_y)
    frame = (frame + 1) % 8

    input_mouse()

    update_canvas()