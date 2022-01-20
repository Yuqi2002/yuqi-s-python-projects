# Yuqi Zhou
# pygame 

import pygame 

pygame.init()

screen=pygame.display.set_mode([500,500])

circleVol=[0]

# getting input of the game 
running=True
while running==True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False 
    if event.type==pygame.KEYDOWN:
        if event.key==pygame.K_left:
            circlePos[0]=circlePos[0]-.2
        if event.key==pygame.K_right:
            circlePos[0]=circlePos[0]+.2
        if event.key==pygame.K_UP:
            circleVol[0]-=1
        if event.key==pygame.K_DOWN:
            circleVol[0]+=1
# actions
    circlePos[0]=circlePos[0]+circle[0]
    circlePos[1]+=circleVOl[1]
    if (circlePos[0]>550):
        circleVol=[0]-=1
    if (circlePos[0]<25):
         circleVol=[0]+=-1
    screen.fill((255,255,255))
    pygame.draw.circle(screen,(0,0,255),(250,250),75)
    pygame.display.flip()
pygame.quit()


