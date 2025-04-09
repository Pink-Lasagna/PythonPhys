from .object import Object


import pygame as pg


class Circle(Object):
    def __init__(self, surface: pg.Surface, pos: pg.Vector2, weight: float, color: pg.Color, r: float, phys: bool):
        super().__init__(surface, pos, weight, color, phys)
        self.r = r

    def move(self, dt):
        super().move(dt)

    def draw(self):
        pg.draw.circle(self.surface,self.color,self.pos,self.r)