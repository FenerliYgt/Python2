import pygame
import random

pygame.init()

GENİŞLİK,YÜKSEKLİK=700,800

pencere=pygame.display.set_mode((GENİŞLİK,YÜKSEKLİK))
HIZ=5
FPS=60
saat=pygame.time.Clock()

boy=pygame.image.load("C://Users//pc//Downloads//obesity.png")
boy_koordinat=boy.get_rect()
boy_koordinat.topleft=(50,50)
hamburger=pygame.image.load("C://Users//pc//Downloads//hamburger.png")
hamburger_koordinat=hamburger.get_rect()
hamburger_koordinat.topleft=(500,500)
durum=True
while durum:
    for etkinlik in pygame.event.get():
        if etkinlik.type==pygame.QUIT:
            durum=False
    tuş=pygame.key.get_pressed()
    if tuş[pygame.K_LEFT] and boy_koordinat.left>0:
        boy_koordinat.x-=HIZ
    elif tuş[pygame.K_RIGHT] and boy_koordinat.right<GENİŞLİK:
        boy_koordinat.x+=HIZ
    elif tuş[pygame.K_UP] and boy_koordinat.top>0:
        boy_koordinat.y-=HIZ
    elif tuş[pygame.K_DOWN] and boy_koordinat.bottom<YÜKSEKLİK:
        boy_koordinat.y+=HIZ
    pencere.fill((0,0,0))
    if boy_koordinat.colliderect(hamburger_koordinat):
        print("çocuk şişmanladı")
        hamburger_koordinat.x=random.randint(0,GENİŞLİK-32)
        hamburger_koordinat.y=random.randint(0,YÜKSEKLİK-32)
    pencere.blit(boy,boy_koordinat)
    pencere.blit(hamburger,hamburger_koordinat)
    pygame.display.update()
    saat.tick(FPS)



pygame.quit()