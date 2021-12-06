from typing_extensions import get_args
import pygame

pygame.init()
screen = pygame.display.set_mode((1000, 1000))
clock = pygame.time.Clock
running = True

while running:
    clock.tick(10)
for event in pygame.event.get():
    if event.type == pygame.QUIT:
        running = False
screen.fill((255, 0, 0))  # (R,G,B)
pygame: quit()
