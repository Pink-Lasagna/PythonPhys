import pygame as pg
import physics.objects as ph

def main():
    dt = 0
    t = 0
    pg.init()
    screen = pg.display.set_mode((1280,720))
    clock = pg.time.Clock()
    

    c1 = ph.Circle(screen, pg.Vector2(640,360),2,"red",10, True)
    r1 = ph.Rectangle(screen, pg.Vector2(100,600), "black",1000,100,10,False)
    phys = ph.ObjectScene((1280,720), dt,c1,r1)

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
        
        screen.fill("white")
        

        phys.updateTime(dt)
        phys.calcObjectScene()

        
        pg.display.flip()

        dt = clock.tick(75)/1000
        t+=dt


if __name__=="__main__":
    main()