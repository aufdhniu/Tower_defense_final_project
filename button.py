import pygame as pg


class Button():
    def __init__(self, x, y, image,hover):
        self.original_image = image
        self.image = image
        self.hover = hover  
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
        self.clicked = False
        
    def draw(self,surface):
        action = False
        
        #get mouse pos
        pos = pg.mouse.get_pos()
        
        #check mouseover and clicked conditions 
        if self.rect.collidepoint(pos):
            self.image = self.hover
            if pg.mouse.get_pressed()[0] == 1 and self.clicked == False:
                action = True
                self.clicked = True
        
        if pg.mouse.get_pressed()[0] == 0 : 
            self.clicked = False
            
        else:
            self.image = self.original_image
        
        #draw button on screen
        surface.blit(self.image,self.rect)

        return action