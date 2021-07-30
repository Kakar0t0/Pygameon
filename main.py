import pygame
pygame.init()

#Création de la fenêtre du jeu
pygame.display.set_mode((800, 600))
pygame.display.set_caption("Pygameon World")

#Maintient de la fenêtre et fermeture
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()