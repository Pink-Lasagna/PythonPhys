import pygame as pg
from . import objects
def clamp(n: float, smallest: float, largest: float): return max(smallest, min(n, largest))

def clampVector2(n: pg.Vector2, smallest: pg.Vector2, largest: pg.Vector2): return pg.Vector2(clamp(n.x, smallest.x, largest.x),clamp(n.y,smallest.y,largest.y)) 

def clampPointInRect(n: pg.Vector2, sq: objects.rectangle.Rectangle): return clampVector2(n, pg.Vector2(sq.x,sq.y),pg.Vector2(sq.x+sq.width,sq.y+sq.height))