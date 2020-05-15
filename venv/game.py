import pygame
import sys
ANCHO = 640
ALTO = 480
color_blau = (104, 117, 243 )
class Bola(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        #cargar imatge
        self.image = pygame.image.load('img/ball.png')
        #obtindre rectangle de la imatge
        self.rect = self.image.get_rect()
        #posicions
        self.rect.centerx = ANCHO/2
        self.rect.centery = ALTO/2
        # establir velocitat inicial
        self.speed = [3,3]

    def update(self):
        if self.rect.bottom >=ALTO or self.rect.top <=0:
            self.speed[1] = -self.speed[1]
        elif self.rect.right >= ANCHO or self.rect.left <= 0:
            self.speed[0] = -self.speed[0]

        self.rect.move_ip(self.speed)

class Paleta(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        #cargar imatge
        self.image = pygame.image.load('img/line.png')
        #obtindre rectangle de la imatge
        self.rect = self.image.get_rect()
        #posicions
        self.rect.midbottom = (ANCHO/2,ALTO - 20)
        # establir velocitat inicial
        self.speed = [0,0]
    def update(self,evento):
        if evento.key == pygame.K_LEFT and self.rect.left > 0:
            self.speed = [-5,0]
        elif evento.key == pygame.K_RIGHT and self.rect.right < ANCHO:
            self.speed = [5,0]
        else:
            self.speed = [0,0]
        self.rect.move_ip(self.speed)

class Ladrillo(pygame.sprite.Sprite):
    def __init__(self,posicion):
        pygame.sprite.Sprite.__init__(self)
        #cargar imatge
        self.image = pygame.image.load('img/brick.png')
        #obtindre rectangle de la imatge
        self.rect = self.image.get_rect()
        #posicions
        self.rect.topleft = posicion
class Muro(pygame.sprite.Group):
    def __init__ (self,cantidadLadrillos):
        pygame.sprite.Group.__init__(self)
        pos_x = 0
        pos_y = 20
        for i in range(cantidadLadrillos):
            ladrillo =Ladrillo((pos_x,pos_y))
            self.add(ladrillo)
            pos_x += ladrillo.rect.width
            if(pos_x >=ANCHO):
                pos_x=0
                pos_y +=ladrillo.rect.height

#obrir pantalla
pantalla = pygame.display.set_mode((ANCHO,ALTO))
pygame.display.set_caption('Joc de ladrillos')
reloj = pygame.time.Clock()
pygame.key.set_repeat(30)
bola = Bola()
jugador = Paleta()
muro = Muro(50)
while True:
        reloj.tick(80)
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                    sys.exit()
            elif evento.type == pygame.KEYDOWN:
                jugador.update(evento)
        bola.update()
        pantalla.fill(color_blau)
        pantalla.blit(bola.image,bola.rect)
        pantalla.blit(jugador.image, jugador.rect)
        muro.draw(pantalla)
        pygame.display.flip()