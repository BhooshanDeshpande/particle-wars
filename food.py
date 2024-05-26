import pygame
from constants import *
from base_particle import BaseParticle
import random

class Food(BaseParticle):
    def __init__(self):
        self.vel = 0 
        self.angle = 0 
        self.x = random.randint(0, WIDTH)
        self.y = random.randint(0, HEIGHT)
        self.color = YELLOW
        self.team =  FOOD
        super().__init__(self.x, self.y, self.color, self.team, self.vel, self.angle) 

    def update_velocity(self, particles): 
        speed = 0
        angle = 0
        return speed, angle