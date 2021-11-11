import pygame
from pygame.sprite import Sprite
from .constantes import ALTO, ANCHO, FPS
import random


class Player(Sprite):
    def __init__(self, pantalla, **Kwargs):
        super().__init__()
        self.vidas = 3
        self.pantalla = pantalla
        self.explosion = pygame.sprite.Group()
        self.colision = False
        self.image = pygame.image.load("resources/img/playerShip1_orange.png").convert_alpha()
        self.rect = self.image.get_rect(**Kwargs)
        self.posicion_inicial = Kwargs
        self.speedx = 0


    def reset(self):
        self.rect = self.image.get_rect(**self.posicion_inicial)

    def update(self):
        self.speedx = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.speedx = -8
        if keystate[pygame.K_RIGHT]:
            self.speedx = 8
        self.rect.x += self.speedx
        if self.rect.right > ANCHO:
            self.rect.right = ANCHO
        if self.rect.left < 0:
            self.rect.left = 0
        if self.colision:
            explosion = Explosion(self.pantalla, center=(self.rect.centerx, self.rect.centery))
            self.explosion.add(explosion)
            self.colision = False

    
    def draw(self):
        self.pantalla.blit(self.image, self.rect)
        for self.explotado in self.explosion:
            self.explotado.update()
            self.explotado.draw()
            if self.explotado.imagenActual == len(self.explotado.listaImagenes) - 1:
                self.explotado.kill()
    
       
        

class Meteoritos(Sprite):
    def __init__(self, pantalla):
        super().__init__()  
        self.pantalla = pantalla
        self.image = pygame.image.load("resources/img/meteorBrown_med1.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(ANCHO - self.rect.width)
        self.rect.y = random.randrange(-100, -40)
        self.speedy = random.randrange(1, 8)
        self.speedx = random.randrange(-3, 3)
        self.colision = False
        self.explosion = pygame.sprite.Group()

    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.top > ALTO or self.rect.right < 0 or self.rect.left > ANCHO:
            self.rect.x = random.randrange(ANCHO - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.speedy = random.randrange(1, 5)

    def comprobar_colision(self, player):
        if not self.colision:
            if self.rect.right >= player.rect.left and self.rect.left <= player.rect.right and \
            self.rect.bottom >= player.rect.top and self.rect.top <= player.rect.bottom: 
                player.vidas -= 1
                explosion = Explosion(self.pantalla, center=(self.rect.centerx, self.rect.centery))
                self.explosion.add(explosion)
                self.rect.top > ALTO or self.rect.right < 0 or self.rect.left > ANCHO
                self.rect.x = random.randrange(ANCHO - self.rect.width)
                self.rect.y = random.randrange(-100, -40)
                self.speedy = random.randrange(1, 5)
                self.colision = True
                player.colision = True

    def draw(self):
        self.pantalla.blit(self.image, self.rect)
        for self.explotado in self.explosion:
            self.explotado.update()
            self.explotado.draw()
            if self.explotado.imagenActual == len(self.explotado.listaImagenes) - 1:
                self.explotado.kill()
            

class Explosion(Sprite):
    def __init__(self, pantalla, **Kwargs):
        super().__init__()
        self.pantalla = pantalla
        self.listaImagenes = []
        for i in range(8):
            self.listaImagenes.append(pygame.image.load(f"resources/img/SonicExplosion0{i}.png").convert_alpha())
        self.imagenActual = 0
        self.image = self.listaImagenes[self.imagenActual]
        self.rect = self.image.get_rect(**Kwargs)

    def update(self):
        self.image = self.listaImagenes[self.imagenActual]
        if self.imagenActual < len(self.listaImagenes) - 1:
            self.imagenActual += 1

    def draw(self):
        self.pantalla.blit(self.image, self.rect)


class Marcador(Sprite):

    def __init__(self, x, y, fichero_letra, tamanno, color):
        super().__init__()
        self._texto = ""
        self.x = x
        self.y = y
        self.color = color 
        self.fuente = pygame.font.Font(f"resources/fonts/{fichero_letra}", tamanno)
        self.image = self.fuente.render(self._texto, True, self.color)
        self.rect = self.image.get_rect(x=self.x, y=self.y)

    def update(self):
        self.image = self.fuente.render(self._texto, True, self.color)
        self.rect = self.image.get_rect(x=self.x, y=self.y)

    @property
    def texto(self):
        return self._texto

    @texto.setter
    def texto(self, valor):
        self._texto = str(valor)

       
    