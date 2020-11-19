import pygame
# Экран
pygame.init()
window = pygame.display.set_mode((640,360))
pygame.display.set_caption("DRaka 3d")
# Переменные
background=pygame.image.load('phone.jpg')
deadpoolr=pygame.image.load('deadpoolr.png')
deadpooll=pygame.image.load('deadpooll.png')
x=5
y=295
widht=24
height=41
speed=5
jumping=False
jump=10
run=True
hp=100
rl=1

def hitreg(a,b):
    a=b    

def drawing():    
    window.blit(background,(0,0))
    pygame.draw.rect(window,(0,0,0),(10,10,105,20),4)
    pygame.draw.rect(window,(255,0,0),(13,13,hp,15))
    if rl==1:
        window.blit(deadpoolr,(x,y))
    else:
        window.blit(deadpooll,(x,y))
    pygame.display.update()
def drawing1():
    font=pygame.font.SysFont("comicsansms",30)
    text=font.render('Game Over',True,(255,255,0))
    textf=font.render('press F to restart',True,(255,255,0))
    window.blit(text,[230,100])
    window.blit(textf,[190,150])
    pygame.display.update()
while run:
    pygame.time.delay(30)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
    keys=pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x>5:
        x-=speed
        rl=0
    if keys[pygame.K_RIGHT]and x<640-widht-5:
        x+=speed
        rl=1
    if not(jumping):
        if keys[pygame.K_SPACE]:
            jumping=True
            hp-=70
    else:
        if jump>=-10:
            if jump<0:
                y+=(jump**2)//8
            else:   
                y-=(jump**2)//8
            jump-=1
        else:
            jumping=False
            jump=10
    if hp<1:
        rip=True
        while rip:
            drawing1()
            pygame.time.delay(30)
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    rip=False
            keys=pygame.key.get_pressed()
            if keys[pygame.K_f]:
                x=5
                y=295
                hp=100
                rl=1
                rip=False
    drawing()

pygame.quit()
