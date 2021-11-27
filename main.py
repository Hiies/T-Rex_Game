import pygame
import os

pygame.init()

tela_altura = 600
tela_largura = 1100
tela = pygame.display.set_mode((tela_largura,tela_altura))

dino_correndo = [pygame.image.load(os.path.join("Assets/Dino","DinoRun1.png")),pygame.image.load(os.path.join("Assets/Dino","DinoRun2.png"))]
dino_pulando = pygame.image.load(os.path.join("Assets/Dino","DinoJump.png"))
dino_abaixado = [pygame.image.load(os.path.join("Assets/Dino","DinoDuck1.png")),pygame.image.load(os.path.join("Assets/Dino","DinoDuck2.png"))]

cacto_pequeno = [pygame.image.load(os.path.join("Assets/Cactus","SmallCactus1.png")),pygame.image.load(os.path.join("Assets/Cactus","SmallCactus2.png"))
,pygame.image.load(os.path.join("Assets/Cactus","SmallCactus3.png"))]

cacto_grande = [pygame.image.load(os.path.join("Assets/Cactus","LargeCactus1.png")),pygame.image.load(os.path.join("Assets/Cactus","LargeCactus2.png"))
,pygame.image.load(os.path.join("Assets/Cactus","LargeCactus3.png"))]

passaro = [pygame.image.load(os.path.join("Assets/Bird","Bird1.png")),pygame.image.load(os.path.join("Assets/Bird","Bird2.png"))]

nuvens = pygame.image.load(os.path.join("Assets/Other","Cloud.png"))

fundo = pygame.image.load(os.path.join("Assets/Other","Track.png"))

def main():
    run = True
    tempo = pygame.time.Clock()

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
main()