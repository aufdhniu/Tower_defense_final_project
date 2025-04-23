import pygame as pg
from enemy import Enemy
from world import World
from turret import Turret
from button import Button
import constant as c
import random

# initialise pygame
pg.init()

# สร้าง clock สำหรับ FPS
clock = pg.time.Clock()

# สร้าง window + config(ขนาด,ชื่อ)
screen = pg.display.set_mode((c.SCREEN_WIDTH+c.SIDE_PANEL, c.SCREEN_HEIGHT))
pg.display.set_caption("Tower Defence")

# gamse variables
placing_turrets = False
selected_turret = None

# load images
enemy_image = pg.image.load(
    './assets/images/enemies/move/enemy_1/move_000.png').convert_alpha()
map_image = pg.image.load(
    './levels/level1.png').convert_alpha()
cursor_turret = pg.image.load(
    './assets/images/turrets/cursor_turret.png').convert_alpha()
panel_image = pg.image.load(
    './assets/images/panel/panel.png').convert_alpha()
button_image = pg.image.load(
    './assets/images/buttons/button.png').convert_alpha()
button_hover_image = pg.image.load(
    './assets/images/buttons/button_hover.png').convert_alpha()
button_star_image = pg.image.load(
    './assets/images/buttons/button_star.png').convert_alpha()
button_star_hover_image = pg.image.load(
    './assets/images/buttons/button_star_hover.png').convert_alpha()

# transform scale image
map_image = pg.transform.scale(map_image, (c.SCREEN_WIDTH, c.SCREEN_HEIGHT))
enemy_image = pg.transform.scale(enemy_image, (120, 100))
cursor_turret = pg.transform.scale(cursor_turret, (30, 30))
button_image = pg.transform.scale(button_image, (40, 40))
button_hover_image = pg.transform.scale(button_hover_image, (40, 40))
button_star_image = pg.transform.scale(button_star_image, (40, 40))
button_star_hover_image = pg.transform.scale(button_star_hover_image, (40, 40))
panel_image = pg.transform.scale(panel_image, (c.SIDE_PANEL, c.SCREEN_HEIGHT))

# create waypoints (ทางเดินของ enemy)
pos_list = []


def check_create_turret(mouse_pos):
    can_create = True
    for zone in world.map_blocked:
        if (mouse_pos[0]-zone[0])**2 + (mouse_pos[1]-zone[1])**2 < 65**2:
            can_create = False
    return can_create


def create_turret(mouse_pos):
    if (check_create_turret(mouse_pos)):
        world.turret_pos.append((mouse_pos[0], mouse_pos[1]))
        world.map_blocked.append((mouse_pos[0], mouse_pos[1]))
        turret = Turret(cursor_turret, mouse_pos)
        turret_group.add(turret)


def select_turret(mouse_pose):
    for turret in turret_group:
        if (mouse_pos[0]-turret.pos[0])**2 + (mouse_pos[1]-turret.pos[1])**2 < 40**2:
            return turret


def clear_selection():
    for turret in turret_group:
        turret.selected = False


def avaible_zone(mouse_pos, color):
    range_image = pg.Surface((80*2, 80*2))
    range_image.fill((0, 0, 0))
    range_image.set_colorkey((0, 0, 0))
    pg.draw.circle(range_image, color,
                   (80, 80), 80)
    range_image.set_alpha(100)
    range_rect = range_image.get_rect()
    range_rect.center = mouse_pos
    screen.blit(range_image, range_rect)


# create world
world = World(map_image)

# create groups
enemy_group = pg.sprite.Group()
turret_group = pg.sprite.Group()


enemy = Enemy(world.waypoints, enemy_image , random.randint(1,9),random.uniform(0.8,1.6))
enemy1 = Enemy(world.waypoints, enemy_image , random.randint(1,9),2)
enemy2 = Enemy(world.waypoints, enemy_image , random.randint(1,9),1)
enemy3 = Enemy(world.waypoints, enemy_image , random.randint(1,9),random.uniform(0.8,1.6))
enemy4 = Enemy(world.waypoints, enemy_image , random.randint(1,9),random.uniform(0.8,1.6))
enemy5 = Enemy(world.waypoints, enemy_image , random.randint(1,9),4)
enemy6 = Enemy(world.waypoints, enemy_image , random.randint(1,9),random.uniform(0.8,1.6))
enemy7 = Enemy(world.waypoints, enemy_image , random.randint(1,9),1.5)
enemy8 = Enemy(world.waypoints, enemy_image , random.randint(1,9),random.uniform(0.8,1.6))
enemy9 = Enemy(world.waypoints, enemy_image , random.randint(1,9),random.uniform(0.8,1.6))
enemy10 = Enemy(world.waypoints, enemy_image , random.randint(1,9),random.uniform(0.8,1.6))
enemy11 = Enemy(world.waypoints, enemy_image , random.randint(1,9),0.5)
enemy12 = Enemy(world.waypoints, enemy_image , random.randint(1,9),random.uniform(0.8,1.6))
enemy13 = Enemy(world.waypoints, enemy_image , random.randint(1,9),random.uniform(0.8,1.6))
enemy14 = Enemy(world.waypoints, enemy_image , random.randint(1,9),2)
enemy15 = Enemy(world.waypoints, enemy_image , random.randint(1,9),random.uniform(0.8,1.6))
enemy16 = Enemy(world.waypoints, enemy_image , random.randint(1,9),random.uniform(0.8,1.6))
enemy17 = Enemy(world.waypoints, enemy_image , random.randint(1,9),1.7)
enemy18 = Enemy(world.waypoints, enemy_image , random.randint(1,9),random.uniform(0.8,1.6))

enemy_group.add(enemy)
enemy_group.add(enemy1)
enemy_group.add(enemy2)
enemy_group.add(enemy3)
enemy_group.add(enemy4)
enemy_group.add(enemy5)
enemy_group.add(enemy6)
enemy_group.add(enemy7)
enemy_group.add(enemy8)
enemy_group.add(enemy9)
enemy_group.add(enemy10)
enemy_group.add(enemy11)
enemy_group.add(enemy12)
enemy_group.add(enemy13)
enemy_group.add(enemy14)
enemy_group.add(enemy15)
enemy_group.add(enemy16)
enemy_group.add(enemy17)
enemy_group.add(enemy18)


# create buttons
turret_button = Button(c.SCREEN_WIDTH + 30, 120,
                       button_image, button_hover_image)
cancel_button = Button(c.SCREEN_WIDTH + 30, 200,
                       button_image, button_hover_image)
upgrade_turret_button = Button(c.SCREEN_WIDTH + 30, 200,
                               button_star_image, button_star_hover_image)


# game loop
run = True
while run:

    # FPS
    clock.tick(60)

    ####################
    # UPDATING SECTION
    ####################

    # update activity ต่างๆของ enemy ใน group
    enemy_group.update()
    turret_group.update(enemy_group)

    # highlight selected turret
    if selected_turret:
        selected_turret.selected = True

    ####################
    # DRAWING SECTION
    ####################

    screen.fill("grey100")

    # draw map
    world.draw(screen)

    # draw groups
    for turret in turret_group:
        turret.draw(screen)
    enemy_group.draw(screen)

    # draw buttons
    screen.blit(panel_image, (c.SCREEN_WIDTH, 0))

    # turret condition
    
    if turret_button.draw(screen):
        placing_turrets = True

    if placing_turrets == True:

        cursor_rect = cursor_turret.get_rect()
        cursor_pos = pg.mouse.get_pos()
        cursor_rect.center = cursor_pos
        if cursor_pos[0] <= c.SCREEN_WIDTH:
            screen.blit(cursor_turret, cursor_rect)
            if (check_create_turret(pg.mouse.get_pos())):
                avaible_zone(pg.mouse.get_pos(), "green")
            else:
                avaible_zone(pg.mouse.get_pos(), "red")
        if cancel_button.draw(screen):
            placing_turrets = False

    if selected_turret: 
        
        if selected_turret.upgrade_level < c.TURRET_LEVEL:
        
            if upgrade_turret_button.draw(screen):
                selected_turret.upgrade(screen)

    # event handler
    for event in pg.event.get():
        # print(event)

        if event.type == pg.QUIT:
            run = False

        if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
            mouse_pos = pg.mouse.get_pos()

            # check if mouse is on the game area
            if mouse_pos[0] < c.SCREEN_WIDTH and mouse_pos[1] < c.SCREEN_HEIGHT:
                # clear selected turrets
                selected_turret = None
                clear_selection()
                if placing_turrets == True:
                    create_turret(mouse_pos)
                else:
                    selected_turret = select_turret(mouse_pos)

    # แต้มจุด สร้าง waypoint
    #     pos = pg.mouse.get_pos()
    #     if event.type == pg.MOUSEBUTTONDOWN:
    #         pos_list.append(pos)
    #         print(pos_list)
    # for p in pos_list:
    #     pg.draw.circle(screen, (255, 0, 0), (p[0], p[1]), 5, 0)

    # update display
    pg.display.flip()

pg.quit()
