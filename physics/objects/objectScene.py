from .object import Object


class ObjectScene:
    def __init__(self, size: tuple, dt, *obj: Object):
        self.size = size
        self.obj = obj
        self.dt = dt

    def updateTime(self, dt):
        self.dt = dt
  
    def calcObjectScene(self):
        for i in self.obj:
            for j in self.obj:
                if i==j:
                    continue
                if i.checkCollision(j):
                    print("lol")
            if i.phys==True: i.move(self.dt)
            i.draw()