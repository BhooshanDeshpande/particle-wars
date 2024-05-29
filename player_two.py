import pygame
import math
from constants import *
from base_particle import BaseParticle
import random

class PlayerTwoParticle(BaseParticle):
    def __init__(self):
        self.vel = 0 # limit 0 px/s to 10 px/s 
        self.angle = 0 #limit 0 to 360
        self.x = random.randint(0, WIDTH)
        self.y = random.randint(0, HEIGHT)
        self.color = PLAYER_TWO_COLOR
        self.team =  PLAYER_TWO
        super().__init__(self.x, self.y, self.color, self.team, self.vel, self.angle) 

    def update_velocity(self, particles): 
        closest_food = None
        closest_food_dist = float('inf')
        for particle in particles: 
            if particle.team == PLAYER_TWO: 
                continue

            if particle.team == FOOD: 
                dist = self.distance_to(particle)
                if dist < closest_food_dist: 
                    closest_food = particle
            
        if closest_food is None: 
            print(closest_food)
            closest_food = particles[0] #go after first particle

        angle = math.degrees(math.atan2(closest_food.y -self.y, closest_food.x - self.x))
        acc = PARTICLE_ACC
        print(angle)
        return acc, angle
    
    def distance_to(self, other):
        return math.hypot(self.x - other.x, self.y - other.y)
        