# import needed libraries
import os
import random
import math
import pygame
from os import listdir
from os.path import isfile, join

# init pygame and set title
pygame.init()
pygame.mixer.init()
pygame.display.set_caption("Toto the Bun: the Great Carrot Adventure")

# screen dimensions
WIDTH, HEIGHT = 1000, 800

# in-game frames per second
FPS = 60

# speed at which the player moves on screen
PLAYER_SPEED = 6

# game screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))

def flipImg(sprites):
    return [pygame.transform.flip(sprite, True, False) for sprite in sprites]

def loadSoundEffects():
    all_sounds = {}
    
    banana = pygame.mixer.Sound("assets/Sounds/Effects/banana.wav")
    all_sounds["banana"] = banana
    
    carrot = pygame.mixer.Sound("assets/Sounds/Effects/carrot.wav")
    all_sounds["carrot"] = carrot
    
    demon_death = pygame.mixer.Sound("assets/Sounds/Effects/demon_death.wav")
    all_sounds["demon_death"] = demon_death
    
    enemy_hit = pygame.mixer.Sound("assets/Sounds/Effects/enemy_hit.wav")
    all_sounds["enemy_hit"] = enemy_hit
    
    health = pygame.mixer.Sound("assets/Sounds/Effects/health_potion.wav")
    all_sounds["health_potion"] = health
    
    lvl = pygame.mixer.Sound("assets/Sounds/Effects/level_finish.wav")
    all_sounds["level_finish"] = lvl
    
    death = pygame.mixer.Sound("assets/Sounds/Effects/player_death.wav")
    all_sounds["player_death"] = death
    
    hit = pygame.mixer.Sound("assets/Sounds/Effects/player_hit.flac")
    all_sounds["player_hit"] = hit
    
    slime = pygame.mixer.Sound("assets/Sounds/Effects/slime_death.wav")
    all_sounds["slime_death"] = slime
    
    return all_sounds

def loadCarrotCollectible(width, height):
    carrot = pygame.image.load(f'assets/Collectibles/Carrot.png').convert_alpha()
    scale = height / carrot.get_height()
    new_width = carrot.get_width() * scale
    new_height = carrot.get_height() * scale
    carrot = pygame.transform.scale(carrot, (new_width, new_height))
    
    return pygame.transform.scale2x(carrot)

def loadBananaCollectible(width, height):
    banana = pygame.image.load(f'assets/Collectibles/Banana_Peeled.png').convert_alpha()
    scale = height / banana.get_height()
    new_width = banana.get_width() * scale
    new_height = banana.get_height() * scale
    banana = pygame.transform.scale(banana, (new_width, new_height))
    
    return pygame.transform.scale2x(banana)

def loadHealthPotionCollectible(width, height):
    potion = pygame.image.load(f'assets/Collectibles/Health_Potion.png').convert_alpha()
    scale = height / potion.get_height()
    new_width = potion.get_width() * scale
    new_height = potion.get_height() * scale
    potion = pygame.transform.scale(potion, (new_width, new_height))
    
    return pygame.transform.scale2x(potion)

def loadFireSheet(width, height):
    path = join("assets", "Traps", "Fire")
    images = [f for f in listdir(path) if isfile(join(path, f))]

    fire = {}

    for image in images:
        sprite_sheet = pygame.image.load(join(path, image)).convert_alpha()

        sprites = []
        for i in range(sprite_sheet.get_width() // width):
            surface = pygame.Surface((width, height), pygame.SRCALPHA, 32)
            rect = pygame.Rect(i * width, 0, width, height)
            surface.blit(sprite_sheet, (0, 0), rect)
            sprites.append(pygame.transform.scale2x(surface))

        fire[image.replace(".png", "")] = sprites

    return fire

def loadSpike(width, height):  
    spike = pygame.image.load(f'assets/Traps/Spike/Idle.png').convert_alpha()
    scale = height / spike.get_height()
    new_width = spike.get_width() * scale
    new_height = spike.get_height() * scale
    spike = pygame.transform.scale(spike, (new_width, new_height))
    
    return pygame.transform.scale2x(spike)

def loadPortal(width, height):
    portal = []
    for i in range(1, 7):
        img = pygame.image.load(f'assets/Portal/p{i}.png').convert_alpha()
        scale = height / img.get_height()
        new_width = img.get_width() * scale
        new_height = img.get_height() * scale
        img = pygame.transform.scale(img, (new_width, new_height))
        portal.append(pygame.transform.scale2x(img))
        
    return portal

def loadSpriteSheet(player_width, player_height):
    
    all_sprites = {}
    
    # Load Running Sprites
    running_sprites = []
    for i in range(1, 5):
        running_sprite = pygame.image.load(f'assets/Player_Sprites/Running/a{i}.png').convert_alpha()
        scale = player_height / running_sprite.get_height()
        new_width = running_sprite.get_width() * scale
        new_height = running_sprite.get_height() * scale
        running_sprite = pygame.transform.scale(running_sprite, (new_width, new_height))
        running_sprites.append(running_sprite)
    
    all_sprites["run" + "_right"] = running_sprites
    all_sprites["run" + "_left"] = flipImg(running_sprites)
        
    # Load Jumping Sprites
    jumping_sprites = []
    
    sprite = pygame.image.load(f'assets/Player_Sprites/Jump/a2.png').convert_alpha()
    scale = player_height / sprite.get_height()
    new_width = sprite.get_width() * scale
    new_height = sprite.get_height() * scale
    sprite = pygame.transform.scale(sprite, (new_width, new_height))
    jumping_sprites.append(sprite)
    
    all_sprites["jump" + "_right"] = jumping_sprites
    all_sprites["jump" + "_left"] = flipImg(jumping_sprites)
    
    # Load Fall Sprites
    falling_sprites = []
    
    sprite = pygame.image.load(f'assets/Player_Sprites/Jump/a5.png').convert_alpha()
    scale = player_height / sprite.get_height()
    new_width = sprite.get_width() * scale
    new_height = sprite.get_height() * scale
    sprite = pygame.transform.scale(sprite, (new_width, new_height))
    falling_sprites.append(sprite)
    
    all_sprites["fall" + "_right"] = falling_sprites
    all_sprites["fall" + "_left"] = flipImg(falling_sprites)
            
    # Load Faint Sprite
    faint_sprites = []
    for i in range(1, 6):
        sprite = pygame.image.load(f'assets/Player_Sprites/Faint/a{i}.png').convert_alpha()
        scale = player_height / sprite.get_height()
        new_width = sprite.get_width() * scale
        new_height = sprite.get_height() * scale
        sprite = pygame.transform.scale(sprite, (new_width, new_height))
        faint_sprites.append(sprite)
        
    all_sprites["faint" + "_right"] = faint_sprites
    all_sprites["faint" + "_left"] = flipImg(faint_sprites)
        
    # Load Dizzy Sprite
    dizzy_sprites = []
    for i in range(1, 3):
        sprite = pygame.image.load(f'assets/Player_Sprites/Dizzy/a{i}.png').convert_alpha()
        scale = player_height / sprite.get_height()
        new_width = sprite.get_width() * scale
        new_height = sprite.get_height() * scale
        sprite = pygame.transform.scale(sprite, (new_width, new_height))
        dizzy_sprites.append(sprite)
        
    all_sprites["dizzy" + "_right"] = dizzy_sprites
    all_sprites["dizzy" + "_left"] = flipImg(dizzy_sprites)
        
    # Load Idle Sprite
    idle_sprites = []
    for i in range(1, 3):
        sprite = pygame.image.load(f'assets/Player_Sprites/Idle/a{i}.png').convert_alpha()
        scale = player_height / sprite.get_height()
        new_width = sprite.get_width() * scale
        new_height = sprite.get_height() * scale
        sprite = pygame.transform.scale(sprite, (new_width, new_height))
        idle_sprites.append(sprite)
        
    all_sprites["idle" + "_right"] = idle_sprites
    all_sprites["idle" + "_left"] = flipImg(idle_sprites)
    
    # load Shoot Sprite
    shoot_sprites = []
    for i in range(1, 4):
        sprite = pygame.image.load(f'assets/Player_Sprites/Shoot/a{i}.png').convert_alpha()
        scale = player_height / sprite.get_height()
        new_width = sprite.get_width() * scale
        new_height = sprite.get_height() * scale
        sprite = pygame.transform.scale(sprite, (new_width, new_height))
        shoot_sprites.append(sprite)
    
    all_sprites["shoot" + "_right"] = shoot_sprites
    all_sprites["shoot" + "_left"] = flipImg(shoot_sprites)
    
    # load explode sprite
    explode_sprite = []
    for i in range(1, 6):
        sprite = pygame.image.load(f'assets/Player_Sprites/Explode/a{i}.png').convert_alpha()
        scale = player_height / sprite.get_height()
        new_width = sprite.get_width() * scale
        new_height = sprite.get_height() * scale
        sprite = pygame.transform.scale(sprite, (new_width, new_height))
        explode_sprite.append(sprite)
        
    all_sprites["explode_left"] = explode_sprite
    all_sprites["explode_right"] = flipImg(explode_sprite)
    
    return all_sprites

def loadHealthSprites(width, height):
    # load Health Sprite
    health_sprites = []
    for i in range(1, 9):
        sprite = pygame.image.load(f'assets/Player_Sprites/HearTile/Cuore{i}.png').convert_alpha()
        scale = height / sprite.get_height()
        new_width = sprite.get_width() * scale
        new_height = sprite.get_height() * scale
        sprite = pygame.transform.scale(sprite, (new_width, new_height))
        health_sprites.append(sprite)
    
    return health_sprites

# load terrain
def loadBlock(size):
    path = join("assets", "Terrain", "Terrain.png")
    image = pygame.image.load(path).convert_alpha()
    surface = pygame.Surface((size, size), pygame.SRCALPHA, 32)
    rect = pygame.Rect(96, 0, size, size)
    surface.blit(image, (0, 0), rect)
    
    return pygame.transform.scale2x(surface)

# load enemy sprites
def loadEnemySprites(width, height, name):
    all_sprites = {}
    
    path = None
    if name == "demon":
        path = "assets/Enemy/Demon/"
    else:
        path = "assets/Enemy/Slime/"
        
    # load attack sprites
    attack_sprites = []
    range_end = None
    if name == "demon":
        range_end = 9
    else:
        range_end = 6
    for i in range(1, range_end):
        sprite = pygame.image.load(path + f'attack/{i}.png').convert_alpha()
        scale = height / sprite.get_height()
        new_height = sprite.get_height() * scale
        new_width = sprite.get_width() * scale
        sprite = pygame.transform.scale(sprite, (new_width, new_height))
        if name == "slime":
            sprite = pygame.transform.scale2x(sprite)
        sprite = pygame.transform.scale2x(sprite)
        attack_sprites.append(sprite)
        
    all_sprites["attack_left"] = attack_sprites
    all_sprites["attack_right"] = flipImg(attack_sprites)

    # load death sprites
    death_sprites = []
    range_end = None
    if name == "demon":
        range_end = 8
    else:
        range_end = 5
    for i in range(1, range_end):
        sprite = pygame.image.load(path + f'death/{i}.png').convert_alpha()
        scale = height / sprite.get_height()
        new_width = scale * sprite.get_width()
        new_height = scale * sprite.get_height()
        sprite = pygame.transform.scale(sprite, (new_width, new_height))
        if name == "slime":
            sprite = pygame.transform.scale2x(sprite)
        sprite = pygame.transform.scale2x(sprite)
        death_sprites.append(sprite)
        
    all_sprites["death_left"] = death_sprites
    all_sprites["death_right"] = flipImg(death_sprites)
    
    # load hurt sprites
    hurt_sprites = []
    range_end = 5
    for i in range(1, range_end):
        sprite = pygame.image.load(path + f'hurt/{i}.png').convert_alpha()
        scale = height / sprite.get_height()
        new_width = scale * sprite.get_width()
        new_height = scale * sprite.get_height()
        sprite = pygame.transform.scale(sprite, (new_width, new_height))
        if name == "slime":
            sprite = pygame.transform.scale2x(sprite)
        sprite = pygame.transform.scale2x(sprite)
        hurt_sprites.append(sprite)
        
    all_sprites["hurt_left"] = hurt_sprites
    all_sprites["hurt_right"] = flipImg(hurt_sprites)
    
    # load move sprites
    move_sprites = []
    range_end = 5
    for i in range(1, range_end):
        sprite = pygame.image.load(path + f'move/{i}.png').convert_alpha()
        scale = height / sprite.get_height()
        new_width = scale * sprite.get_width()
        new_height = scale * sprite.get_height()
        sprite = pygame.transform.scale(sprite, (new_width, new_height))
        if name == "slime":
            sprite = pygame.transform.scale2x(sprite)
        sprite = pygame.transform.scale2x(sprite)
        move_sprites.append(sprite)
        
    all_sprites["move_left"] = move_sprites
    all_sprites["move_right"] = flipImg(move_sprites)
    
    return all_sprites
    
# Enemy Class
class Enemy(pygame.sprite.Sprite):
    LATENCY = 3
    
    def __init__(self, x, y, width, height, dx, name = "None"):
        super().__init__()
        
        self.SPRITES = loadEnemySprites(width, height, name)
        
        self.rect = pygame.Rect(x, y, width, height)
        
        self.name = name
        
        self.mask = None
        
        self.direction = "right"
        self.animation_count = 0
        self.speed = 3
        self.movement_range = dx
        self.distance_covered = 0
        
        self.hit = False
        self.hit_count = 0
        self.invincibility = False
        
        self.attacks = False
        self.attack_count = 0
        
        
        self.lives = True
        
        
    def move(self, dx):
        self.rect.x += dx
        
    def getHit(self):
        self.hit = True
        self.hit_count = 0
        
    def moveLeft(self, speed):
        self.speed = -speed
        if self.direction != "left":
            self.direction = "left"
            self.animation_count = 0
            
    def moveRight(self, speed):
        self.speed = speed
        if self.direction != "right":
            self.direction = "right"
            self.animation_count = 0

    def loop(self, fps):
        if self.hit == False and self.attacks == False:
            self.move(self.speed)

            self.distance_covered += abs(self.speed)

            if self.distance_covered >= self.movement_range:
                self.speed = -self.speed
                self.distance_covered = 0
                if self.direction == "left":
                    self.direction = "right"
                else:
                    self.direction = "left"
        
        if self.hit:
            self.hit_count += 1
        
        if self.hit_count > fps // 2:
            self.hit = False
            self.hit_count = 0
            self.invincibility = False
            if self.health <= 0:
                self.lives = False
                
        if self.attacks:
            self.attack_count += 1
            
        if self.attack_count > fps // 2:
            self.attacks = False
            self.attack_count = 0
            if self.speed > 0:
                self.direction = "right"
            else:
                self.direction = "left"
            
        self.updateSprite()
        
    def updateSprite(self):
        sprite_sheet = "move"
        if self.health <= 0:
            sprite_sheet = "death"
            self.invincibility = True
        elif self.hit:
            sprite_sheet = "hurt"
        elif self.attacks:
            sprite_sheet = "attack"
            
        sprite_sheet_name = sprite_sheet + "_" + self.direction
        sprites = self.SPRITES[sprite_sheet_name]
        
        if sprite_sheet == "death":
            index = (self.animation_count // 10) % len(sprites)
        else:
            index = (self.animation_count // self.LATENCY) % len(sprites)
        
        self.sprite = sprites[index]
        self.animation_count += 1
        
        self.update()
        
    def update(self):
        self.rect = self.sprite.get_rect(topleft = (self.rect.x, self.rect.y))
        self.mask = pygame.mask.from_surface(self.sprite)
        
    def draw(self, disp, dx):
        disp.blit(self.sprite, (self.rect.x - dx, self.rect.y))
            
# slime enemy
class Slime(Enemy):
    def __init__(self, x, y, width, height, dx):
        super().__init__(x, y, width, height, dx, "slime")
        
        self.health = 1
        self.points = 2
        
        self.distance = dx
        


class Demon(Enemy):
    def __init__(self, x, y, width, height, dx):
        super().__init__(x, y, width, height, dx, "demon")
        
        self.health = 3
        self.points = 10
        
        self.distance = dx
        


# Player Class
class Player(pygame.sprite.Sprite):
    COLOR=(255, 0, 0)
    GRAVITY = 1
    
    SPRITES = loadSpriteSheet(64, 64)
    LATENCY = 3
    
    HEALTH_IMG = loadHealthSprites(30, 30)
    
    def __init__(self, x, y, width, height):
        super().__init__()
        
        self.rect = pygame.Rect(x, y, width, height)
        
        self.x_speed = 0
        self.y_speed = 0
        
        self.mask = None
        
        self.direction = "left"
        self.animation_count = 0
        
        self.fall_count = 0
        self.jump_count = 0
        
        self.hit = False
        self.hit_count = 0
        
        self.health = 3
        self.invincibility = False
        self.health_anim = 0
        
        self.score = 0
        
        self.will_teleport = False
        self.teleport_count = 0
        
    def jump(self):
        multiplier = 6
        if self.jump_count == 1:
            multiplier = 9
        
        self.y_speed = -self.GRAVITY * multiplier
        self.animation_count = 0
        self.jump_count += 1
        
        if self.jump_count == 1:
            self.fall_count = 0
        
        
    def move(self, dx, dy):
        self.rect.x += dx
        self.rect.y += dy
        
    def getHit(self):
        self.hit = True
        self.hit_count = 0
        
    def moveLeft(self, speed):
        self.x_speed = -speed
        if self.direction != "left":
            self.direction = "left"
            self.animation_count = 0
        
    def moveRight(self, speed):
        self.x_speed = speed
        if self.direction != "right":
            self.direction = "right"
            self.animation_count = 0
    
    def loop(self, fps):
        self.y_speed += min(1, (self.fall_count / fps) * self.GRAVITY)
        self.move(self.x_speed, self.y_speed)
        
        if self.hit:
            self.hit_count += 1
            
        if self.hit_count > fps // 2:
            self.hit = False
            self.hit_count = 0
            self.invincibility = False
            if self.health <= 0:
                main(screen)
                
        if self.will_teleport:
            self.teleport_count += 1
            
        if self.teleport_count > fps // 2:
            main(screen)
        
        self.fall_count += 1
        
        self.updateSprite()
        
    def landed(self):
        self.fall_count = 0
        self.y_speed = 0
        self.jump_count = 0
        
    def hitHead(self):
        self.count = 0
        self.y_speed *= -1
    
    def displayHealth(self, disp):
        index = (self.health_anim // self.LATENCY) % len(self.HEALTH_IMG)
        for life in range(self.health):
            sprite = self.HEALTH_IMG[index]
            x_pos = 10 + life * (sprite.get_width() + 10)
            y_pos = 10
            disp.blit(sprite, (x_pos, y_pos))
        
    def updateSprite(self):
        sprite_sheet = "idle"
        if self.health <= 0:
            sprite_sheet = "faint"
            self.invincibility = True
        elif self.will_teleport:
            sprite_sheet = "explode"
        elif self.hit:
            sprite_sheet = "dizzy"
        elif self.y_speed < 0:
            sprite_sheet = "jump"
        elif self.y_speed > self.GRAVITY * 2:
            sprite_sheet = "fall"
        elif self.x_speed != 0:
            sprite_sheet = "run"
            
        sprite_sheet_name = sprite_sheet + "_" + self.direction
        sprites = self.SPRITES[sprite_sheet_name]
        
        if sprite_sheet == "faint":
            index = (self.animation_count // 10) % len(sprites) # value for which the animation works (if it works, don't change it)
        elif sprite_sheet == "explode":
            index = (self.animation_count // 5) % len(sprites) # value for which the animation works (if it works, don't change it)
        else:
            index = (self.animation_count // self.LATENCY) % len(sprites)
        
        self.sprite = sprites[index]
        self.animation_count += 1
        
        self.health_anim += 1
        if(self.health_anim >= len(self.HEALTH_IMG) * self.LATENCY):
            self.health_anim = 0
            
        
        self.update()
        
    def update(self):
        self.rect = self.sprite.get_rect(topleft = (self.rect.x, self.rect.y))
        self.mask = pygame.mask.from_surface(self.sprite)
        
        
    def draw(self, disp, offset_x):
        disp.blit(self.sprite, (self.rect.x - offset_x, self.rect.y))
        self.displayHealth(disp)

class Object(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, name = None):
        super().__init__()
        
        self.rect = pygame.Rect(x, y, width, height)
        self.image = pygame.Surface((width, height), pygame.SRCALPHA)
        self.width = width
        self.height = height
        self.name = name
        
    def draw(self, disp, offset_x):
        disp.blit(self.image, (self.rect.x - offset_x, self.rect.y))
        
        
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
        
        
class Collectible(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, name = None):
        super().__init__()
        
        self.rect = pygame.Rect(x, y, width, height)
        self.image = pygame.Surface((width, height), pygame.SRCALPHA)
        self.width = width
        self.height = height
        self.name = name
        
        self.touched = 0

        
    def draw(self, disp, offset_x):
        disp.blit(self.image, (self.rect.x - offset_x, self.rect.y))

        
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
        

def handleVerticalCollision(player, objects, enemies, dy):
    collided_objects = []
    for obj in objects:
        if pygame.sprite.collide_mask(player, obj):
            if obj.name == "portal":
                player.will_teleport = True
            elif dy > 0:
                player.rect.bottom = obj.rect.top
                player.landed()
            elif dy < 0:
                player.rect.top = obj.rect.bottom
                player.hitHead()
            collided_objects.append(obj)
    
    enemy_hit = None
    if dy > 0:
        for ent in enemies:
            if ent.lives and pygame.sprite.collide_mask(player, ent):
                height_index = 1
                if ent.name == "demon":
                    height_index = 3
                if player.rect.bottom <= ent.rect.top + ent.rect.height // height_index:
                    player.rect.bottom = ent.rect.top
                    player.landed()
                    enemy_hit = ent
                    break
        
    return collided_objects, enemy_hit

def isEnemyHitting(player, enemies, dx):
    player.move(dx, 0)
    player.update()
    
    attacker = None
    for ent in enemies:
        if ent.lives and ent.invincibility == False:
            if pygame.sprite.collide_mask(player, ent):
                attacker = ent
                ent.attacks = True
                if ent.rect.x < player.rect.x:
                    ent.direction = "right"
                else:
                    ent.direction = "left"
                break
    
    player.move(-dx, 0)
    player.update
    
    return attacker

def collide(player, objects, dx):
    player.move(dx, 0)
    player.update()
    
    collided_object = None
    
    for obj in objects:
        if pygame.sprite.collide_mask(player, obj):
            collided_object = obj
            if obj.name == "portal":
                player.will_teleport = True
            break
        
    player.move(-dx, 0)
    player.update()
    
    return collided_object

def handleCollectibles(player, collectibles):
    collided_items = []
    
    for item in collectibles:
        if pygame.sprite.collide_mask(player, item):
            item.touched += 1
            collided_items.append(item)
    
    return collided_items


def handleMovement(player, objects, collectibles, enemies, sounds):
    keys = pygame.key.get_pressed()
    
    collide_left = collide(player, objects, -PLAYER_SPEED * 2)
    collide_right = collide(player, objects, PLAYER_SPEED * 2)
    
    attacker_left = isEnemyHitting(player, enemies, -PLAYER_SPEED * 2)
    attacker_right = isEnemyHitting(player, enemies, PLAYER_SPEED * 2)
    
    
    player.x_speed = 0
    if player.health > 0:
        if keys[pygame.K_a] and not collide_left:
            player.moveLeft(PLAYER_SPEED)
        if keys[pygame.K_d] and not collide_right:
            player.moveRight(PLAYER_SPEED)
        
    vertical_collide, enemy_hit = handleVerticalCollision(player, objects, enemies, player.y_speed)
    to_check = [collide_left, collide_right, *vertical_collide]
    
    for obj in to_check:
        if obj and obj.name == "fire" and player.invincibility == False:
            player.getHit()
            player.health -= 1
            player.invincibility = True
            curr_sound = sounds["player_hit"]
            if player.health == 0:
                curr_sound = sounds["player_death"]
            curr_sound.play()
        elif obj and obj.name == "spike" and player.invincibility == False:
            player.getHit()
            player.health -= 1
            player.invincibility = True
            curr_sound = sounds["player_hit"]
            if player.health == 0:
                curr_sound = sounds["player_death"]
            curr_sound.play()
        elif obj and obj.name == "portal":
            curr_sound = sounds["level_finish"]
            curr_sound.set_volume(0.5)
            curr_sound.play()
    
    if player.invincibility == False:
        if enemy_hit:
            if enemy_hit.invincibility == False:
                enemy_hit.health -= 1
                enemy_hit.getHit()
                enemy_hit.invincibility = True
                curr_sound = sounds["enemy_hit"]
                if enemy_hit.health <= 0:
                    player.score += enemy_hit.points
                    curr_sound = sounds[enemy_hit.name + "_death"]
                curr_sound.play()
        elif attacker_left or attacker_right:
            player.getHit()
            player.health -= 1
            player.invincibility = True
            curr_sound = sounds["player_hit"]
            if player.health == 0:
                curr_sound = sounds["player_death"]
            curr_sound.play()
            
    to_check = handleCollectibles(player, collectibles)
    for obj in to_check:
        if obj and obj.name == "potion" and obj.touched == 1:
            if player.health < 3:
                player.health += 1
                curr_sound = sounds["health_potion"]
                curr_sound.play()
            else:
                obj.touched = 0
        elif obj and obj.touched == 1:
            player.score += obj.value
            if obj.name == "carrot":
                curr_sound = sounds["carrot"]
            else:
                curr_sound = sounds["banana"]
            curr_sound.play()
            
        if obj.touched > 2:
            obj.touched = 2


# background function
def getBackground(level):
    if level > 8:
        level = level%8 + 1
    if level == 1:
        img = pygame.image.load("assets/Backgrounds/m1/PRE_ORIG_SIZE.png")
    elif level == 2:
        img = pygame.image.load("assets/Backgrounds/m2/PRE_ORIG_SIZE.png")
    elif level == 3:
        img = pygame.image.load("assets/Backgrounds/m3/PRE_ORIG_SIZE.png")
    elif level == 4:
        img = pygame.image.load("assets/Backgrounds/m4/PRE_ORIG_SIZE.png")
    elif level == 5:
        img = pygame.image.load("assets/Backgrounds/m5/PRE_ORIG_SIZE.png")
    elif level == 6:
        img = pygame.image.load("assets/Backgrounds/m6/PRE_ORIG_SIZE.png")
    elif level == 7:
        img = pygame.image.load("assets/Backgrounds/m7/PRE_ORIG_SIZE.png")
    elif level == 8:
        img = pygame.image.load("assets/Backgrounds/m8/PRE_ORIG_SIZE.png")
    
    return img

def drawText(screen, text, size, color, x, y):
    font = pygame.font.Font("assets/Fonts/pcsenior.ttf", size)
    text = font.render(text, True, color)
    screen.blit(text, (x, y))

def drawScreen(screen, level, player, objects, collectibles, enemies, offset_x):
    # set BackGround    
    background_img = getBackground(level)
    background_img = pygame.transform.scale(background_img, (WIDTH, HEIGHT))
    screen.blit(background_img, (0, 0))
    
    # draw objects
    for obj in objects:
        obj.draw(screen, offset_x)
        
    # draw collectibles
    for obj in collectibles:
        if obj.touched == 0:
            obj.draw(screen, offset_x)
    
    # draw Player
    player.draw(screen, offset_x)
    
    # draw enemies
    for entity in enemies:
        if entity.lives:
            entity.draw(screen, offset_x)
    
    # draw Score
    drawText(screen, f"Score = {player.score}", 16, (0, 0, 0), WIDTH - 180, 8)
    
    # draw game over text
    if player.health == 0:
        drawText(screen, "Game Over!", 64, (0, 0, 0), WIDTH // 5, HEIGHT / 2.5)
        
    # draw level finished text
    if player.will_teleport:
        drawText(screen, "Level Finished!", 64, (0, 0, 0), 30, HEIGHT / 2.5)
    
    pygame.display.update()    

def loopTraps(traps):
    for obj in traps:
        obj.loop()
        
def loopCollectibles(items):
    for obj in items:
        obj.loop()
        
def loopEnemies(enemies, fps):
    for enemy in enemies:
        enemy.loop(fps)

def loadLevelImgs(width, height):
    images = []
    for i in range(1, 9):
        img = pygame.image.load(f'assets/Level_Buttons/0{i}.png').convert_alpha()
        scale = height / img.get_height()
        new_width = img.get_width() * scale
        new_height = img.get_height() * scale
        img = pygame.transform.scale(img, (new_width, new_height))
        images.append(pygame.transform.scale2x(img))
        
    return images

def getLevelButtons(screen, width, height):
    # button coordinates
    x1 = width // 7
    x2 = 2.5*x1
    x3 = 4*x1
    x4 = 5.5*x1
    
    
    x = [x1, x2, x3, x4]
    
    y1 = height - height // 2
    y2 = y1 + 150
    
    y = [y1, y2]
    
    buttons = []
    
    # drawing buttons
    index_x = 0
    index_y = 0
    for img in range(9):
        button_rect = pygame.Rect(x[index_x], y[index_y], 64, 64)
        buttons.append(button_rect)
        
        index_x += 1
        if(index_x == 4):
            index_x = 0
            index_y = 1
    
    
    
    return buttons

def waitForLevelSelection(buttons):
    back_rect = pygame.Rect(0, 0, 50, 50)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.mixer.stop()
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mouse_pos = event.pos
                for idx, button in enumerate(buttons):
                    if button.collidepoint(mouse_pos):
                        return idx + 1
                if back_rect.collidepoint(mouse_pos):
                    return 9

def drawPlayMenu(screen, width, height):
    img = pygame.image.load("assets/Backgrounds/menu/play.png")
    img = pygame.transform.scale(img, (width, height))
    screen.blit(img, (0, 0))
    
    levels = loadLevelImgs(32, 32)
    back_img = loadBackImg(50, 50)
    
    # button coordinates
    x1 = width // 7
    x2 = 2.5*x1
    x3 = 4*x1
    x4 = 5.5*x1
    
    
    x = [x1, x2, x3, x4]
    
    y1 = height - height // 2
    y2 = y1 + 150
    
    y = [y1, y2]
    
    # drawing buttons
    index_x = 0
    index_y = 0
    for img in levels:
        screen.blit(img, (x[index_x], y[index_y]))
        
        index_x += 1
        if(index_x % 4 == 0):
            index_x = 0
            index_y = 1
            
    screen.blit(back_img, (0, 0))
            
    # drawing text
    drawText(screen, "Toto the Bun:", 65, (0, 0, 0), WIDTH // 8 - 5, 20)
    drawText(screen, "Toto the Bun:", 64, (255, 255, 255), WIDTH // 8, 20)
    drawText(screen, "the Great Carrot Adventure", 36, (0, 0, 0), WIDTH // 18, 80)
    drawText(screen, "the Great Carrot Adventure", 36, (255, 255, 255), WIDTH // 18, 84)
    drawText(screen, "Select a Level:", 25, (0, 0, 0), 25, HEIGHT // 2 - 20)
    drawText(screen, "Select a Level:", 25, (255, 255, 255), 25, HEIGHT // 2 - 23)
    
    pygame.display.flip()

def play(screen, width, height):
    buttons = getLevelButtons(screen, width, height)
    drawPlayMenu(screen, width, height)
    level = waitForLevelSelection(buttons)  
    return level  

def displayControls(screen, width, height):
    img = pygame.image.load("assets/Backgrounds/menu/controls.png")
    img = pygame.transform.scale(img, (width, height))
    screen.blit(img, (0, 0))
    
    back_img = loadBackImg(50, 50)
    screen.blit(back_img, (0, 0))
    
    drawText(screen, "Toto the Bun:", 65, (0, 0, 0), WIDTH // 8 - 5, 20)
    drawText(screen, "Toto the Bun:", 64, (255, 255, 255), WIDTH // 8, 20)
    drawText(screen, "the Great Carrot Adventure", 36, (0, 0, 0), WIDTH // 18, 80)
    drawText(screen, "the Great Carrot Adventure", 36, (255, 255, 255), WIDTH // 18, 84)
    
    curr_height = 84 + 36 + 36
    drawText(screen, "Controls:", 20, (0, 0, 0), 15, curr_height - 4)
    drawText(screen, "Controls:", 20, (255, 255, 255), 15, curr_height)
    
    curr_height += 20 + 15
    drawText(screen, "Jump: W (x2 W for double jumping)", 16, (0, 0, 0), 10, curr_height - 2.5)
    drawText(screen, "Jump: W (x2 W for double jumping)", 16, (255, 255, 255), 10, curr_height)
    
    curr_height += 16 + 15
    drawText(screen, "Move Left: A", 16, (0, 0, 0), 10, curr_height - 2.5)
    drawText(screen, "Move Left: A", 16, (255, 255, 255), 10, curr_height)
    
    curr_height += 16 + 15
    drawText(screen, "Move Right: D", 16, (0, 0, 0), 10, curr_height - 2.5)
    drawText(screen, "Move Right: D", 16, (255, 255, 255), 10, curr_height)
    
    curr_height += 16 + 15
    drawText(screen, "Pause: SPACE", 16, (0, 0, 0), 10, curr_height - 2.5)
    drawText(screen, "Pause: SPACE", 16, (255, 255, 255), 10, curr_height)
    
    curr_height += 16 + 15
    drawText(screen, "Exit to Menu: ESC", 16, (0, 0, 0), 10, curr_height - 2.5)
    drawText(screen, "Exit to Menu: ESC", 16, (255, 255, 255), 10, curr_height)
    
    
    
    curr_height += 16 + 45
    drawText(screen, "Gameplay:", 20, (0, 0, 0), 15, curr_height)
    drawText(screen, "Gameplay:", 20, (0, 0, 0), 15, curr_height - 8)
    drawText(screen, "Gameplay:", 20, (255, 255, 255), 15, curr_height - 4)
    
    curr_height += 20 + 15
    text = "You are a bunny called Toto who is captive somewhere in the"
    drawText(screen, text, 16, (0, 0, 0), 10, curr_height)
    drawText(screen, text, 16, (255, 255, 255), 10, curr_height - 2.5)
    
    curr_height += 16 + 15
    text = "multiverse. Your goal is go search for the portal on every"
    drawText(screen, text, 16, (0, 0, 0), 10, curr_height)
    drawText(screen, text, 16, (255, 255, 255), 10, curr_height - 2.5)

    text = "level that will get you home. On every level you have"
    curr_height += 16 + 15
    drawText(screen, text, 16, (0, 0, 0), 10, curr_height)
    drawText(screen, text, 16, (255, 255, 255), 10, curr_height - 2.5)
    
    text = "different items such as carrots and bananas. Collecting them"
    curr_height += 16 + 15
    drawText(screen, text, 16, (0, 0, 0), 10, curr_height)
    drawText(screen, text, 16, (255, 255, 255), 10, curr_height - 2.5)
    
    text = "will increase your score. Try collecting them all! Also, you"
    curr_height += 16 + 15
    drawText(screen, text, 16, (0, 0, 0), 10, curr_height)
    drawText(screen, text, 16, (255, 255, 255), 10, curr_height - 2.5)
    
    text = "can find health potions. They increase your health, but no"
    curr_height += 16 + 15
    drawText(screen, text, 16, (0, 0, 0), 10, curr_height)
    drawText(screen, text, 16, (255, 255, 255), 10, curr_height - 2.5)
    
    text = "more than three lives! On every level, there are various"
    curr_height += 16 + 15
    drawText(screen, text, 16, (0, 0, 0), 10, curr_height)
    drawText(screen, text, 16, (255, 255, 255), 10, curr_height - 2.5)
    
    text = "dangers such as traps and mobs that can hurt you! Try"
    curr_height += 16 + 15
    drawText(screen, text, 16, (0, 0, 0), 10, curr_height)
    drawText(screen, text, 16, (255, 255, 255), 10, curr_height - 2.5)
    
    text = "avoiding them! You can hit a mob by jumping on his head!"
    curr_height += 16 + 15
    drawText(screen, text, 16, (0, 0, 0), 10, curr_height)
    drawText(screen, text, 16, (255, 255, 255), 10, curr_height - 2.5)
    
    text = "Be careful, on each level there are mobs that are harder"
    curr_height += 16 + 15
    drawText(screen, text, 16, (0, 0, 0), 10, curr_height)
    drawText(screen, text, 16, (255, 255, 255), 10, curr_height - 2.5)
    
    text = "to kill. Killing a mob will also increase your score!"
    curr_height += 16 + 15
    drawText(screen, text, 16, (0, 0, 0), 10, curr_height)
    drawText(screen, text, 16, (255, 255, 255), 10, curr_height - 2.5)
    
    text = "With all that being said, HAVE FUN PLAYING!"
    curr_height += 16 + 15
    drawText(screen, text, 16, (0, 0, 0), 10, curr_height)
    drawText(screen, text, 16, (255, 255, 255), 10, curr_height - 2.5)

    pygame.display.flip()
    
def waitForControlsSelection():
    back_rect = pygame.Rect(0, 0, 50, 50)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.mixer.stop()
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mouse_pos = event.pos
                if back_rect.collidepoint(mouse_pos):
                    return None

def controls(screen, width, height):
    displayControls(screen, width, height)
    return waitForControlsSelection()

def loadMenuButtons(width, height):
    buttons = []
    for i in range(1, 4):
        img = pygame.image.load(f'assets/Menu_Buttons/{i}.png').convert_alpha()
        scale = height / img.get_height()
        new_width = img.get_width() * scale
        new_height = img.get_height() * scale
        img = pygame.transform.scale(img, (new_width, new_height))
        buttons.append(img)
        
    return buttons

def getMenuButtons(screen, width, height):
    # button coordinates
    
    x = width // 2 - 150
    
    y1 = height // 4
    y2 = height // 2
    y3 = height // 2 + height // 4
    
    buttons = []
    
    y = [y1, y2, y3]
    for img in range(3):
        button_rect = pygame.Rect(x, y[img], 300, 100)
        buttons.append(button_rect)
        
    return buttons

def drawMainMenu(screen, width, height):
    img = pygame.image.load("assets/Backgrounds/menu/main.png")
    img = pygame.transform.scale(img, (width, height))
    screen.blit(img, (0, 0))
    
    buttons = loadMenuButtons(300, 100)
    
    # button coordinates
    x = width // 2 - 150
    
    y1 = height // 4
    y2 = height // 2
    y3 = height // 2 + height // 4
    
    y = [y1, y2, y3]
    
    # drawing buttons
    index = 0
    for img in buttons:
        screen.blit(img, (x, y[index]))
        
        index += 1
        
    # drawing text
    drawText(screen, "Toto the Bun:", 65, (0, 0, 0), WIDTH // 8 - 5, 20)
    drawText(screen, "Toto the Bun:", 64, (255, 255, 255), WIDTH // 8, 20)
    drawText(screen, "the Great Carrot Adventure", 36, (0, 0, 0), WIDTH // 18, 80)
    drawText(screen, "the Great Carrot Adventure", 36, (255, 255, 255), WIDTH // 18, 84)
    
    pygame.display.flip()
    
def waitForMenuSelection(buttons):
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.mixer.stop()
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mouse_pos = event.pos
                for idx, button in enumerate(buttons):
                    if button.collidepoint(mouse_pos):
                        return idx + 1

def mainMenu(screen, width, height):
    buttons = getMenuButtons(screen, width, height)
    drawMainMenu(screen, width, height)
    option = waitForMenuSelection(buttons)
    
    lvl = None
    if option == 1:
        lvl = play(screen, width, height)
        if lvl == 9:
            lvl = None
    elif option == 2:
        controls(screen, width, height)
    elif option == 3:
        pygame.mixer.stop()
        pygame.quit()
        quit()
        
    return lvl

def loadBackImg(width, height):
    img = pygame.image.load("assets/Menu_Buttons/4.png").convert_alpha()
    scale = height / img.get_height()
    new_width = img.get_width() * scale
    new_height = img.get_height() * scale
    img = pygame.transform.scale(img, (new_width, new_height))
    
    return img

def getLevelMusic(level):
    music = pygame.mixer.Sound(f'assets/Sounds/Music/lv{level}.wav')
    return music

# main function
def main(screen):
    level = None
    
    pygame.mixer.stop()
    music = pygame.mixer.Sound("assets/Sounds/Music/menu.wav")
    music.play(-1)
    music.set_volume(0.5)
    
    while not level:
        level = mainMenu(screen, WIDTH, HEIGHT)

    music.stop()
    
    music = getLevelMusic(level)
    music.play(-1)
    music.set_volume(0.5)
        
    clock = pygame.time.Clock()
        
    # generate Player
    player = Player(100, 100, 50, 50)
    
    # generate blocks
    block_size = 96 
    
    floor = [Block(i * block_size, HEIGHT - block_size, block_size) for i in range(-WIDTH * 2// block_size, WIDTH * 3 // block_size)]
    
    # generate traps 
    traps = [
            Fire(100, HEIGHT - block_size - 64, 16, 32),
            Spike(100-block_size-32, HEIGHT - block_size - 32, 16, 16),
            Portal(100+5*block_size, HEIGHT - block_size - 66, 33, 33)
            ]   
    
    
    # generate collectibles
    
    collectibles = [
        Carrot(100+2*block_size, HEIGHT - block_size - 64, 32, 32),
        Potion(100+3*block_size, HEIGHT - block_size - 76, 38, 38),
        Banana(100+4*block_size, HEIGHT - 2 * block_size - 64, 32, 32)
        ]

    
    # create objects list
    objects = [*floor,
            Block(0, HEIGHT - block_size * 2, block_size),
            Block(block_size * 3, HEIGHT - block_size * 4, block_size),
            *traps
            ]
    
    # create enemy list
    enemies = [
        Slime(WIDTH, HEIGHT - block_size - 100, 32, 25, block_size * 3),
        Demon(0 - 5*block_size, HEIGHT - block_size - 142, 81, 71, block_size * 4)
    ]
    
    # load sounds
    sounds = loadSoundEffects()
    
    # background scrolling variables
    offset_x = 0
    scrolling_area_width = 200
    
    # check if game is paused
    IS_PAUSED = False
    # game run loop
    run = True
    while run:
        # manage Events
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # quit if players closes screen
                run = False
                break
            
            
            # manage game pausing
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    IS_PAUSED = not IS_PAUSED
                    if IS_PAUSED:
                        drawText(screen, "Game Paused!", 64, (0, 0, 0), WIDTH // 7, HEIGHT / 2.5)
                        pygame.display.flip()
                elif event.key == pygame.K_ESCAPE:
                    main(screen)
                
                if not IS_PAUSED and player.health > 0:
                    if event.key == pygame.K_w and player.jump_count < 2:
                        player.jump()
        if not IS_PAUSED:
            player.loop(FPS)
            loopTraps(traps)
            loopCollectibles(collectibles)
            loopEnemies(enemies, FPS)
            handleMovement(player, objects, collectibles, enemies, sounds)
            drawScreen(screen, level, player, objects, collectibles, enemies, offset_x)

            if ((player.rect.right - offset_x >= WIDTH - scrolling_area_width) and player.x_speed > 0) or (
                (player.rect.left - offset_x <= scrolling_area_width) and player.x_speed < 0):
                offset_x += player.x_speed
                

    pygame.quit()
    quit()

# works only if ran from main file
if __name__ == "__main__":
    main(screen)
    