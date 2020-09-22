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


