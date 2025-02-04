import sys
import pygame
from buttons import Button

pygame.init()

width, height = 1500, 700
running = True
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('df')
green_button = Button(width/2-(252/2), 100, 252, 211, '', 'kaspersky.png', 'mcaffee.png')

while running:
    for event in pygame.event.get():
        green_button.handle_event(event)
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.USEREVENT:
            pass
    green_button.check_hover(pygame.mouse.get_pos())
    green_button.draw_button(screen)
    pygame.display.flip()
pygame.quit()
sys.exit()