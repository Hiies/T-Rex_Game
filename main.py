import pygame
import os
from sys import exit

pygame.init()

tela = pygame.display.set_mode((1100, 600))

correndo = [pygame.image.load(os.path.join(
    "Assets/Dino", "DinoRun1.png")), pygame.image.load(os.path.join("Assets/Dino", "DinoRun2.png"))]

pulando = pygame.image.load(os.path.join("Assets/Dino", "DinoJump.png"))

abaixado = [pygame.image.load(os.path.join(
    "Assets/Dino", "DinoDuck1.png")), pygame.image.load(os.path.join("Assets/Dino", "DinoDuck2.png"))]

cacto_pequeno = [pygame.image.load(os.path.join("Assets/Cactus", "SmallCactus1.png")), pygame.image.load(os.path.join(
    "Assets/Cactus", "SmallCactus2.png")), pygame.image.load(os.path.join("Assets/Cactus", "SmallCactus3.png"))]

cacto_grande = [pygame.image.load(os.path.join("Assets/Cactus", "LargeCactus1.png")), pygame.image.load(os.path.join(
    "Assets/Cactus", "LargeCactus2.png")), pygame.image.load(os.path.join("Assets/Cactus", "LargeCactus3.png"))]

passaro = [pygame.image.load(os.path.join("Assets/Bird", "Bird1.png")),
           pygame.image.load(os.path.join("Assets/Bird", "Bird2.png"))]

nuvens = pygame.image.load(os.path.join("Assets/Other", "Cloud.png"))

fundo = pygame.image.load(os.path.join("Assets/Other", "Track.png"))


class Dino:
    x_pos = 80
    y_pos = 310
    y_pos_abaixado = 340
    pulando_vel = 8.5

    def __init__(self):
        self.dino_abaixado_img = abaixado
        self.dino_correndo_img = correndo
        self.dino_pulando_img = pulando

        self.dino_abaixado = False
        self.dino_correndo = True
        self.dino_pulando = False

        self.step_index = 0
        self.pulando_vel = self.pulando_vel
        self.image = self.dino_correndo_img[0]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.x_pos
        self.dino_rect.y = self.y_pos

    def update(self, userInput):
        if self.dino_abaixado:
            self.abaixado()
        if self.dino_correndo:
            self.correndo()
        if self.dino_pulando:
            self.pulando()

        if self.step_index >= 10:
            self.step_index = 0

        if userInput[pygame.K_UP] and not self.dino_pulando:
            self.dino_abaixado = False
            self.dino_corendo = False
            self.dino_pulando = True
        elif userInput[pygame.K_DOWN] and not self.dino_pulando:
            self.dino_abaixado = True
            self.dino_corendo = False
            self.dino_pulando = False
        elif not (self.dino_pulando or userInput[pygame.K_DOWN]):
            self.dino_abaixado = False
            self.dino_corendo = True
            self.dino_pulando = False

    def abaixado(self):
        self.image = self.abaixado_img[self.step_index // 5]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.x_pos
        self.dino_rect.y = self.y_pos
        self.step_index += 1

    def correndo(self):
        self.image = self.dino_correndo_img[self.step_index // 5]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.x_pos
        self.dino_rect.y = self.y_pos
        self.step_index += 1

    def pulando(self):
        self.image = self.dino_correndo_img[self.step_index // 5]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.x_pos
        self.dino_rect.y = self.y_pos
        self.step_index += 1

    def draw(self, tela):
        tela.blit(self.image, (self.dino_rect.x, self.dino_rect.y))


def main():
    run = True
    relogio = pygame.time.Clock()
    player = Dino()
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        userInput = pygame.key.get_pressed()
        tela.fill((255, 255, 255))
        player.draw(tela)
        player.update(userInput)

        relogio.tick(30)
        pygame.display.update()


main()
