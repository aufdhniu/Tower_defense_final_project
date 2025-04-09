import pygame as pg
from pygame.math import Vector2 
import math
import os 
class Enemy(pg.sprite.Sprite):
    
    def __init__(self, waypoints, image, health=100):
        pg.sprite.Sprite.__init__(self)
        self.waypoints = waypoints
        self.pos = Vector2(self.waypoints[0])
        self.target_waypoint = 1 
        self.speed = 1.4
        self.angle = 0
        self.orginal_image = image
        self.orginal_image = pg.transform.scale(self.orginal_image,(100,100))
        self.image = pg.transform.rotate(self.orginal_image,self.angle)
        self.health = health
        #update image
        self.animetion_list = self.load_images()
        self.frame_index = 0
        self.image = self.animetion_list[self.frame_index]
        self.update_time = pg.time.get_ticks()
        
        self.rect = self.image.get_rect()
        self.rect.center = self.pos
    
    def play_animation(self):
        self.image = self.animetion_list[self.frame_index]
        self.image = pg.transform.scale(self.image,(150,100))
        
        if pg.time.get_ticks() - self.update_time > 20 :
            self.update_time = pg.time.get_ticks()
            self.frame_index += 1
            if self.frame_index >= len(self.animetion_list):
                self.frame_index = 0
        self.rect = self.image.get_rect()
        self.rect.center = self.pos
    
    def load_images(self):
        animation_list = []
        img_dir = "assets/images/enemy/enemy_3"
        for filename in sorted(os.listdir(img_dir)):
            img_path=os.path.join(img_dir,filename)
            animation_list.append(pg.image.load(img_path))
        return animation_list
    
    def get_enemy_image(img):
        return pg.image.load(f"assets/images/enemy/{img}").convert_alpha()
    
    def update(self):
        self.move()    
        self.rotate()
        self.play_animation()
    
    def move(self):
        #define a target waypoint 
        if self.target_waypoint < len(self.waypoints):
            self.target = Vector2(self.waypoints[self.target_waypoint])
            self.movement = self.target - self.pos
        else:
            self.kill()
            
        #caluculate distance to target
        dist = self.movement.length()
        #check if remaining destance is greater than the enemy speed
        if dist >= self.speed:
            self.pos += self.movement.normalize()*self.speed
        else:
            if dist != 0:
                self.pos += self.movement.normalize()*dist
            self.target_waypoint +=1
    
    
    def rotate(self):
        dist = self.target - self.pos
        
        #calculate angle
        self.angle = math.degrees(math.atan2(-dist[1],dist[0]))
        # print(self.angle)
        self.image = pg.transform.rotate(self.orginal_image,self.angle)
        self.image = pg.transform.scale(self.orginal_image,(150,100))
        self.rect = self.image.get_rect()
        self.rect.center = self.pos
    
    def check_health(self):
        if self.health <= 0:
            self.kill()
    
    def draw_health(self, screen):
        # Draw a health bar above the enemy
        bar_width = 50
        bar_height = 5
        health_percentage = max(self.health / 100, 0)  # Calculate health ratio
        bar_fill = int(bar_width * health_percentage)
        health_bar = pg.Rect(self.rect.centerx - bar_width // 2, 
                            self.rect.top - bar_height - 5, 
                            bar_width, bar_height)
        health_fill = pg.Rect(health_bar.x, health_bar.y, bar_fill, bar_height)
        pg.draw.rect(screen, "red", health_bar)  # Draw the full health bar (background)
        pg.draw.rect(screen, "green", health_fill)  # Draw the filled portion (