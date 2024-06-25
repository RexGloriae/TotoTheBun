# import needed libraries and modules
import pygame

from loaders import loadLevelImgs, loadBackImg
from settings import WIDTH, HEIGHT
from screen import drawText

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
    text = "multiverse. Your goal is to go search on every level for the"
    drawText(screen, text, 16, (0, 0, 0), 10, curr_height)
    drawText(screen, text, 16, (255, 255, 255), 10, curr_height - 2.5)

    text = "portal that will get you home. On every level you have"
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