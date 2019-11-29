import game_framework
from pico2d import *
import world_build_state as start_state

font = None


def enter():
    global font
    font = load_font('ENCR10B.TTF', 50)
    pass


def exit():
    global font
    del font
    pass


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
            game_framework.change_state(start_state)


def update():
    pass


def draw():
    clear_canvas()
    with open('ranking.json', 'r') as f:
        time = json.load(f)

    if len(time) < 10:
        for i in range(len(time)):
            font.draw(300, 800 - i * 50, '#: %d' % (i + 1), (0, 0, 0))
            font.draw(500, 800 - i * 50, '(Time: %3.2f)' % time[i], (0, 0, 0))
    else:
        for i in range(10):
            font.draw(300, 800 - i * 50, '#: %d' % (i + 1), (0, 0, 0))
            font.draw(500, 800 - i * 50, '(Time: %3.2f)' % time[i], (0, 0, 0))
    update_canvas()
