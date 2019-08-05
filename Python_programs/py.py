import pygame
pygame.init()
pygame.display.set_caption('Hello World')
screen=pygame.display.set_mode((700,500))
done = False
x,y,width,height,vel=50,50,40,60,5
while not done:
    pygame.time.delay(50)
    for event in pygame.event.get():
        if event.type== pygame.QUIT:
            done=True
    keys=pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x>vel:
        x-=vel
    elif keys[pygame.K_RIGHT] and x < 500-vel-width:
        x+=vel
    elif keys[pygame.K_UP] and y>vel:
        y-=vel
    elif keys[pygame.K_DOWN] and y< 500-height-vel:
        y+=vel
    screen.fill((0,0,0))
    pygame.draw.rect(screen,(255,0,0),(x,y,width,height))
    pygame.display.update()
pygame.quit()
    
