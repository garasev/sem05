import pygame

WIDTH = 1600
HEIGHT = 900
FPS = 60

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sosalo FPS")
clock = pygame.time.Clock()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
CYRCLE = (0, 255, 255)

text1 = 'Добро пожаловать в мою программу'
text2 = 'Sosalo FPS'
text3 = 'SPEED: slow'
text8 = 'SPEED: medium'
text4 = 'SPEED: fast'
text9 = 'SPEED: very fast'
text10 = 'SPEED: sonic'
text5 = 'FPS: 15'
text6 = 'FPS: 30'
text7 = 'FPS: 60'

timer = [10, 10, 7, 5, 4, 3]

running = True
part = 0
tick = 0
x = 300
x1 = 300
x2 = 300

while running:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                pass

    screen.fill(WHITE)
    if part == 0:
        font = pygame.font.Font('freesansbold.ttf', 50)
        textSurfaceObj = font.render(text1, True, BLACK)
        textRectObj = textSurfaceObj.get_rect()
        textRectObj.center = (700, 200)
        screen.blit(textSurfaceObj, textRectObj)
        font = pygame.font.Font('freesansbold.ttf', 100)
        textSurfaceObj = font.render(text2, True, BLACK)
        textRectObj = textSurfaceObj.get_rect()
        textRectObj.center = (1200, 400)
        screen.blit(textSurfaceObj, textRectObj)
    elif part == 1:
        font = pygame.font.Font('freesansbold.ttf', 50)
        textSurfaceObj = font.render(text3, True, BLACK)
        textRectObj = textSurfaceObj.get_rect()
        textRectObj.center = (800, 100)
        screen.blit(textSurfaceObj, textRectObj)

        font = pygame.font.Font('freesansbold.ttf', 50)
        textSurfaceObj = font.render(text5, True, BLACK)
        textRectObj = textSurfaceObj.get_rect()
        textRectObj.center = (100, 300)
        screen.blit(textSurfaceObj, textRectObj)

        font = pygame.font.Font('freesansbold.ttf', 50)
        textSurfaceObj = font.render(text6, True, BLACK)
        textRectObj = textSurfaceObj.get_rect()
        textRectObj.center = (100, 500)
        screen.blit(textSurfaceObj, textRectObj)

        font = pygame.font.Font('freesansbold.ttf', 50)
        textSurfaceObj = font.render(text7, True, BLACK)
        textRectObj = textSurfaceObj.get_rect()
        textRectObj.center = (100, 700)
        screen.blit(textSurfaceObj, textRectObj)

        x += 1

        if tick % 4 == 0:
            pygame.draw.circle(screen, CYRCLE, (x, 300), 70)
            x1 = x
        else:
            pygame.draw.circle(screen, CYRCLE, (x1, 300), 70)
        if tick % 2 == 0:
            pygame.draw.circle(screen, CYRCLE, (x, 500), 70)
            x2 = x
        else:
            pygame.draw.circle(screen, CYRCLE, (x2, 500), 70)
        pygame.draw.circle(screen, CYRCLE, (x, 700), 70)
    elif part == 2:
        font = pygame.font.Font('freesansbold.ttf', 50)
        textSurfaceObj = font.render(text8, True, BLACK)
        textRectObj = textSurfaceObj.get_rect()
        textRectObj.center = (800, 100)
        screen.blit(textSurfaceObj, textRectObj)

        font = pygame.font.Font('freesansbold.ttf', 50)
        textSurfaceObj = font.render(text5, True, BLACK)
        textRectObj = textSurfaceObj.get_rect()
        textRectObj.center = (100, 300)
        screen.blit(textSurfaceObj, textRectObj)

        font = pygame.font.Font('freesansbold.ttf', 50)
        textSurfaceObj = font.render(text6, True, BLACK)
        textRectObj = textSurfaceObj.get_rect()
        textRectObj.center = (100, 500)
        screen.blit(textSurfaceObj, textRectObj)

        font = pygame.font.Font('freesansbold.ttf', 50)
        textSurfaceObj = font.render(text7, True, BLACK)
        textRectObj = textSurfaceObj.get_rect()
        textRectObj.center = (100, 700)
        screen.blit(textSurfaceObj, textRectObj)

        x += 3

        if tick % 4 == 0:
            pygame.draw.circle(screen, CYRCLE, (x, 300), 70)
            x1 = x
        else:
            pygame.draw.circle(screen, CYRCLE, (x1, 300), 70)
        if tick % 2 == 0:
            pygame.draw.circle(screen, CYRCLE, (x, 500), 70)
            x2 = x
        else:
            pygame.draw.circle(screen, CYRCLE, (x2, 500), 70)
        pygame.draw.circle(screen, CYRCLE, (x, 700), 70)
    elif part == 3:
        font = pygame.font.Font('freesansbold.ttf', 50)
        textSurfaceObj = font.render(text4, True, BLACK)
        textRectObj = textSurfaceObj.get_rect()
        textRectObj.center = (800, 100)
        screen.blit(textSurfaceObj, textRectObj)

        font = pygame.font.Font('freesansbold.ttf', 50)
        textSurfaceObj = font.render(text5, True, BLACK)
        textRectObj = textSurfaceObj.get_rect()
        textRectObj.center = (100, 300)
        screen.blit(textSurfaceObj, textRectObj)

        font = pygame.font.Font('freesansbold.ttf', 50)
        textSurfaceObj = font.render(text6, True, BLACK)
        textRectObj = textSurfaceObj.get_rect()
        textRectObj.center = (100, 500)
        screen.blit(textSurfaceObj, textRectObj)

        font = pygame.font.Font('freesansbold.ttf', 50)
        textSurfaceObj = font.render(text7, True, BLACK)
        textRectObj = textSurfaceObj.get_rect()
        textRectObj.center = (100, 700)
        screen.blit(textSurfaceObj, textRectObj)

        x += 5

        if tick % 4 == 0:
            pygame.draw.circle(screen, CYRCLE, (x, 300), 70)
            x1 = x
        else:
            pygame.draw.circle(screen, CYRCLE, (x1, 300), 70)
        if tick % 2 == 0:
            pygame.draw.circle(screen, CYRCLE, (x, 500), 70)
            x2 = x
        else:
            pygame.draw.circle(screen, CYRCLE, (x2, 500), 70)
        pygame.draw.circle(screen, CYRCLE, (x, 700), 70)
    elif part == 4:
        font = pygame.font.Font('freesansbold.ttf', 50)
        textSurfaceObj = font.render(text9, True, BLACK)
        textRectObj = textSurfaceObj.get_rect()
        textRectObj.center = (800, 100)
        screen.blit(textSurfaceObj, textRectObj)

        font = pygame.font.Font('freesansbold.ttf', 50)
        textSurfaceObj = font.render(text5, True, BLACK)
        textRectObj = textSurfaceObj.get_rect()
        textRectObj.center = (100, 300)
        screen.blit(textSurfaceObj, textRectObj)

        font = pygame.font.Font('freesansbold.ttf', 50)
        textSurfaceObj = font.render(text6, True, BLACK)
        textRectObj = textSurfaceObj.get_rect()
        textRectObj.center = (100, 500)
        screen.blit(textSurfaceObj, textRectObj)

        font = pygame.font.Font('freesansbold.ttf', 50)
        textSurfaceObj = font.render(text7, True, BLACK)
        textRectObj = textSurfaceObj.get_rect()
        textRectObj.center = (100, 700)
        screen.blit(textSurfaceObj, textRectObj)

        x += 7

        if tick % 4 == 0:
            pygame.draw.circle(screen, CYRCLE, (x, 300), 70)
            x1 = x
        else:
            pygame.draw.circle(screen, CYRCLE, (x1, 300), 70)
        if tick % 2 == 0:
            pygame.draw.circle(screen, CYRCLE, (x, 500), 70)
            x2 = x
        else:
            pygame.draw.circle(screen, CYRCLE, (x2, 500), 70)
        pygame.draw.circle(screen, CYRCLE, (x, 700), 70)
    elif part == 5:
        font = pygame.font.Font('freesansbold.ttf', 50)
        textSurfaceObj = font.render(text10, True, BLACK)
        textRectObj = textSurfaceObj.get_rect()
        textRectObj.center = (800, 100)
        screen.blit(textSurfaceObj, textRectObj)

        font = pygame.font.Font('freesansbold.ttf', 50)
        textSurfaceObj = font.render(text5, True, BLACK)
        textRectObj = textSurfaceObj.get_rect()
        textRectObj.center = (100, 300)
        screen.blit(textSurfaceObj, textRectObj)

        font = pygame.font.Font('freesansbold.ttf', 50)
        textSurfaceObj = font.render(text6, True, BLACK)
        textRectObj = textSurfaceObj.get_rect()
        textRectObj.center = (100, 500)
        screen.blit(textSurfaceObj, textRectObj)

        font = pygame.font.Font('freesansbold.ttf', 50)
        textSurfaceObj = font.render(text7, True, BLACK)
        textRectObj = textSurfaceObj.get_rect()
        textRectObj.center = (100, 700)
        screen.blit(textSurfaceObj, textRectObj)

        x += 9

        sonic = pygame.image.load('sonic.png')

        if tick % 4 == 0:
            screen.blit(sonic, (x, 200))
            x1 = x
        else:
            screen.blit(sonic, (x1, 200))
        if tick % 2 == 0:
            screen.blit(sonic, (x, 400))
            x2 = x
        else:
            screen.blit(sonic, (x2, 400))
        screen.blit(sonic, (x, 600))
    elif part == -1:
        font = pygame.font.Font('freesansbold.ttf', 100)
        textSurfaceObj = font.render(text2, True, BLACK)
        textRectObj = textSurfaceObj.get_rect()
        textRectObj.center = (1200, 400)
        screen.blit(textSurfaceObj, textRectObj)
    if part != -1 and tick // FPS == timer[part]:
        part += 1
        x = 300
        x1 = 300
        x2 = 300
        tick = 0
        if len(timer) == part:
            part = -1
    tick += 1
    pygame.display.flip()