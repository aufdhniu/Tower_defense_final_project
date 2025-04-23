import os 
import pygame as pg 
def load_animation(folder_path):
    animation_list = []
    for filename in sorted(os.listdir(folder_path)):
            path = os.path.join(folder_path, filename)
            image = pg.image.load(path)
            animation_list.append(image)
    return animation_list