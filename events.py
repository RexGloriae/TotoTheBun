# import needed libraries and modules
import pygame

from settings import PLAYER_SPEED

def touchesCollectible(player, collectibles):
    collided_items = []
    
    for item in collectibles:
        if pygame.sprite.collide_mask(player, item):
            item.touched += 1
            collided_items.append(item)
    
    return collided_items


def handleCollectibles(player, collectibles, sounds):
    to_check = touchesCollectible(player, collectibles)
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

def isEnemyBeingHit(player, enemies, dy):
    enemy_hit = None
    if dy > 0:
        for ent in enemies:
            if ent.lives and pygame.sprite.collide_mask(player, ent):
                height_index = 1
                if ent.name == "demon":
                    height_index = 2
                if player.rect.bottom <= ent.rect.top + ent.rect.height // height_index:
                    player.rect.bottom = ent.rect.top
                    player.landed()
                    enemy_hit = ent
                    break    
                
    return enemy_hit

def handleEnemies(player, enemies, sounds):
    enemy_hit = isEnemyBeingHit(player, enemies, player.y_speed)
    
    attacker_left = isEnemyHitting(player, enemies, -PLAYER_SPEED * 2)
    attacker_right = isEnemyHitting(player, enemies, PLAYER_SPEED * 2)
        
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
                pygame.mixer.stop()
            curr_sound.play()



def handleVerticalCollision(player, objects, dy):
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
        
    return collided_objects

def handleCollisions(player, objects, collide_left, collide_right, sounds):
    vertical_collide = handleVerticalCollision(player, objects, player.y_speed)
    
    to_check = [collide_left, collide_right, *vertical_collide]
    
    for obj in to_check:
        if obj and obj.name == "fire" and player.invincibility == False:
            player.getHit()
            player.health -= 1
            player.invincibility = True
            curr_sound = sounds["player_hit"]
            if player.health == 0:
                curr_sound = sounds["player_death"]
                pygame.mixer.stop()
            curr_sound.play()
        elif obj and obj.name == "spike" and player.invincibility == False:
            player.getHit()
            player.health -= 1
            player.invincibility = True
            curr_sound = sounds["player_hit"]
            if player.health == 0:
                curr_sound = sounds["player_death"]
                pygame.mixer.stop()
            curr_sound.play()
        elif obj and obj.name == "portal":
            if player.will_teleport == False:
                pygame.mixer.stop()
                curr_sound = sounds["level_finish"]
                curr_sound.set_volume(0.5)
                curr_sound.play()
                player.will_teleport = True

def collide(player, objects, dx):
    player.move(dx, 0)
    player.update()
    
    collided_object = None
    
    for obj in objects:
        if pygame.sprite.collide_mask(player, obj):
            collided_object = obj
            break
        
    player.move(-dx, 0)
    player.update()
    
    return collided_object

def handleMovement(player, objects, sounds):
    keys = pygame.key.get_pressed()
    
    collide_left = collide(player, objects, -PLAYER_SPEED * 2)
    collide_right = collide(player, objects, PLAYER_SPEED * 2)
    
    player.x_speed = 0
    if player.health > 0:
        if keys[pygame.K_a] and not collide_left:
            player.moveLeft(PLAYER_SPEED)
        if keys[pygame.K_d] and not collide_right:
            player.moveRight(PLAYER_SPEED)
            
    handleCollisions(player, objects, collide_left, collide_right, sounds)