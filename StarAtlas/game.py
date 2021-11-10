import pygame
from .constantes import ALTO, ANCHO, FPS
from StarAtlas.escenas import Portada, Partida, Records




class Game():
    pygame.init()
    
    def __init__(self):
        pantalla = pygame.display.set_mode((ANCHO, ALTO))
        self.escenas = [Portada(pantalla), Partida(pantalla), Records(pantalla)]

    def start(self):

        i = 0

        while True:
            self.escenas[i].bucle_principal()
            i += 1
            if i == len(self.escenas):
                i = 0

