import pygame as pg
from settings import *
from ray_casting import ray_casting
import math as m
class Drawing:
    def __init__(self, dis):
        self.dis = dis
        self.font = pg.font.SysFont('Arial', 36, bold=True)
        self.textures = {'0': pg.image.load('img/1.png').convert(),
                         '1': pg.image.load('img/2.png').convert(),
                         '2': pg.image.load('img/3.png').convert(),
                         'K': pg.image.load('img/sky2.jpg').convert(),
                         'S': pg.image.load('img/sky.png').convert(),
                         'I': pg.image.load('img/info.png').convert(),
                         'V': pg.image.load('img/infoblock.png').convert(),
                         'M': pg.image.load('img/doom_sky.png').convert(),
                         'F': pg.image.load('img/doom_1.png').convert(),
                         'G': pg.image.load('img/doom_2.png').convert(),
                         }

    def background(self, angle):
        sky_offset = -5 * m.degrees(angle) % WIDTH
        self.dis.blit(self.textures['S'], (sky_offset, 0))
        self.dis.blit(self.textures['S'], (sky_offset - WIDTH, 0))
        self.dis.blit(self.textures['S'], (sky_offset + WIDTH, 0))
        pg.draw.rect(self.dis, DARKGRAY, (0, HALF_HEIGHT, WIDTH, HALF_HEIGHT))

    def world(self, player_pos, player_angle):
        ray_casting(self.dis, player_pos, player_angle, self.textures)

    def fps(self, clock):
        display_fps = str(int(clock.get_fps()))
        render = self.font.render(display_fps, 0, RED)
        self.dis.blit(render, FPS_POS)

