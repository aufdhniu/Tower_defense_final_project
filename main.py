import pygame as pg
import constants as c
import time
from enemy import Enemy
from world import World
from turret import Turret



#initialise pygame
pg.init()

#create clock
clock = pg.time.Clock()

#game window size 
screen = pg.display.set_mode((c.SCREEN_WIDTH, c.SCREEN_HEIGHT))
pg.display.set_caption("Tower Defence")

#load images
map_image = pg.image.load("levels/level1.png")
cursor_turret = pg.image.load("assets/images/turrets/cursor_turret.png").convert_alpha()
enemy_image = pg.image.load("assets/images/enemy/enemy_3/move_000.png").convert_alpha()

#create groups
enemy_group = pg.sprite.Group()
turret_group = pg.sprite.Group()

def create_turret(mouse_pos):
    # mouse_tile_x = mouse_pos[0] // 64
    # mouse_tile_y = mouse_pos[1] // 100

    can_created = True
    for not_use in world.map_not_avaible : 
        if (mouse_pos[0]-not_use[0])**2 + (mouse_pos[1]-not_use[1])**2 < 80**2:
            can_created = False
        
          
    if(can_created):    
        world.map_not_avaible.append((mouse_pos[0],mouse_pos[1]))
        turret = Turret(cursor_turret,mouse_pos)
        turret_group.add(turret)


world = World(map_image)
enemy = Enemy(world.waypoints, enemy_image)
enemy_group.add(enemy)

print(enemy_group)
pos_list = []

#game loop
run = True
while run:
    
    #FPS
    clock.tick(c.FPS)
    
    
    #update groups
    enemy_group.update()
    turret_group.update()
    
    for turret in turret_group:
        turret.deal_damage(enemy_group)

    #draw groups
    screen.fill("grey100")
    world.draw(screen)
    enemy_group.draw(screen)

    for enemy in enemy_group:
        enemy.draw_health(screen)

    turret_group.draw(screen)
    
    #draw enemy path
    # pg.draw.lines(screen, "grey0", False, world.waypoints)
    

    #event handler
    for event in pg.event.get():
        #quit program
        if event.type == pg.QUIT:
            run = False
        
        if event.type == pg.MOUSEBUTTONDOWN and event.button == 1 :
            
            mouse_pos = pg.mouse.get_pos()
            if mouse_pos[0] < c.SCREEN_WIDTH and mouse_pos[1] < c.SCREEN_HEIGHT:
                create_turret(mouse_pos)
                
        
    #     pos = pg.mouse.get_pos()
    #     if event.type == pg.MOUSEBUTTONDOWN:
    #         pos_list.append(pos)
    #         print(pos_list)
    # for p in pos_list:
    #     pg.draw.circle(screen, (255, 0, 0), (p[0], p[1]), 5, 0)
    pg.display.flip()

pg.quit()
