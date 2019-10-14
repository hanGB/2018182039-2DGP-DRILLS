from pico2d import *
import random

# Game object class here


class Grass:
    def __init__(self):
        self.image = load_image("grass.png")

    def draw(self):
        self.image.draw(400, 30)


class Boy:
    def __init__(self):
        self.x, self.y = random.randint(0, 800), 90
        self.image = load_image("run_animation.png")
        self.frame = random.randint(0, 8)

    def update(self):
        self.frame = (self.frame + 1) % 8
        self.x += 0.5

    def draw(self):
        self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y)


class Ball:
    def __init__(self):
        self.x, self.y = random.randint(0, 800), 599
        self.size = random.randint(0, 1)
        self.speed = random.randint(1, 20)
        self.falling = True
        if self.size == 0:
            self.image = load_image("ball21x21.png")
        elif self.size == 1:
            self.image = load_image("ball41x41.png")

    def update(self):
        if self.size == 0:
            if self.y <= 61:
                self.y = 61
            else:
                self.y -= self.speed / 10
        if self.size == 1:
            if self.y <= 71:
                self.y = 71
            else:
                self.y -= self.speed / 10

    def draw(self):
        self.image.draw(self.x, self.y)


def handle_events():
    global game
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game = False

# initialization code


open_canvas()

grass = Grass()
# boy = Boy()
team = [Boy() for i in range(11)]
falling_balls = [Ball() for i in range(20)]
game = True

# game main loop code


while game:
    handle_events()

    for boy in team:
        boy.update()

    for ball in falling_balls:
        ball.update()

    clear_canvas()
    grass.draw()

    for boy in team:
        boy.draw()

    for ball in falling_balls:
        ball.draw()

    update_canvas()

# finalization code


close_canvas()