import pygame,math
pygame.init()
win=pygame.display.set_mode((700,500))
done=3
while done:
    for i in pygame.event.get():
        if i.type is pygame.QUIT:
            done =False
    x,y=250,100
    for i in range(360):
        x1=int(math.sin(i*math.pi/180)*x)+300
        y1=int(math.cos(i*math.pi/180)*y)+150
        win.fill((0,0,0))
        pygame.draw.circle(win,(0,200,0),(300,150),30)
        pygame.draw.ellipse(win,(0,0,200),(50,50,500,200),3)
        pygame.draw.circle(win,(0,200,0),(x1,y1),20)
        pygame.display.update()
pygame.quit()
    
