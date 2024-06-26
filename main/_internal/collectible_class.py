# import needed libraries and modules
import pygame

from loaders import loadCarrotCollectible, loadBananaCollectible, loadHealthPotionCollectible

class Collectible(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, name = None):
        super().__init__()
        
        self.rect = pygame.Rect(x, y, width, height)
        self.image = pygame.Surface((width, height), pygame.SRCALPHA)
        self.width = width
        self.height = height
        self.name = name
        
        self.touched = 0

        
    def draw(self, disp, offset_x, offset_y):
        disp.blit(self.image, (self.rect.x - offset_x, self.rect.y - offset_y))

        
class Carrot(Collectible):
    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height, "carrot")
        
        self.image = loadCarrotCollectible(width, height)
        self.value = 1
        
    def loop(self):
        self.rect = self.image.get_rect(topleft = (self.rect.x, self.rect.y))
        self.mask = pygame.mask.from_surface(self.image)

class Banana(Collectible):
    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height, "banana")
        
        self.image = loadBananaCollectible(width, height)
        self.value = 5
        
    def loop(self):
        self.rect = self.image.get_rect(topleft = (self.rect.x, self.rect.y))
        self.mask = pygame.mask.from_surface(self.image)
        
class Potion(Collectible):
    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height, "potion")
        
        self.image = loadHealthPotionCollectible(width, height)
        
    def loop(self):
        self.rect = self.image.get_rect(topleft = (self.rect.x, self.rect.y))
        self.mask = pygame.mask.from_surface(self.image)
