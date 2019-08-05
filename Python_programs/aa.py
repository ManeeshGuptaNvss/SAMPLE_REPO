import pygame
pygame.init()
win=pygame.display.set_mode((500,500))
pygame.display.set_caption('hello')
done=True
while done:
    for event in pygame.event.get():
        print(event)
