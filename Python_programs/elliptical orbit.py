import pygame,math,time
pygame.init()
screen=pygame.display.set_mode((700,500))
pygame.display.set_caption('Elliptical Orbit')
done=True

while done:
    #pygame.time.delay(50)
    for event in pygame.event.get():
        if event.type== pygame.QUIT:
            done= False
    x,y=250,100
    for i in range(360):
        x1=int(math.sin(i*math.pi/180)*x)+300
        y1=int(math.cos(i*math.pi/180)*y)+150
        screen.fill((0,0,0))
        pygame.draw.circle(screen,(0,0,255),(300,150),30)
        pygame.draw.ellipse(screen,(255,0,0),(50,50,500,200),10)
        pygame.draw.circle(screen,(255,255,255),(x1,y1),15)
        pygame.display.update()
        #time.sleep(0.2)
        #pygame.display.flip()
        
pygame.quit()
