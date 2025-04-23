import pygame as pg
import os
import constant as c
import math
from turret_data import TURRET_DATA
from load_animation import load_animation


class Turret(pg.sprite.Sprite):
    animations = {}

    for num in range(0, 2):
        folder_path = f'./assets/images/turrets/turret_1/level{num+1}'
        animations[num] = load_animation(folder_path)

    def __init__(self, image, pos):
        pg.sprite.Sprite.__init__(self)
        self.upgrade_level = 1
        self.range = TURRET_DATA[self.upgrade_level - 1].get("range")
        self.cooldown = TURRET_DATA[self.upgrade_level - 1].get("cooldown")
        self.last_shot = pg.time.get_ticks()
        self.pos = pos
        self.selected = False
        self.target = None

        # animation var

        self.animation_list = self.animations[self.upgrade_level-1]
        self.frame_index = 0
        self.update_time = pg.time.get_ticks()

        # update image
        self.image = self.animation_list[self.frame_index]
        self.image = pg.transform.scale(self.image, (360, 360))
        self.rect = self.image.get_rect()
        self.rect.center = (self.pos[0], self.pos[1])

        # create transparent circle showing range
        self.range_image = pg.Surface((self.range*2, self.range*2))
        self.range_image.fill((0, 0, 0))
        self.range_image.set_colorkey((0, 0, 0))
        pg.draw.circle(self.range_image, "grey100",
                       (self.range, self.range), self.range)
        self.range_image.set_alpha(100)
        self.range_rect = self.range_image.get_rect()
        self.range_rect.center = self.rect.center

    def play_animation(self):
        # update image
        self.image = self.animation_list[self.frame_index]
        self.image = pg.transform.scale(self.image, (360, 360))
        self.rect = self.image.get_rect()
        self.rect.center = self.pos

        # check if enough time since last update
        if pg.time.get_ticks() - self.update_time > c.ANIMATION_DELAY:
            self.update_time = pg.time.get_ticks()
            self.frame_index += 1

            # reset animation
            if self.frame_index >= len(self.animation_list):
                self.frame_index = 0
                self.last_shot = pg.time.get_ticks()
                self.target = None

    def update(self, enemy_group):
        if self.target:
            self.play_animation()
        else:
            if pg.time.get_ticks() - self.last_shot > self.cooldown:
                self.pick_target(enemy_group)

    def pick_target(self, enemy_group):
        # find an enemy to target
        x_dist = 0
        y_dist = 0

        # check dist to each enemy is in range or not
        for enemy in enemy_group:
            x_dist = enemy.pos[0] - self.pos[0]
            y_dist = enemy.pos[1] - self.pos[1]
            dist = math.sqrt(x_dist ** 2 + y_dist ** 2)
            if dist < self.range:
                self.target = enemy
                print("Target selected")

    def upgrade(self, surface):
        self.upgrade_level += 1
        self.range = TURRET_DATA[self.upgrade_level - 1].get("range")
        self.cooldown = TURRET_DATA[self.upgrade_level - 1].get("cooldown")

        self.animation_list = self.animations[self.upgrade_level-1]

        self.image = self.animation_list[self.frame_index]
        self.image = pg.transform.scale(self.image, (360, 360))
        self.rect = self.image.get_rect()
        self.rect.center = (self.pos[0], self.pos[1])

        self.draw(surface)

        # upgrade range circle
        self.range_image = pg.Surface((self.range*2, self.range*2))
        self.range_image.fill((0, 0, 0))
        self.range_image.set_colorkey((0, 0, 0))
        pg.draw.circle(self.range_image, "grey100",
                       (self.range, self.range), self.range)
        self.range_image.set_alpha(100)
        self.range_rect = self.range_image.get_rect()
        self.range_rect.center = self.rect.center

    def draw(self, surface):
        surface.blit(self.image, self.rect)
        if self.selected:
            surface.blit(self.range_image, self.range_rect)
