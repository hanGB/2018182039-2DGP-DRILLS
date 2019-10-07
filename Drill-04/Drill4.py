from pico2d import *


def handle_events():
    global running
    global dir
    global face

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                dir += 1
                face = dir
            elif event.key == SDLK_LEFT:
                dir -= 1
                face = dir
            elif event.key == SDLK_ESCAPE:
                running = False
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                dir -= 1
            elif event.key == SDLK_LEFT:
                dir += 1
    pass


open_canvas()
grass = load_image('grass.png')
character = load_image('animation_sheet.png')

running = True
x = 800 // 2
frame = 0
dir = 0
face = 1
aniType = 1

while running:
    clear_canvas()
    grass.draw(400, 30)

    if dir == 0:
        if face == 1:
            aniType = 3
        elif face == -1:
            aniType = 2
    else:
        if face == 1:
            aniType = 1
        elif face == -1:
            aniType = 0

    character.clip_draw(frame * 100, 100 * aniType, 100, 100, x, 90)

    update_canvas()

    handle_events()

    frame = (frame + 1) % 8
    if (x != 15 and dir == -1) or (x != 785 and dir == 1):
        x += dir

close_canvas()

