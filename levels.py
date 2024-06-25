# import needed libraries and modules
import pygame

from settings import WIDTH, HEIGHT
from object_class import Block, Fire, Spike, Portal
from enemy_class import Slime, Demon
from collectible_class import Carrot, Banana, Potion

from assets_dim import *

def getLevelMusic(level):
    music = pygame.mixer.Sound(f'assets/Sounds/Music/lv{level}.wav')
    return music

def levelOne(): 
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
    floor = [Block(i * block_size, HEIGHT - block_size, block_size) for i in range(1, 5)]
    wall_left = [Block(0, HEIGHT - i * block_size, block_size) for i in range(1, HEIGHT // block_size)]
    
    # generate traps 
    traps = [
            *(Spike(8 * block_size + i * spike_width, HEIGHT + 6 * block_size - 2 * spike_height, spike_width, spike_height) for i in range(0, 6, 2)),
            *(Fire((11 + j) * block_size + i * fire_width, HEIGHT + 7 * block_size - 2 * fire_height, fire_width, fire_height) for j in range(2) for i in range(0, 6, 2)),
            Portal(36 * block_size - portal_width // 2, HEIGHT + 7 * block_size - 2 * portal_height, portal_width, portal_height),
            ]   
    
    
    # generate collectibles
    
    collectibles = [
        Carrot(4 * block_size, HEIGHT - block_size - carrot_height * 2, carrot_width, carrot_height),
        Carrot(7 * block_size, HEIGHT + 6 * block_size - 2 * carrot_height, carrot_width, carrot_height),
        Potion(17 * block_size, HEIGHT + 6 * block_size - 2 * potion_height, potion_width, potion_height),
        Carrot(11 * block_size + 2 * carrot_width, HEIGHT + 6 * block_size - 3 * carrot_height, carrot_width, carrot_height),
        *(Carrot((18 + i) * block_size, HEIGHT + (6 - i) * block_size - 2 * carrot_height, carrot_width, carrot_height) for i in range(4)),
        Banana(23 * block_size, HEIGHT + 2 * block_size - 2 * banana_height, banana_width, banana_height),
        *(Carrot((25 + i) * block_size + carrot_width, HEIGHT + (3 + i) * block_size - 2 * carrot_height, carrot_width, carrot_height) for i in range(4)),
        ]

    # create objects list
    objects = [*floor,
               *traps,
               *wall_left,
               *(Block(4 * block_size, HEIGHT + i * block_size, block_size) for i in range(6)),
               *(Block((4 + i) * block_size, HEIGHT + 6 * block_size, block_size) for i in range(7)),
               *(Block((10 + i) * block_size, HEIGHT + 7 * block_size, block_size) for i in range(4)),
               *(Block((13 + i) * block_size, HEIGHT + 6 * block_size, block_size) for i in range(5)),
               *(Block((18 + i) * block_size, HEIGHT + (6 - i) * block_size, block_size) for i in range(5)),
               *(Block((23 + i) * block_size, HEIGHT + 2 * block_size, block_size) for i in range(2)),
               *(Block((25 + i) * block_size, HEIGHT + (3 + i) * block_size, block_size) for i in range(5)),
               *(Block((30 + i) * block_size, HEIGHT + 7 * block_size, block_size) for i in range(7)),
               *(Block(37 * block_size, HEIGHT + (7 - i) * block_size, block_size) for i in range(10)),
            ]
    
    # create enemy list
    enemies = [
        Slime(9 * block_size, HEIGHT + 6 * block_size - 4 * slime_height, slime_width, slime_height, block_size),
        Slime(14 * block_size, HEIGHT + 6 * block_size - 4 * slime_height, slime_width, slime_height, 2 * block_size),
        Demon(31 * block_size, HEIGHT + 7 * block_size - 2 * demon_height, demon_width, demon_height, 3 * block_size),
    ]
    
    return objects, traps, collectibles, enemies

def levelFour():
    floor = [Block(i * block_size, HEIGHT - block_size, block_size) for i in range(block_size // block_size, 4)]
    wall_left = [Block(0, HEIGHT - i * block_size, block_size) for i in range(1, HEIGHT // block_size)]
    
    # generate traps 
    traps = [
            *(Spike((16 + i) * block_size + j * spike_width, HEIGHT + block_size - 2 * spike_height, spike_width, spike_height) for i in range(11) for j in range(0, 6, 2)),
            Fire(19 * block_size + 2 * fire_width, HEIGHT - 7 * block_size - 2 * fire_height, fire_width, fire_height),
            Portal(34 * block_size - portal_width // 2, HEIGHT - 19 * block_size - 2 * portal_height, portal_width, portal_height),
            ]   
    
    
    # generate collectibles
    
    collectibles = [
        *(Carrot((4 + i) * block_size - carrot_width // 2, HEIGHT - (i + 1) * block_size - 2 * carrot_height, carrot_width, carrot_height) for i in range(5)),
        Potion(15 * block_size + potion_width // 2, HEIGHT - 6 * block_size - 2 * potion_height, potion_width, potion_height),
        Banana(22 * block_size + banana_width, HEIGHT - 5 * block_size - 2 * banana_height, banana_width, banana_height),
        Carrot(26 * block_size + carrot_width // 2, HEIGHT - 13 * block_size - 2 * carrot_height, carrot_width, carrot_height),
        Carrot(23 * block_size + carrot_width // 2, HEIGHT - 14 * block_size - 2 * carrot_height, carrot_width, carrot_height),
        Potion(26 * block_size + potion_width // 2, HEIGHT - 16 * block_size - 2 * potion_height, potion_width, potion_height),
        ]

    # create objects list
    objects = [
                *floor,
                *traps,
                *wall_left,
                *(Block((4 + i) * block_size, HEIGHT - (i + 1) * block_size, block_size) for i in range(5)),
                *(Block((9 + i) * block_size, HEIGHT - 6 * block_size, block_size) for i in range(7)),

                *(Block(15 * block_size, HEIGHT - (5 - i) * block_size, block_size) for i in range(6)),
                *(Block((15 + i) * block_size, HEIGHT + block_size, block_size) for i in range(12)),
                *(Block(27 * block_size, HEIGHT - (-1 + i) * block_size, block_size) for i in range(21)),

                *(Block((18 + i) * block_size, HEIGHT - 7 * block_size, block_size) for i in range(3)),

                Block(22 * block_size, HEIGHT - 5 * block_size, block_size),
                Block(26 * block_size, HEIGHT - 7 * block_size, block_size),
                Block(26 * block_size, HEIGHT - 9 * block_size, block_size),
                
                *(Block((23 - i) * block_size, HEIGHT - 11 * block_size, block_size) for i in range(4)),
                
                Block(26 * block_size, HEIGHT - 13 * block_size, block_size),
                Block(23 * block_size, HEIGHT - 14 * block_size, block_size),
                Block(26 * block_size, HEIGHT - 16 * block_size, block_size),
                Block(26 * block_size, HEIGHT - 18 * block_size, block_size),
                
                *(Block((28 + i) * block_size, HEIGHT - 19 * block_size, block_size) for i in range(7)),
                *(Block(35 * block_size, HEIGHT - (19 + i) * block_size, block_size) for i in range(11)),
            ]
    
    # create enemy list
    enemies = [
        *(Slime((10 + i) * block_size, HEIGHT - 6 * block_size - 4 * slime_height, slime_width, slime_height, block_size) for i in range(0, 4, 3)),
        Slime(20 * block_size, HEIGHT - 11 * block_size - 4 * slime_height, slime_width, slime_height, 2 * block_size),
        Demon(28 * block_size, HEIGHT - 19 * block_size - 2 * demon_height, demon_width, demon_height, 3 * block_size),
    ]
    
    return objects, traps, collectibles, enemies

def levelFive():
    floor = [Block(i * block_size, HEIGHT - block_size, block_size) for i in range(block_size // block_size, 3)]
    wall_left = [Block(0, HEIGHT + i * block_size, block_size) for i in range(-10, 10)]
    floor_down = [Block(i * block_size, HEIGHT + 10 * block_size, block_size) for i in range(20)]
    wall_right = [Block(20 * block_size, HEIGHT + i * block_size, block_size) for i in range(-9, 11)]
    
    # generate traps 
    traps = [
            *(Fire((1 + i) * block_size + j * fire_width, HEIGHT + 10 * block_size - 2 * fire_height, fire_width, fire_height) for i in range(18) for j in range(0, 6, 2)),
            *(Spike(10 * block_size + j * spike_width, HEIGHT - 6 * block_size - 2 * spike_height, spike_width, spike_height) for j in range(0, 3, 2)),
            *(Spike(12 * block_size + j * spike_width, HEIGHT - 6 * block_size - 2 * spike_height, spike_width, spike_height) for j in range(2, 6, 2)),
            Portal(28 * block_size - portal_width // 2, HEIGHT - 9 * block_size - 2 * portal_height, portal_width, portal_height),
            ]   
    
    
    # generate collectibles
    
    collectibles = [
        Carrot(5 * block_size + carrot_width // 2, HEIGHT - 2 * block_size - 2 * carrot_height, carrot_width, carrot_height),
        Carrot(9 * block_size + carrot_width // 2, HEIGHT - 2 * block_size - 2 * carrot_height, carrot_width, carrot_height),
        Carrot(13 * block_size + carrot_width // 2, HEIGHT - 2 * block_size - 2 * carrot_height, carrot_width, carrot_height),
        Potion(14 * block_size + potion_width // 3, HEIGHT - 6 * block_size - 2 * potion_height, potion_width, potion_height),
        Banana(11 * block_size + banana_width // 2, HEIGHT - 6 * block_size - 2 * banana_height, banana_width, banana_height),
        Carrot(16 * block_size + carrot_width // 2, HEIGHT - 7 * block_size - 2 * carrot_height, carrot_width, carrot_height),
        Carrot(19 * block_size + carrot_width // 2, HEIGHT - 7 * block_size - 2 * carrot_height, carrot_width, carrot_height),
        Potion(20 * block_size + potion_width // 3, HEIGHT - 9 * block_size - 2 * potion_height, potion_width, potion_height),
        ]

    # create objects list
    objects = [
                *floor,
                *traps,
                *wall_left,
                *floor_down,
                *wall_right,
                Block(5 * block_size, HEIGHT - 2 * block_size, block_size),
                *(Block((9 + i) * block_size, HEIGHT - 2 * block_size, block_size) for i in range(5)),
                Block(14 * block_size, HEIGHT - 4 * block_size, block_size),
                Block(14 * block_size, HEIGHT - 6 * block_size, block_size),
                *(Block((12 - i) * block_size, HEIGHT - 6 * block_size, block_size) for i in range(3)),
                *(Block((16 + i) * block_size, HEIGHT - 7 * block_size, block_size) for i in range(5)),
                *(Block((21 + i) * block_size, HEIGHT - 9 * block_size, block_size) for i in range(8)),
                *(Block(29 * block_size, HEIGHT - (9 + i) * block_size, block_size) for i in range(5)),
            ]
    
    # create enemy list
    enemies = [
        Slime(10 * block_size, HEIGHT - 2 * block_size - 4 * slime_height, slime_width, slime_height, 2 * block_size),
        Demon(17 * block_size, HEIGHT - 7 * block_size - 2 * demon_height, demon_width, demon_height, block_size),
        Demon(21 * block_size, HEIGHT - 9 * block_size - 2 * demon_height, demon_width, demon_height, 3 * block_size),
    ]
    
    return objects, traps, collectibles, enemies

def levelSix():
    floor = [Block(i * block_size, HEIGHT - block_size, block_size) for i in range(block_size // block_size, 15)]
    wall_left = [Block(0, HEIGHT - i * block_size, block_size) for i in range(1, HEIGHT // block_size)]
    
    # generate traps 
    traps = [
            Fire(3 * block_size + 2 * fire_width, HEIGHT - block_size - 2 * fire_height, fire_width, fire_height),
            Spike(8 * block_size + 2 * spike_width, HEIGHT - block_size - 2 * spike_height, spike_width, spike_height),
            Fire(28 * block_size, HEIGHT - 4 * block_size - 2 * fire_height, fire_width, fire_height),
            Fire(28 * block_size + 2 * fire_width, HEIGHT - 4 * block_size - 2 * fire_height, fire_width, fire_height),
            Fire(28 * block_size + 4 * fire_width, HEIGHT - 4 * block_size - 2 * fire_height, fire_width, fire_height),
            Portal(34 * block_size - portal_width // 2, HEIGHT - 5 * block_size - 2 * portal_height, portal_width, portal_height),
            ]   
    
    
    # generate collectibles
    
    collectibles = [
        *(Carrot((6 + i) * block_size + carrot_width // 2, HEIGHT - block_size - 2 * carrot_height, carrot_width, carrot_height) for i in range(2)),
        *(Carrot((9 + i) * block_size + carrot_width // 2, HEIGHT - block_size - 2 * carrot_height, carrot_width, carrot_height) for i in range(2)),
        Potion(19 * block_size + potion_width // 2, HEIGHT - 5 * block_size - 2 * potion_height, potion_width, potion_height),
        Banana(28 * block_size + banana_width // 2, HEIGHT - 5 * block_size - 3 * banana_height, banana_width, banana_height),
        ]

    # create objects list
    objects = [*floor,
               *traps,
               *wall_left,
               *(Block((6 + i) * block_size, HEIGHT - 4 * block_size, block_size) for i in range(6)),
               Block(12 * block_size, HEIGHT - 3 * block_size, block_size),
               *(Block((15 + i) * block_size, HEIGHT - (1 + i) * block_size, block_size) for i in range(5)),
               *(Block((20 + i) * block_size, HEIGHT - 5 * block_size, block_size) for i in range(8)),
               *(Block((27 + i) * block_size, HEIGHT - 4 * block_size, block_size) for i in range(3)),
               *(Block((29 + i) * block_size, HEIGHT - 5 * block_size, block_size) for i in range(6)),
                *(Block(35 * block_size, HEIGHT - (5 + i) * block_size, block_size) for i in range(5)),
            ]
    
    # create enemy list
    enemies = [
        Demon(7 * block_size, HEIGHT - 4 * block_size - 2 * demon_height, demon_width, demon_height, 3 * block_size),
        Slime(20 * block_size, HEIGHT - 5 * block_size - 4 * slime_height, slime_width, slime_height, 2 * block_size),
        Demon(23 * block_size, HEIGHT - 5 * block_size - 2 * demon_height, demon_width, demon_height, 3 * block_size),
        Demon(30 * block_size, HEIGHT - 5 * block_size - 2 * demon_height, demon_width, demon_height, 2 * block_size),
    ]
    
    return objects, traps, collectibles, enemies

def levelSeven():
    floor = [Block(i * block_size, HEIGHT - block_size, block_size) for i in range(block_size // block_size, WIDTH * 3 // block_size)]
    wall_left = [Block(0, HEIGHT - i * block_size, block_size) for i in range(1, HEIGHT // block_size)]
    
    # generate traps 
    traps = [
            *(Spike((3 + i) * block_size + j * spike_width, HEIGHT - block_size - spike_height * 2, spike_width, spike_height) for i in range(2) for j in range(0, 6, 2)),
            *(Spike((6 + i) * block_size + j * spike_width, HEIGHT - block_size - 2 * spike_height, spike_width, spike_height) for i in range(7) for j in range(0, 6, 2)),
            *(Fire((14 + i) * block_size + j * fire_width, HEIGHT - block_size - 2 * fire_height, fire_width, fire_height) for i in range(2) for j in range(0, 6, 2)),
            *(Fire(25 * block_size + j * fire_width, HEIGHT - block_size - 2 * fire_height, fire_width, fire_height) for j in range(2, 6, 2)),
            *(Fire(26 * block_size + j * fire_width, HEIGHT - block_size - 2 * fire_height, fire_width, fire_height) for j in range(0, 6, 2)),
            *(Fire(27 * block_size + j * fire_width, HEIGHT - block_size - 2 * fire_height, fire_width, fire_height) for j in range(0, 4, 2)),
            Portal(48 * block_size - portal_width // 2, HEIGHT - 5 * block_size - 2 * portal_height, portal_width, portal_height),
            ]   
    
    
    # generate collectibles
    
    collectibles = [
        Carrot(5 * block_size + carrot_width // 2, HEIGHT - 3 * block_size - 2 * carrot_height, carrot_width, carrot_height),
        Carrot(13 * block_size + carrot_width // 2, HEIGHT - 4 * block_size - 2 * carrot_height, carrot_width, carrot_height),
        Potion(16 * block_size + potion_width // 2, HEIGHT - block_size - 2 * potion_height, potion_width, potion_height),
        Banana(26 * block_size + banana_width // 2, HEIGHT - 3.5 * block_size - 2 * banana_height, banana_width, banana_height),
        *(Carrot((32 + i) * block_size - carrot_width // 2, HEIGHT - (2 + i) * block_size - 2 * carrot_height, carrot_width, carrot_height) for i in range(3)),
        Potion(35 * block_size + potion_width // 2, HEIGHT - 5 * block_size - 2 * potion_height, potion_width, potion_height),
        ]

    # create objects list
    objects = [
                *floor,
                *traps,
                *wall_left,
                *(Block(5 * block_size, HEIGHT - (2 + i) * block_size, block_size) for i in range(2)),
                *(Block((8 + i) * block_size, HEIGHT - 3 * block_size, block_size) for i in range(3)),
                *(Block(13 * block_size, HEIGHT - (2 + i) * block_size, block_size) for i in range(3)),
                *(Block((31 + i) * block_size, HEIGHT - (1 + i) * block_size, block_size) for i in range(5)),
                *(Block((36 + i) * block_size, HEIGHT - 5 * block_size, block_size) for i in range(13)),
                *(Block(49 * block_size, HEIGHT - (5 + i) * block_size, block_size) for i in range(6)),
            ]
    
    # create enemy list
    enemies = [
        Demon(8 * block_size, HEIGHT - 3 * block_size - 2 * demon_height, demon_width, demon_height, 2 * block_size),
        *(Slime((18 + i) * block_size, HEIGHT - block_size - 4 * slime_height, slime_width, slime_height, 2 * block_size) for i in range(0, 6, 2)),
        Demon(36 * block_size, HEIGHT - 5 * block_size - 2 * demon_height, demon_width, demon_height, 3 * block_size),
        Demon(39 * block_size, HEIGHT - 5 * block_size - 2 * demon_height, demon_width, demon_height, 3 * block_size),
        Demon(42 * block_size, HEIGHT - 5 * block_size - 2 * demon_height, demon_width, demon_height, 3 * block_size),
    ]
    
    return objects, traps, collectibles, enemies

def levelEight():
    floor = [Block(i * block_size, HEIGHT - block_size, block_size) for i in range(block_size // block_size, WIDTH * 3 // block_size)]
    wall_left = [Block(0, HEIGHT - i * block_size, block_size) for i in range(1, HEIGHT // block_size)]
    
    # generate traps 
    traps = [
            
            ]   
    
    
    # generate collectibles
    
    collectibles = [
        ]

    # create objects list
    objects = [*floor,
               *traps,
               *wall_left,
            ]
    
    # create enemy list
    enemies = [
    ]
    
    return objects, traps, collectibles, enemies

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