from ..engine import g, scale, screen


import pygame as pg


class Object:
    vectorMovement = pg.Vector2(0,0)
    def __init__(self, surface: pg.Surface, pos: pg.Vector2, weight: float, color: pg.Color, phys: bool):
        self.surface = surface
        self.pos = pos
        self.x = pos.x
        self.y = pos.y
        self.phys = phys
        self.weight = weight
        self.color = color

    def calcForces(self, dt) -> None:
        self.vectorMovement.y -= g*dt

    def applyForces(self):
        self.pos.x += self.vectorMovement.x
        self.pos.y -= self.vectorMovement.y
        

    def checkCollision(self, obj) -> bool:
        return False

    def draw(self) -> None:
        pass

    def onCollision(self):
        pass