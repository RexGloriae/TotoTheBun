# import needed libraries
import pygame
from os import listdir
from os.path import isfile, join

from img import flipImg

def loadSoundEffects():
    all_sounds = {}
    
    banana = pygame.mixer.Sound("../assets/Sounds/Effects/banana.wav")
    all_sounds["banana"] = banana
    
    carrot = pygame.mixer.Sound("../assets/Sounds/Effects/carrot.wav")
    all_sounds["carrot"] = carrot
    
    demon_death = pygame.mixer.Sound("../assets/Sounds/Effects/demon_death.wav")
    all_sounds["demon_death"] = demon_death
    
    enemy_hit = pygame.mixer.Sound("../assets/Sounds/Effects/enemy_hit.wav")
    all_sounds["enemy_hit"] = enemy_hit
    
    health = pygame.mixer.Sound("../assets/Sounds/Effects/health_potion.wav")
    all_sounds["health_potion"] = health
    
    lvl = pygame.mixer.Sound("../assets/Sounds/Effects/level_finish.wav")
    all_sounds["level_finish"] = lvl
    
    death = pygame.mixer.Sound("../assets/Sounds/Effects/player_death.wav")
    all_sounds["player_death"] = death
    
    hit = pygame.mixer.Sound("../assets/Sounds/Effects/player_hit.flac")
    all_sounds["player_hit"] = hit
    
    slime = pygame.mixer.Sound("../assets/Sounds/Effects/slime_death.wav")
    all_sounds["slime_death"] = slime
    
    return all_sounds

def loadCarrotCollectible(width, height):
    carrot = pygame.image.load(f'../assets/Collectibles/Carrot.png').convert_alpha()
    scale = height / carrot.get_height()
    new_width = carrot.get_width() * scale
    new_height = carrot.get_height() * scale
    carrot = pygame.transform.scale(carrot, (new_width, new_height))
    
    return pygame.transform.scale2x(carrot)

def loadBananaCollectible(width, height):
    banana = pygame.image.load(f'../assets/Collectibles/Banana_Peeled.png').convert_alpha()
    scale = height / banana.get_height()
    new_width = banana.get_width() * scale
    new_height = banana.get_height() * scale
    banana = pygame.transform.scale(banana, (new_width, new_height))
    
    return pygame.transform.scale2x(banana)

def loadHealthPotionCollectible(width, height):
    potion = pygame.image.load(f'../assets/Collectibles/Health_Potion.png').convert_alpha()
    scale = height / potion.get_height()
    new_width = potion.get_width() * scale
    new_height = potion.get_height() * scale
    potion = pygame.transform.scale(potion, (new_width, new_height))
    
    return pygame.transform.scale2x(potion)

def loadFireSheet(width, height):
    path = join("../assets", "Traps", "Fire")
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
    spike = pygame.image.load(f'../assets/Traps/Spike/Idle.png').convert_alpha()
    scale = height / spike.get_height()
    new_width = spike.get_width() * scale
    new_height = spike.get_height() * scale
    spike = pygame.transform.scale(spike, (new_width, new_height))
    
    return pygame.transform.scale2x(spike)

def loadPortal(width, height):
    portal = []
    for i in range(1, 7):
        img = pygame.image.load(f'../assets/Portal/p{i}.png').convert_alpha()
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
        running_sprite = pygame.image.load(f'../assets/Player_Sprites/Running/a{i}.png').convert_alpha()
        scale = player_height / running_sprite.get_height()
        new_width = running_sprite.get_width() * scale
        new_height = running_sprite.get_height() * scale
        running_sprite = pygame.transform.scale(running_sprite, (new_width, new_height))
        running_sprites.append(running_sprite)
    
    all_sprites["run" + "_right"] = running_sprites
    all_sprites["run" + "_left"] = flipImg(running_sprites)
        
    # Load Jumping Sprites
    jumping_sprites = []
    
    sprite = pygame.image.load(f'../assets/Player_Sprites/Jump/a2.png').convert_alpha()
    scale = player_height / sprite.get_height()
    new_width = sprite.get_width() * scale
    new_height = sprite.get_height() * scale
    sprite = pygame.transform.scale(sprite, (new_width, new_height))
    jumping_sprites.append(sprite)
    
    all_sprites["jump" + "_right"] = jumping_sprites
    all_sprites["jump" + "_left"] = flipImg(jumping_sprites)
    
    # Load Fall Sprites
    falling_sprites = []
    
    sprite = pygame.image.load(f'../assets/Player_Sprites/Jump/a5.png').convert_alpha()
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
        sprite = pygame.image.load(f'../assets/Player_Sprites/Faint/a{i}.png').convert_alpha()
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
        sprite = pygame.image.load(f'../assets/Player_Sprites/Dizzy/a{i}.png').convert_alpha()
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
        sprite = pygame.image.load(f'../assets/Player_Sprites/Idle/a{i}.png').convert_alpha()
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
        sprite = pygame.image.load(f'../assets/Player_Sprites/Shoot/a{i}.png').convert_alpha()
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
        sprite = pygame.image.load(f'../assets/Player_Sprites/Explode/a{i}.png').convert_alpha()
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
        sprite = pygame.image.load(f'../assets/Player_Sprites/HearTile/Cuore{i}.png').convert_alpha()
        scale = height / sprite.get_height()
        new_width = sprite.get_width() * scale
        new_height = sprite.get_height() * scale
        sprite = pygame.transform.scale(sprite, (new_width, new_height))
        health_sprites.append(sprite)
    
    return health_sprites

# load terrain
def loadBlock(size):
    path = join("../assets", "Terrain", "Terrain.png")
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
        path = "../assets/Enemy/Demon/"
    else:
        path = "../assets/Enemy/Slime/"
        
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
    
# background function
def getBackground(level):
    if level > 8:
        level = level%8 + 1
    if level == 1:
        img = pygame.image.load("../assets/Backgrounds/m1/PRE_ORIG_SIZE.png")
    elif level == 2:
        img = pygame.image.load("../assets/Backgrounds/m2/PRE_ORIG_SIZE.png")
    elif level == 3:
        img = pygame.image.load("../assets/Backgrounds/m3/PRE_ORIG_SIZE.png")
    elif level == 4:
        img = pygame.image.load("../assets/Backgrounds/m4/PRE_ORIG_SIZE.png")
    elif level == 5:
        img = pygame.image.load("../assets/Backgrounds/m5/PRE_ORIG_SIZE.png")
    elif level == 6:
        img = pygame.image.load("../assets/Backgrounds/m6/PRE_ORIG_SIZE.png")
    elif level == 7:
        img = pygame.image.load("../assets/Backgrounds/m7/PRE_ORIG_SIZE.png")
    elif level == 8:
        img = pygame.image.load("../assets/Backgrounds/m8/PRE_ORIG_SIZE.png")
    
    return img

def loadLevelImgs(width, height):
    images = []
    for i in range(1, 9):
        img = pygame.image.load(f'../assets/Level_Buttons/0{i}.png').convert_alpha()
        scale = height / img.get_height()
        new_width = img.get_width() * scale
        new_height = img.get_height() * scale
        img = pygame.transform.scale(img, (new_width, new_height))
        images.append(pygame.transform.scale2x(img))
        
    return images

def loadBackImg(width, height):
    img = pygame.image.load("../assets/Menu_Buttons/4.png").convert_alpha()
    scale = height / img.get_height()
    new_width = img.get_width() * scale
    new_height = img.get_height() * scale
    img = pygame.transform.scale(img, (new_width, new_height))
    
    return img