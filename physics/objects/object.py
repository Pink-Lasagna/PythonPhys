from ..engine import g, scale


import pygame as pg


class Object:
    velocity = 0
    inAir = True
    vectorMovement = pg.Vector2(0,0)
    def __init__(self, surface: pg.Surface, pos: pg.Vector2, weight: float, color: pg.Color, phys: bool):
        self.surface = surface
        self.pos = pos
        self.x = pos.x
        self.y = pos.y
        self.phys = phys
        self.weight = weight
        self.color = color

    def move(self, dt) -> None:
        self.pos.y += (((g*dt**2)/2)+self.velocity*dt)*scale
        print(self.pos.y)
        self.velocity += g*dt

    def applyForces(self, vector: pg.Vector2):

    def checkCollision(self, obj) -> bool:
        return False

    def draw(self) -> None:
        pass