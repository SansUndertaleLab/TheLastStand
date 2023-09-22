from UI import UI, Label
import sys
import pygame

pygame.init()

display = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

pygame.font.init()

title_font = pygame.font.SysFont("timesnewroman", 50)
menu_font = pygame.font.SysFont("calibri", 50)

i = 0

ui = UI()

ui.addElement(Label((0, 0), display, "The Last Stand: Farm, Cure, Survive", title_font))
game_version = "0.0.0.1"

while True:
    display.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_c]:
                pygame.quit()
                sys.exit()

    menu_buttons = [
        "New World",
        "Continue World"
    ]
    
    ui.render()
    pygame.display.update()