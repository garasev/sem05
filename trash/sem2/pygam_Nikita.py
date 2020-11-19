import pygame
import random
import time
import math
pygame.init()

window_size = (800,800)

rect_1 = ((0,0),(800, 400))
rect_2 = ((0,400), (800,400))

rect_1_color = (0, 0, 128)
rect_2_color = (34, 139, 34)
white = (255, 255, 255)
black = (0, 0, 0)
sun = (255, 215, 0)
sun_a = (253, 233, 16)
moon = (125, 132, 113)
moon_a = (209, 209, 203)
# Рисуется звезда

def pause():
    time.sleep(1)
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption("Анимация")

ap_pos1 = (int(600 + random.random() * 40), int(470 + random.random() * 40))
ap_pos2 = (int(600 + random.random() * 40), int(470 + random.random() * 40))
ap_pos3 = (int(600 + random.random() * 40), int(470 + random.random() * 40))
ap_pos4 = (int(600 + random.random() * 40), int(470 + random.random() * 40))
i = 0
done = False
clock = pygame.time.Clock()
# text setting
while done == False:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    screen.fill(white)
    # sun moon
    pygame.draw.rect(screen, rect_1_color, rect_1, 0)
    pygame.draw.circle(screen, sun_a, (400 + int(300 * math.cos(i / 48)),
                                     400 + int(300 * math.sin(i / 48))), 55)
    pygame.draw.circle(screen, sun, (400 + int(300 * math.cos(i / 48)),
                                     400 + int(300 * math.sin(i / 48))), 45)
    pygame.draw.circle(screen, moon, (400 + int(300 * math.cos(3.14 + i / 48)),
                                     400 + int(300 * math.sin(3.14 + i / 48))), 50)
    pygame.draw.circle(screen, moon_a, (400 + int(280 * math.cos(3.14 + i / 48)),
                                     400 + int(280 * math.sin(3.14 + i / 48))), 10)
    pygame.draw.circle(screen, moon_a, (400 + int(310 * math.cos(3.20 + i / 48)),
                                     400 + int(310 * math.sin(3.20 + i / 48))), 20)
    pygame.draw.circle(screen, moon_a, (400 + int(300 * math.cos(3.05 + i / 48)),
                                     400 + int(300 * math.sin(3.05 + i / 48))), 15)
    pygame.draw.rect(screen, rect_2_color, rect_2, 0)

    # home
    pygame.draw.rect(screen, (92, 58, 41), ((50, 550), (200, 80)))
    pygame.draw.polygon(screen, (166, 13, 16), ((250, 550), (290, 510),
                                               (270, 470)))
    pygame.draw.polygon(screen, (212, 17, 20), ((50, 550), (70, 470),
                                               (270, 470), (250, 550)))
    pygame.draw.polygon(screen, (92, 58, 41), ((250, 630), (290, 590),
                                               (290, 510), (250, 550)))
    pygame.draw.rect(screen, sun_a, ((80, 570), (40, 40)))
    pygame.draw.rect(screen, sun_a, ((180, 570), (40, 40)))
    pygame.draw.rect(screen, black, ((50, 550), (200, 80)), 2)
    pygame.draw.line(screen, black, (250, 630), (290, 590), 2)
    pygame.draw.line(screen, black, (290, 590), (290, 510), 2)
    pygame.draw.line(screen, black, (290, 510), (250, 550), 2)
    pygame.draw.line(screen, black, (50, 550), (70, 470), 2)
    pygame.draw.line(screen, black, (70, 470), (270, 470), 2)
    pygame.draw.line(screen, black, (270, 470), (250, 550), 2)
    pygame.draw.line(screen, black, (290, 510), (270, 470), 2)
    pygame.draw.rect(screen, black, ((80, 570), (40, 40)), 2)
    pygame.draw.rect(screen, black, ((180, 570), (40, 40)), 2)

    pygame.draw.rect(screen, (92, 58, 41), ((600, 500), (20, 100)))
    pygame.draw.circle(screen, (0, 77, 0), (610, 480), 50)
    pygame.draw.circle(screen, (212, 17, 20), (ap_pos1), 5)
    pygame.draw.circle(screen, (212, 17, 20), (ap_pos2), 5)
    pygame.draw.circle(screen, (212, 17, 20), (ap_pos3), 5)
    pygame.draw.circle(screen, (212, 17, 20), (ap_pos4), 5)
    
    # clock
    pygame.draw.circle(screen, white, (400, 400), 97)
    pygame.draw.circle(screen, black, (400, 400), 100, 6)
    pygame.draw.line(screen, black, (400, 320), (400, 300), 6)
    pygame.draw.line(screen, black, (400, 480), (400, 500), 6)
    pygame.draw.line(screen, black, (300, 400), (320, 400), 6)
    pygame.draw.line(screen, black, (500, 400), (480, 400), 6)

    pygame.draw.line(screen, black, (330, 330), (344, 344), 5)
    pygame.draw.line(screen, black, (470, 470), (456, 456), 5)
    pygame.draw.line(screen, black, (330, 470), (344, 456), 5)
    pygame.draw.line(screen, black, (470, 330), (456, 344), 5)

    pygame.draw.line(screen, black, (400, 400), (400 + 50 * math.cos(1.57 + i / 24),
                                                 400 + 50 * math.sin(1.57 + i / 24)), 10)
    pygame.draw.line(screen, black, (400, 400), (400 + 75 * math.cos(1.57 + i / 2),
                                                 400 + 75 * math.sin(1.57 + i / 2)), 8)
    pygame.display.update()
    i += 1
    clock.tick(30)

pygame.quit()
