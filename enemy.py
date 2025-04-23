import pygame as pg
from pygame.math import Vector2
import math
import constant as c
import os
from load_animation import load_animation

class Enemy(pg.sprite.Sprite):
    animations = {}

    for num in range(0, 10):
        folder_path = f'./assets/images/enemies/move/enemy_{num+1}'
        animations[num] = load_animation(folder_path)
        
    

    def __init__(self, waypoints, image,num,speed):
        pg.sprite.Sprite.__init__(self)
        self.waypoints = waypoints
        self.pos = Vector2(self.waypoints[0])
        self.target_waypoint = 1
        self.speed = speed
        self.angle = 0
        self.original_image = image

        # animation var
        self.animation_list = self.animations[num]
        self.frame_index = 0
        self.update_time = pg.time.get_ticks()

        # update image
        self.image = self.animation_list[self.frame_index]

    def update(self):
        self.move()
        self.rotate()
        self.play_animation()

    def move(self):
        if self.target_waypoint < len(self.waypoints):
            self.target = Vector2(self.waypoints[self.target_waypoint])
            self.movement = self.target - self.pos
        else:
            # ถึงจุดจบ waypoint
            self.kill()

        # เช็คระยะว่าถึงแล้ว
        dist = self.movement.length()
        if dist >= self.speed:
            # สร้างเวกเตอร์ 1 หน่วย สำหรับไว้บวก
            self.pos += self.movement.normalize()*self.speed
        else:
            if dist != 0:
                self.pos += self.movement.normalize()*dist
                self.target_waypoint += 1

    def rotate(self):
        dist = self.target - self.pos
        self.angle = math.degrees(math.atan2(-dist[1], dist[0]))
        if self.angle < 90 and self.angle > -90:
            # update image ทุกครั้งที่ rotate
            self.image = pg.transform.rotate(self.original_image, 0)
        else:
            # update image ทุกครั้งที่ rotate
            self.image = pg.transform.rotate(self.original_image, 180)
            self.rect = self.image.get_rect()
            self.rect.center = self.pos

    def play_animation(self):
        # update image
        self.image = self.animation_list[self.frame_index]
        self.image = pg.transform.scale(self.image, (120, 100))
        self.rect = self.image.get_rect()
        self.rect.center = self.pos

        # check if enough time since last update
        if pg.time.get_ticks() - self.update_time > 60:
            self.update_time = pg.time.get_ticks()
            self.frame_index += 1

            # reset animation
            if self.frame_index >= len(self.animation_list):
                self.frame_index = 0
