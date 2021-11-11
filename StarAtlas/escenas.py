import pygame
from .constantes import ANCHO, ALTO, FPS
from .entidades import Meteoritos, Player, Marcador




class Escena():
    def __init__(self, pantalla):
        self.pantalla = pantalla
        self.reloj = pygame.time.Clock()


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
        self.player = Player(self.pantalla, midbottom = (ANCHO // 2, ALTO -15))
        self.ListaMeteoritos = []
        for _ in range(8):
            self.ListaMeteoritos.append(Meteoritos(self.pantalla))
        
        self.cuentaPuntos = Marcador(10, 40, "CabinSketch-Bold.ttf", 24, (255, 255, 255))
        self.cuentaVidas = Marcador(10, 10, "CabinSketch-Bold.ttf", 24, (255, 255, 255))
        self.todos.add(self.cuentaPuntos, self.cuentaVidas)

        

    def reset(self):
        self.player.vidas = 3
        self.puntos = 0
        self.player.reset()


        
    def bucle_principal(self):

        self.reset()
        game_over = False
        while not game_over:
            self.reloj.tick(FPS)
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    exit()

            
            self.pantalla.blit(self.fondo, (0,0))
            ''' AREA DE DIBUJO '''
            self.player.update()
            self.player.draw()

            for meteorito in self.ListaMeteoritos:
                meteorito.comprobar_colision(self.player)
                meteorito.update()
                meteorito.draw()

            self.cuentaVidas.texto = self.player.vidas
            self.cuentaPuntos.texto = self.puntos

            if self.player.vidas <= 0:
                game_over = True
            
            self.todos.update()
            
            self.todos.draw(self.pantalla)
            
           
            pygame.display.flip()

class Records(Escena):

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

            self.pantalla.fill((80, 80, 200))  
        

            pygame.display.flip()
