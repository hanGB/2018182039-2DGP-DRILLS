from pico2d import *
import random


class SmallBall:
    image = None

    def __init__(self):
        self.x = random.randint(50, 1230)
        self.y = random.randint(50, 970)

        if SmallBall.image is None:
            SmallBall.image = load_image("ball21x21.png")

    def get_bb(self):
        return self.x - 10, self.y - 10, self.x + 10, self.y + 10

    def get_xy(self):
        return self.x, self.y

    def update(self):
        pass

    def draw(self):
        SmallBall.image.draw(self.x, self.y)


class BigBall:
    image = None

    def __init__(self):
        self.x = random.randint(50, 1230)
        self.y = random.randint(50, 970)

        if BigBall.image is None:
            BigBall.image = load_image("ball41x41.png")

    def get_bb(self):
        return self.x - 20, self.y - 20, self.x + 20, self.y + 20

    def get_xy(self):
        return self.x, self.y

    def update(self):
        pass

    def draw(self):
        BigBall.image.draw(self.x, self.y)

