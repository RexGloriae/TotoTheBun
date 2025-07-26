# import needed libraries and modules
import pygame

from loaders import loadBlock, loadFireSheet, loadSpike, loadPortal

class Object(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, name = None):
        super().__init__()
        
        self.rect = pygame.Rect(x, y, width, height)
        self.image = pygame.Surface((width, height), pygame.SRCALPHA)
        self.width = width
        self.height = height
        self.name = name
        
    def draw(self, disp, offset_x, offset_y):
        disp.blit(self.image, (self.rect.x - offset_x, self.rect.y - offset_y))
        
        
class Block(Object):
    def __init__(self, x, y, size):
        super().__init__(x, y, size, size)
        
        block = loadBlock(size)
        self.image.blit(block, (0, 0))
        self.mask = pygame.mask.from_surface(self.image)
        
class Fire(Object):
    LATENCY = 3
    
    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height, "fire")
        self.fire = loadFireSheet(width, height)
        self.image = self.fire["off"][0]
        self.mask = pygame.mask.from_surface(self.image)
        self.anim_count = 0
        self.anim_name = "on"
        
    def on(self):
        self.anim_name = "on"
        
    def off(self):
        self.anim_name = "off"
        
    def loop(self):
        sprites = self.fire[self.anim_name]
        
        index = (self.anim_count // self.LATENCY) % len(sprites)
        
        self.image = sprites[index]
        self.anim_count += 1
        
        self.rect = self.image.get_rect(topleft = (self.rect.x, self.rect.y))
        self.mask = pygame.mask.from_surface(self.image)
        
        if (self.anim_count // self.LATENCY) > len(sprites):
            self.anim_count = 0

class Spike(Object):
    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height, "spike")
        
        self.image = loadSpike(width, height)
        
    def loop(self):
        self.rect = self.image.get_rect(topleft = (self.rect.x, self.rect.y))
        self.mask = pygame.mask.from_surface(self.image)
        
class Portal(Object):
    LATENCY = 3
    
    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height, "portal")
        self.sprites = loadPortal(width, height)
        self.mask = pygame.mask.from_surface(self.image)
        self.anim_count = 0

    def loop(self):
        
        index = (self.anim_count // self.LATENCY) % len(self.sprites)
        
        self.image = self.sprites[index]
        self.anim_count += 1
        
        self.rect = self.image.get_rect(topleft = (self.rect.x, self.rect.y))
        self.mask = pygame.mask.from_surface(self.image)
        
        if (self.anim_count // self.LATENCY) > len(self.sprites):
            self.anim_count = 0
