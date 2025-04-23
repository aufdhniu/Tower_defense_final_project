import pygame as pg
from waypoint import waypoints,waypoints_blocked


class World():
    def __init__(self, map_image ):
        self.level = 1
        self.turret_pos = []
        self.map_blocked = waypoints_blocked
        self.waypoints = waypoints
        self.image = map_image
        self.enemy_list = []
        self.spawned_enemies = 0

    def draw(self, surface):
        surface.blit(self.image, (0, 0))
