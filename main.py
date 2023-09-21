from UI import Label
import sys
import pygame

pygame.init()

display = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

pygame.font.init()

title_font = pygame.font.SysFont("timesnewroman", 50)
menu_font = pygame.font.SysFont("calibri", 50)

i = 0

title = Label((0, 0), display, "The Last Stand: Farm, Cure, Survive", title_font)
game_version = "0.0.0.1"

while True:
    display.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            keys = pygame.key.get_pressed()

    menu_buttons = [
        "New World",
        "Continue World"
    ]

    title.render()
    
    pygame.display.update()