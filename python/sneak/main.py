import pygame
import random


class Player:
    def __init__(self, pos=(1, 1)):
        self.segments = []
        self.segments.append(pos)
        self.dir = 0



class Scene:
    def __init__(self):
        for i in range(SIZE):
            for j in range(SIZE):
                tmp = []


SIZE = 20
WIDTH = 18
HEIGHT = 24
FPS = 60

pygame.init()
screen = pygame.display.set_mode((SIZE * WIDTH, SIZE * HEIGHT))
pygame.display.set_caption("Sneaky boy")
clock = pygame.time.Clock()

WHITE = (255, 255, 255)
BACK = (146, 204, 180)
SNAKE = (83, 96, 76)

player = Player()

running = True
while running:

    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                pass

    screen.fill(BACK)
    pygame.display.flip()
