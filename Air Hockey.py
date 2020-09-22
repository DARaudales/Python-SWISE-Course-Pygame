import pygame

pygame.init()



ganar = pygame.display.set_mode((750, 500))

pygame.display.set_caption('Table Air Hockey')

blanco = (255, 255, 255)
negro = (0, 0, 0)

# Sprites

class Barra1(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([10, 75])
        self.image.fill(blanco)
        self.rect = self.image.get_rect()
        self.points = 0

class Barra2(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([10, 75])
        self.image.fill(blanco)
        self.rect = self.image.get_rect()
        self.points = 0

class Pelota(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([10, 10])
        self.image.fill(blanco)
        self.rect = self.image.get_rect()
        self.speed = 10
        self.dx = 1
        self.dy = 1


barra1 = Barra1()
barra1.rect.x = 25
barra1.rect.y = 225

barra2= Barra2()
barra2.rect.x = 715
barra2.rect.y = 225

velocidad_barra = 10

ball = Pelota()
ball.rect.x = 375
ball.rect.y = 250

# Grupo de sprites

all_sprites = pygame.sprite.Group()
all_sprites.add(barra1, barra2, ball)


# funcion para actualizar la pantalla

def dibujar():
    #pantalla negra
    ganar.fill(negro)

    #fuente de titulo
    fuente = pygame.font.SysFont('Comic Sans MS', 30)
    texto = fuente.render('AIR HOCKEY', False, blanco)
    textRect = texto.get_rect()
    textRect.center = (750 // 2, 25)
    ganar.blit(texto, textRect)

    # Player 1 Score
    p1_score = fuente.render(str(barra1.points), False, blanco)
    p1Rect = p1_score.get_rect()
    p1Rect.center = (50, 50)
    ganar.blit(p1_score, p1Rect)

    # Player 2 Score
    p2_score = fuente.render(str(barra2.points), False, blanco)
    p2Rect = p2_score.get_rect()
    p2Rect.center = (700, 50)
    ganar.blit(p2_score, p2Rect)


    all_sprites.draw(ganar)


    pygame.display.update()

run = True
