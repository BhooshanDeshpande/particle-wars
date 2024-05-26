import pygame
import math
from constants import *
from base_particle import BaseParticle
import random

class PlayerTwoParticle(BaseParticle):
    def __init__(self):
        self.vel = 0 # limit 0 px/s to 10 px/s 
        self.angle = 0 #limit 0 to 360
        self.x = 200
        self.y = 300
        self.color = PLAYER_TWO_COLOR
        self.team =  PLAYER_TWO
        super().__init__(self.x, self.y, self.color, self.team, self.vel, self.angle) 

    def update_velocity(self, particles): 
        speed = random.randint(0, PARTICLE_SPEED)
        angle = random.randint(0, 360)
        return speed, angle
        