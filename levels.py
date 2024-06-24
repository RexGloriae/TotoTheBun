# import needed libraries and modules
import pygame

from settings import WIDTH, HEIGHT
from object_class import Block, Fire, Spike, Portal
from enemy_class import Slime, Demon
from collectible_class import Carrot, Banana, Potion

def getLevelMusic(level):
    music = pygame.mixer.Sound(f'assets/Sounds/Music/lv{level}.wav')
    return music

def levelOne():
    block_size = 96
    
    carrot_width = 32
    carrot_height = 32
    banana_width = 32
    banana_height = 32
    potion_width = 38
    potion_height = 38
    
    fire_width = 16
    fire_height = 32
    spike_width = 16
    spike_height = 16
    portal_width = 33 * 2
    portal_height = 33 * 2
    
    slime_width = 32
    slime_height = 25 # magnified 4 times
    demon_width = 81
    demon_height = 71
    
    # all others - magnified twice
    
    
    floor = [Block(i * block_size, HEIGHT - block_size, block_size) for i in range(block_size // block_size, WIDTH * 3 // block_size)]
    wall_left = [Block(0, HEIGHT - i * block_size, block_size) for i in range(1, HEIGHT // block_size)]
    
    # generate traps 
    traps = [
            *(Spike((4 + i) * block_size, HEIGHT - block_size - spike_height * 2, spike_width, spike_height) for i in range(3)),
            *(Spike((4 + i) * block_size + spike_width * 2, HEIGHT - block_size - spike_height * 2, spike_width, spike_height) for i in range(3)),
            *(Spike((4 + i) * block_size + spike_width * 4, HEIGHT - block_size - spike_height * 2, spike_width, spike_height) for i in range(3)),
            Fire(13 * block_size + 2 * fire_width, HEIGHT - block_size - 2 * fire_height, fire_width, fire_height),
            *(Spike(27 * block_size + spike_width * i, HEIGHT - block_size - spike_width * 2, spike_width, spike_height) for i in range(0, 5, 2)),
            Portal(35 * block_size, HEIGHT - 8 * block_size - 2 * portal_height, portal_width, portal_height),
            ]   
    
    
    # generate collectibles
    
    collectibles = [
        Carrot(2 * block_size, HEIGHT - block_size - carrot_height * 2, carrot_width, carrot_height),
        *(Carrot((3 + i) * block_size, HEIGHT - 3 * block_size - 2 * carrot_height, carrot_width, carrot_height) for i in range(1, 5, 2)),
        Potion(18 * block_size, HEIGHT - block_size - 2 * potion_height, potion_width, potion_height),
        Carrot(21 * block_size + carrot_width, HEIGHT - 2 * block_size - 2 * carrot_height, carrot_width, carrot_height),
        Banana(25 * block_size + banana_width, HEIGHT - block_size - 2 * banana_height, banana_width, banana_height),
        ]

    # create objects list
    objects = [*floor,
               *traps,
               *wall_left,
               *(Block((3 + i) * block_size, HEIGHT - 3 * block_size, block_size) for i in range(5)),
               *(Block((16 + i) * block_size, HEIGHT - 3 * block_size, block_size) for i in range(5)),
               Block(14 * block_size, HEIGHT - 2 * block_size, block_size),
               *(Block((23 + i) * block_size, HEIGHT - 4 * block_size, block_size) for i in range(4)),
               *(Block(23 * block_size, HEIGHT - i * block_size, block_size) for i in range (2, 5)),
               Block(28 * block_size, HEIGHT - 2 * block_size, block_size),
               Block(28 * block_size, HEIGHT - 6 * block_size, block_size),
               *(Block((30 + i) * block_size, HEIGHT - 8 * block_size, block_size) for i in range(6)),
               *(Block(30 * block_size, HEIGHT - i * block_size, block_size) for i in range (2, 8)),
            ]
    
    # create enemy list
    enemies = [
        Slime(5 * block_size, HEIGHT - 3 * block_size - 4 * slime_height, slime_width, slime_height, 2 * block_size),
        Slime(8 * block_size, HEIGHT - block_size - 4 * slime_height, slime_width, slime_height, 4 * block_size),
        Slime(23 * block_size, HEIGHT - 4 * block_size - 4 * slime_height, slime_width, slime_height, 3 * block_size),
        Demon(30 * block_size, HEIGHT - 8 * block_size - 2 * demon_height, demon_width, demon_height, 3 * block_size),
    ]
    
    return objects, traps, collectibles, enemies

def levelTwo():
    block_size = 96
    
    carrot_width = 32
    carrot_height = 32
    banana_width = 32
    banana_height = 32
    potion_width = 38
    potion_height = 38
    
    fire_width = 16
    fire_height = 32
    spike_width = 16
    spike_height = 16
    portal_width = 33 * 2
    portal_height = 33 * 2
    
    slime_width = 32
    slime_height = 25 # magnified 4 times
    demon_width = 81
    demon_height = 71
    
    # all others - magnified twice
    
    
    floor = [Block(i * block_size, HEIGHT - block_size, block_size) for i in range(-2 * block_size // block_size, 8)]
    wall_left = [Block(-2 * block_size, HEIGHT - i * block_size, block_size) for i in range(1, 2 * HEIGHT // block_size)]
    
    # generate traps 
    traps = [
            *(Fire((2 + i) * block_size + 2 * j * fire_width, HEIGHT - block_size - 2 * fire_height, fire_width, fire_height) for i in range(2) for j in range(3)),
            *(Spike(6 * block_size + i * spike_width, HEIGHT - block_size - 2 * spike_height, spike_width, spike_height) for i in range(0, 6, 2)),
            Fire(10 * block_size + 2 * fire_width, HEIGHT - 4 * block_size - 2 * fire_height, fire_width, fire_height),
            *(Spike(15 * block_size + i * spike_width, HEIGHT - 11 * block_size - 2 * spike_height, spike_width, spike_height) for i in range(0, 6, 2)),
            Portal(13 * block_size, HEIGHT - 11 * block_size - 2 * portal_height, portal_width, portal_height)
            ]   
    
    
    # generate collectibles
    
    collectibles = [
        Banana(-block_size, HEIGHT - block_size - 2 * banana_height, banana_width, banana_height),
        Carrot(4 * block_size + carrot_width, HEIGHT - 2 * block_size - 2 * carrot_height, carrot_width, carrot_height),
        Carrot(11 * block_size + carrot_width, HEIGHT - 4 * block_size - carrot_height * 2, carrot_width, carrot_height),
        Potion(-block_size, HEIGHT - 6 * block_size - 2 * potion_height, potion_width, potion_height),
        *(Carrot(i * block_size + carrot_width, HEIGHT - (10 + i) * block_size - 2 * carrot_height, carrot_width, carrot_height) for i in range(3)),
        Carrot(10 * block_size, HEIGHT - 15 * block_size - carrot_height // 2, carrot_width, carrot_height),
        Potion(16 * block_size + potion_width // 2, HEIGHT - 15 * block_size - 2 * potion_height, potion_width, potion_height),
        ]

    # create objects list
    objects = [*floor,
               *traps,
               *wall_left,
               Block(4 * block_size, HEIGHT - 2 * block_size, block_size),
               *(Block(7 * block_size, HEIGHT - (2 + i) * block_size, block_size) for i in range(2)),
               *(Block((7 + i) * block_size, HEIGHT - 4 * block_size, block_size) for i in range(6)),
               *(Block(12 * block_size, HEIGHT - (5 + i) * block_size, block_size) for i in range(10)),
               Block(4 * block_size, HEIGHT - 6 * block_size, block_size),
               *(Block((1 - i) * block_size, HEIGHT - 6 * block_size, block_size) for i in range(3)),
               Block(- block_size, HEIGHT - 8 * block_size, block_size),
               *(Block(i * block_size, HEIGHT - (10 + i) * block_size, block_size) for i in range(3)),
               *(Block((3 + i) * block_size, HEIGHT - 13 * block_size, block_size) for i in range(6)),
               *(Block((12 + i) * block_size, HEIGHT - 15 * block_size, block_size) for i in range(5)),
               *(Block((13 + i) * block_size, HEIGHT - 11 * block_size, block_size) for i in range(8)),
               *(Block(21 * block_size, HEIGHT - (10 + i) * block_size, block_size) for i in range(10)),
            ]
    
    # create enemy list
    enemies = [
        Slime(3 * block_size, HEIGHT - 13 * block_size - 4 * slime_height, slime_width, slime_height, 2 * block_size),
        Slime(6 * block_size, HEIGHT - 13 * block_size - 4 * slime_height, slime_width, slime_height, 2 * block_size),
        Slime(13 * block_size, HEIGHT - 15 * block_size - 4 * slime_height, slime_width, slime_height, 2 * block_size),
        Demon(17 * block_size, HEIGHT - 11 * block_size - 2 * demon_height, demon_width, demon_height, 3 * block_size),
    ]
    
    return objects, traps, collectibles, enemies

def levelThree():
    pass

def levelFour():
    pass

def levelFive():
    pass

def levelSix():
    pass

def levelSeven():
    pass

def levelEight():
    pass

def loadLevel(level):
    if level == 1:
        return levelOne()
    elif level == 2:
        return levelTwo()
    elif level == 3:
        return levelThree()
    elif level == 4:
        return levelFour()
    elif level == 5:
        return levelFive()
    elif level == 6:
        return levelSix()
    elif level == 7:
        return levelSeven()
    elif level == 8:
        return levelEight()