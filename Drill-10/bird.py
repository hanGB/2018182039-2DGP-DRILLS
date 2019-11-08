from pico2d import *
import game_framework

PIXEL_PER_METER = (10.0 / 0.3)
RUN_SPEED_KMPH = 50.0
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 8


class Bird:
    image = None

    def __init__(self):
        if Bird.image is None:
            Bird.image = load_image('bird_animation.png')
        self.x = 50
        self.y = 300
        self.frame = 0
        self.velocity = RUN_SPEED_PPS

    def update(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 14
        self.x += self.velocity * game_framework.frame_time
        self.x = clamp(25, self.x, 1600 - 25)
        if self.x < 30 or self.x > 1600 - 30:
            self.velocity *= -1

    def draw(self):
        if int(self.frame) < 5:
            fx = int(self.frame)
            fy = 0
        elif int(self.frame) < 10:
            fx = int(self.frame) - 5
            fy = 1
        elif int(self.frame) < 14:
            fx = int(self.frame) - 10
            fy = 2

        Bird.image.clip_draw(183 * fx, 169 * fy, 183, 169, self.x, self.y, 3 * PIXEL_PER_METER, 2 * PIXEL_PER_METER)