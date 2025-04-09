import pygame as pg 
import os

class Turret(pg.sprite.Sprite):
    
    animation_frame = []
    img_dir = "assets/images/turrets/turret_1"
    for filename in sorted(os.listdir(img_dir)):
            img_path=os.path.join(img_dir,filename)
            animation_frame.append(pg.image.load(img_path))
    
    
    
    def __init__(self,image,pos):
        pg.sprite.Sprite.__init__(self)
        self.pos = pg.math.Vector2(pos)
        #calculate center 
        
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = (self.pos[0],self.pos[1])
        self.last_attack_time = 0  # Track the last attack time
        self.attack_cooldown = 500
        self.animetion_list = self.animation_frame
        self.frame_index = 0
        self.image = self.animetion_list[self.frame_index]
        self.update_time = pg.time.get_ticks()
        
    def play_animation(self):
        self.image = self.animetion_list[self.frame_index]
        self.image = pg.transform.scale(self.image,(500,500))
        
        if pg.time.get_ticks() - self.update_time > 80 :
            self.update_time = pg.time.get_ticks()
            self.frame_index += 1
            if self.frame_index >= len(self.animetion_list):
                self.frame_index = 0
        self.rect = self.image.get_rect()
        self.rect.center = self.pos
    
    # def load_images(self):
       
    #     return animation_list
    
    def update(self):
        self.play_animation()


    def deal_damage(self, enemies, damage=25, range=150):
        current_time = pg.time.get_ticks()
        if current_time - self.last_attack_time >= self.attack_cooldown:
            for enemy in enemies:
                if self.pos.distance_to(enemy.pos) <= range:
                    enemy.health -= damage
                    self.last_attack_time = current_time  # Reset cooldown
                    if enemy.health <= 0:
                        enemy.kill()