import pygame
import math
from constants import *

class BaseParticle:
    def __init__(self, x, y, color, team, vel, angle):
        self.x = x
        self.y = y
        self.vel = vel
        self.angle = angle
        self.color = color
        self.team = team
        self.attack = PARITCLE_ATTACK
        self.defense = PARTICLE_DEFENSE
        self.health = PARTICLE_HEALTH
        self.acc = 0

    def update(self): 
        vel_x = self.vel*math.cos(math.radians(self.angle)) + math.cos(math.radians(self.angle))*self.acc 
        vel_y = self.vel*math.sin(math.radians(self.angle)) + math.sin(math.radians(self.angle))*self.acc 
        self.vel = math.sqrt(vel_x*vel_x + vel_y*vel_y)

        self.x = self.x + self.vel * math.cos(math.radians(self.angle))
        self.y = self.y + self.vel * math.sin(math.radians(self.angle))

        self.health = self.health - self.vel/1000 

        # resepct boundaries
        self.x = max(0, min(WIDTH, self.x))
        self.y = max(0, min(HEIGHT, self.y))
        self.health = max(0, min(PARTICLE_HEALTH, self.health))
        self.vel = max(0, min(PARTICLE_SPEED, self.vel))

    def __distance_to(self, other):
        return math.hypot(self.x - other.x, self.y - other.y)
    def is_facing(self, other, visibility_threshold=10):
        dx = other.x - self.x
        dy = other.y - self.y
        phi = math.degrees(math.atan2(dy, dx))
        delta_theta = (phi - self.angle) % 360
        if delta_theta > 180:
            delta_theta -= 360
        return abs(delta_theta) <= visibility_threshold

    def in_range(self, other):
        return self.__distance_to(other) < PARTICLE_RANGE
    
    def __in_attack_range(self, other): 
        return self.in_range(self, other) and (self.__distance_to(other) < PARTICLE_RANGE)

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), PARTICLE_SIZE)