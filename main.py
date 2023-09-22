from UI import UI, Label, Button
import sys
import pygame

pygame.init()

display = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
# display= pygame.display.set_mode((300, 300))

pygame.font.init()

title_font = pygame.font.SysFont("timesnewroman", 50)
menu_font = pygame.font.SysFont("calibri", 50)
mini_font = pygame.font.SysFont("calibri", 20)

i = 0

ui = UI()

ui.addElement(Label((0, 0), display, "The Last Stand: Farm, Cure, Survive", title_font))
game_version = "0.0.0.1"

print_c = lambda msg : (lambda : print(msg))

ui.addElement(Label((0, display.get_height() - 20), display, game_version, mini_font))

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
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_clicked_pos = pygame.mouse.get_pos()
            ui.clicked(mouse_clicked_pos)
    
    ui.update_buttons()
    ui.render()
    pygame.display.update()