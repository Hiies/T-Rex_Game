import pygame
import os
import random

from pygame.constants import KEYDOWN

pygame.init()

tela_largura = 1100
tela_altura = 600
tela = pygame.display.set_mode((tela_largura, tela_altura))

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

nuvem = pygame.image.load(os.path.join("Assets/Other", "Cloud.png"))

fundo = pygame.image.load(os.path.join("Assets/Other", "Track.png"))


class Dino:
    x_pos = 80
    y_pos = 310
    y_pos_abaixado = 340
    pulando_vel_const = 8.5

    def __init__(self):
        self.dino_abaixado_img = abaixado
        self.dino_correndo_img = correndo
        self.dino_pulando_img = pulando

        self.dino_abaixado = False
        self.dino_correndo = True
        self.dino_pulando = False

        self.step_index = 0
        self.pulando_vel = self.pulando_vel_const
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
            self.dino_correndo = False
            self.dino_pulando = True

        elif userInput[pygame.K_DOWN] and not self.dino_pulando:
            self.dino_abaixado = True
            self.dino_correndo = False
            self.dino_pulando = False
        elif not (self.dino_pulando or userInput[pygame.K_DOWN]):
            self.dino_abaixado = False
            self.dino_correndo = True
            self.dino_pulando = False

    def abaixado(self):
        self.image = self.dino_abaixado_img[self.step_index // 5]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.x_pos
        self.dino_rect.y = self.y_pos_abaixado
        self.step_index += 1

    def correndo(self):
        self.image = self.dino_correndo_img[self.step_index // 5]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.x_pos
        self.dino_rect.y = self.y_pos
        self.step_index += 1

    def pulando(self):
        self.image = self.dino_pulando_img
        if self.dino_pulando:
            self.dino_rect.y -= self.pulando_vel * 4
            self.pulando_vel -= 0.8
            if self.pulando_vel < - self.pulando_vel_const:
                self.dino_pulando = False
                self.pulando_vel = self.pulando_vel_const

    def draw(self, tela):
        tela.blit(self.image, (self.dino_rect.x, self.dino_rect.y))


class Nuvem:
    def __init__(self):
        self.x = tela_largura + random.randint(800, 1000)
        self.y = random.randint(50, 100)
        self.image = nuvem
        self.largura = self.image.get_width()

    def update(self):
        self.x -= game_speed
        if self.x < - self.largura:
            self.x = tela_largura + random.randint(2500, 3000)
            self.y = random.randint(50, 100)
        pass

    def draw(self, tela):
        tela.blit(self.image, (self.x, self.y))


class Obstaculo:
    def __init__(self, image, type):
        self.image = image
        self.type = type
        self.rect = self.image[self.type].get_rect()
        self.rect.x = tela_largura

    def update(self):
        self.rect.x -= game_speed
        if self.rect.x < - self.rect.width:
            obstaculos.pop()

    def draw(self, tela):
        tela.blit(self.image[self.type], self.rect)


class SmallCactus(Obstaculo):
    def __init__(self, image):
        self.type = random.randint(0, 2)
        super().__init__(image, self.type)
        self.rect.y = 325


class LargeCactus(Obstaculo):
    def __init__(self, image):
        self.type = random.randint(0, 2)
        super().__init__(image, self.type)
        self.rect.y = 300


class Passaro(Obstaculo):
    def __init__(self, image):
        self.type = 0
        super().__init__(image, self.type)
        self.rect.y = 250
        self.index = 0

    def draw(self, tela):
        if self.index >= 9:
            self.index = 0
        tela.blit(self.image[self.index//5], self.rect)
        self.index += 1


def main():
    global game_speed, x_pos_bg, y_pos_bg, pontos, obstaculos
    run = True
    relogio = pygame.time.Clock()
    player = Dino()
    nuvem = Nuvem()
    game_speed = 20
    pontos = 0
    font = pygame.font.Font('freesansbold.ttf', 20)
    x_pos_bg = 0
    y_pos_bg = 380
    obstaculos = []
    death_count = 0

    def pontuacao():
        global pontos, game_speed
        pontos += 1
        if pontos % 100 == 0:
            game_speed += 1

        text = font.render("Pontos: " + str(pontos), True, (0, 0, 0))
        textRect = text.get_rect()
        textRect.center = (1000, 40)
        tela.blit(text, textRect)

    def background():
        global x_pos_bg, y_pos_bg
        image_largura = fundo.get_width()
        tela.blit(fundo, (x_pos_bg, y_pos_bg))
        tela.blit(fundo, (image_largura + x_pos_bg, y_pos_bg))
        if x_pos_bg <= -image_largura:
            tela.blit(fundo, (image_largura + x_pos_bg, y_pos_bg))
            x_pos_bg = 0
        x_pos_bg -= game_speed

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                quit()
        userInput = pygame.key.get_pressed()
        tela.fill((255, 255, 255))

        player.draw(tela)
        player.update(userInput)

        if len(obstaculos) == 0:
            if random.randint(0, 2) == 0:
                obstaculos.append(SmallCactus(cacto_pequeno))
            elif random.randint(0, 2) == 1:
                obstaculos.append(LargeCactus(cacto_grande))
            elif random.randint(0, 2) == 2:
                obstaculos.append(Passaro(passaro))

        for obstaculo in obstaculos:
            obstaculo.draw(tela)
            obstaculo.update()
            if player.dino_rect.colliderect(obstaculo.rect):
                pygame.time.delay(500)
                death_count += 1
                menu(death_count)

        nuvem.draw(tela)
        nuvem.update()

        background()

        pontuacao()

        relogio.tick(30)
        pygame.display.update()


def menu(death_count):
    global pontos
    run = True
    while run:
        tela.fill((255, 255, 255))
        font = pygame.font.Font('freesansbold.ttf', 30)

        if death_count == 0:
            text = font.render(
                "Pressione qualquer tecla para começar", True, (0, 0, 0))
        elif death_count > 0:
            text = font.render(
                "Pressione qualquer tecla para recomeçar", True, (0, 0, 0))
            score = font.render("Sua pontuação: " +
                                str(pontos), True, (0, 0, 0))
            scoreRect = score.get_rect()
            scoreRect.center = (tela_largura // 2, tela_altura // 2 + 50)
            tela.blit(score, scoreRect)
        textRect = text.get_rect()
        textRect.center = (tela_largura // 2, tela_altura // 2)
        tela.blit(text, textRect)
        tela.blit(correndo[0], (tela_largura // 2 -
                                20, tela_altura // 2 - 140))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                main()


menu(death_count=0)
