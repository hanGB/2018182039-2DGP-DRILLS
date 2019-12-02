from pico2d import *
import random
import main_state

class Ball:
    image = None

    def __init__(self):
        if Ball.image is None:
            Ball.image = load_image("ball41x41.png")

        self.x = random.randint(50, 1750)
        self.y = random.randint(50, 1050)

    def get_bb(self):
        return self.x - 20, self.y - 20, self.x + 20, self.y + 20

    def draw(self):
        wl, wb = main_state.background.get_window_left_bottom()
        cx, cy = self.x - wl, self.y - wb
        Ball.image.draw(cx, cy)

    def update(self):
        pass
