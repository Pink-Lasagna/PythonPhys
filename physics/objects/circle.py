from .object import Object
from .rectangle import Rectangle
from .. import utils
import math
import pygame as pg


class Circle(Object):
    def __init__(self, surface: pg.Surface, pos: pg.Vector2, weight: float, color: pg.Color, r: float, phys: bool):
        super().__init__(surface, pos, weight, color, phys)
        self.r = r

    def move(self, dt):
        super().move(dt)

    def draw(self):
        pg.draw.circle(self.surface,self.color,self.pos,self.r)

    def checkCollision(self, obj: Object):
        if type(obj) == Rectangle:
            clPoint = utils.clampPointInRect(self.pos,obj)
            if (clPoint.x-self.pos.x)**2 + (clPoint.y-self.pos.y)**2 < self.r or self.pos == clPoint:
                return True
        return False