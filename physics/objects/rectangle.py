from .object import Object


import pygame as pg


class Rectangle(Object):
    def __init__(self, surface: pg.Surface, pos: pg.Vector2, color: pg.Color, width: float, height: float, weight: float, phys: bool, vectorMovement: None):
        super().__init__(surface, pos, weight, color, phys, vectorMovement)
        self.width = width
        self.height = height

    def draw(self):
        pg.draw.rect(self.surface,self.color,pg.Rect(self.pos.x, self.pos.y,self.width, self.height))