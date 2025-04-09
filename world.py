import pygame as pg
import map_waypoints as mw

class World():
    def __init__(self,map_image):
        self.waypoints = mw.map1
        self.map_not_avaible = mw.map1_a    
        self.map_image = map_image
        self.map_image = pg.transform.scale(self.map_image,(1280,720))
    def draw(self,surface):
        surface.blit(self.map_image,(0,0))
    
    def process_data(self):
        pass
