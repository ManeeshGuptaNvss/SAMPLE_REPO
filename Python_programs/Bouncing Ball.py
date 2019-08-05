import pygame,time
#from pygame.locals import *
pygame.init()
#clock=pygame.time.Clock()
d=pygame.display.set_mode((600,600))
pygame.display.set_caption('Bouncing Ball')
x,y=500,10
done=True
direction='down'
while done:
    d.fill((0,0,0))
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            done=False
    if direction=='down':
       # pygame.fill((0,0,0))
        y+=25
        if y==560:
            direction='up'
    elif direction=='up':
        y-=25
        if y== 35:
            direction='down'
    pygame.draw.circle(d,(255,255,255),(x,y),12)
    #pygame.draw.rect(d,(255,0,0),(460,560,110,20))
    #pygame.display.flip()
    
    pygame.display.update()
    time.sleep(0.05)
    #clock.tick(20)
pygame.quit()
