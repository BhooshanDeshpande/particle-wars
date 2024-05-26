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

    def update(self):       
        self.x = self.x + self.vel * math.cos(math.radians(self.angle))
        self.y = self.y + self.vel * math.sin(math.radians(self.angle)) 

        # resepct boundaries
        self.x = max(0, min(WIDTH, self.x))
        self.y = max(0, min(HEIGHT, self.y))
        self.health = max(0, min(PARTICLE_HEALTH, self.health))
        self.vel = max(0, min(PARTICLE_SPEED, self.vel))

    def distance_to(self, other):
        return math.hypot(self.x - other.x, self.y - other.y)

    def in_range(self, other):
        return self.distance_to(other) < PARTICLE_RANGE

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), PARTICLE_SIZE)