import pygame

pygame.init()
window=pygame.display.set_mode((500,500))
pygame.display.set_caption('First Pygame')

x,y=10,10
width,height=30,40
run= True
while run:
    pygame.time.delay(100)
    
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
    keys=pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x> 10:
        x-=5
    if keys[pygame.K_RIGHT] and x<500-width:
        x+=5
    if keys[pygame.K_UP] and y>10:
        y-=5
    if keys[pygame.K_DOWN] and y < 500- height :
        y+=5
    window.fill((255,255,255))
    pygame.draw.rect(window,(255,0,0),(x,y,width,height))
    pygame.display.update()
pygame.quit() 
