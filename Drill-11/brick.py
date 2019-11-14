from pico2d import *
import game_framework


class Brick:
    image = None

    def __init__(self):
        if Brick.image == None:
            Brick.image = load_image('brick180x40.png')
        self.x, self.y, self.fall_speed = 0, 180, 200
        self.dir = 1

    def get_bb(self):
        # fill here
        return self.x - 90, self.y - 20, self.x + 90, self.y + 20

    def draw(self):
        self.image.draw(self.x, self.y)
        # fill here for draw
        draw_rectangle(*self.get_bb())

    def update(self):
        if self.x < 0 or self.x > 1600:
            self.dir *= -1

        self.x += self.dir * self.fall_speed * game_framework.frame_time


