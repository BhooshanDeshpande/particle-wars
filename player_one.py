import pygame
import math
from constants import *
from base_particle import BaseParticle
import random

class PlayerOneParticle(BaseParticle):
    def __init__(self):
        self.vel = 0 # limit 0 px/s to 10 px/s 
        self.angle = 0 #limit 0 to 360
        self.x = random.randint(0, WIDTH)
        self.y = random.randint(0, HEIGHT)
        self.color = PLAYER_ONE_COLOR
        self.team =  PLAYER_ONE
        super().__init__(self.x, self.y, self.color, self.team, self.vel, self.angle) 

    def update_velocity(self, particles): 
        '''
        Given all particle positions, set a particle speed and angle
        '''
        closest_enemy = None
        closest_enemy_dist = float('inf')
        for particle in particles: 
            if particle.team == FOOD: 
                continue

            if particle.team == PLAYER_TWO: 
                dist = self.distance_to(particle)
                if dist < closest_enemy_dist: 
                    closest_enemy = particle
            
        if closest_enemy is None: 
            closest_enemy = particles[0] #go after first particle

        angle = math.degrees(math.atan2(closest_enemy.y -self.y, closest_enemy.x - self.x))
        acc = PARTICLE_ACC
        return acc, angle
    
    def distance_to(self, other):
        return math.hypot(self.x - other.x, self.y - other.y)

        