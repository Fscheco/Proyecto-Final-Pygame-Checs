import pygame
from .constantes import ANCHO, ALTO, FPS
from .entidades import Meteoritos, Player, Marcador




class Escena():
    def __init__(self, pantalla):
        self.pantalla = pantalla
        self.reloj = pygame.time.Clock()

    def bucle_principal():
        pass

class Portada(Escena):
    def __init__(self, pantalla):
        super().__init__(pantalla)
      

    def bucle_principal(self):
        game_over = False
        while not game_over:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    exit()

                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_SPACE:
                        game_over = True

            self.pantalla.fill((80, 80, 255))  
        

            pygame.display.flip()


class Partida(Escena):
    def __init__(self, pantalla):
        super().__init__(pantalla)
        self.fondo = pygame.image.load("resources/img/starfield.png")
        self.todos = pygame.sprite.Group()
        self.player = Player(midbottom = (ANCHO // 2, ALTO -15))
        self.meteoritos = []
        for _ in range(8):
            self.meteoritos.append(Meteoritos())
        


        self.cuentaPuntos = Marcador(10, 40, "CabinSketch-Bold.ttf", 24, (255, 255, 255))
        self.cuentaVidas = Marcador(10, 10, "CabinSketch-Bold.ttf", 24, (255, 255, 255))
        self.todos.add(self.player, self.cuentaPuntos, self.cuentaVidas, self.meteoritos)

        

    def reset(self):
        self.vidas = 3
        self.puntos = 0
        ## self.player.reset() ##


        
    def bucle_principal(self):
        self.reset()
        while self.vidas > 0:
            self.reloj.tick(FPS)
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    exit()


            self.cuentaVidas.texto = self.vidas
            self.cuentaPuntos.texto = self.puntos

            self.todos.update()
        


            self.pantalla.blit(self.fondo, (0,0))
            self.todos.draw(self.pantalla)
    
            pygame.display.flip()

class Records(Escena):
    pass