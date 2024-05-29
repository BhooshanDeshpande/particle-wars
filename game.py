import pygame
from constants import *
from player_one import PlayerOneParticle
from player_two import PlayerTwoParticle
from food import Food
from time import sleep

def draw_text(screen, text, x, y, font_size=24, COLOR=BLACK):
    font = pygame.font.Font(None, font_size)
    text_surface = font.render(text, True, COLOR)
    screen.blit(text_surface, (x, y))

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()

    particles = []

    for _ in range(PARTICLE_COUNT):
        particles.append(PlayerOneParticle())
        particles.append(PlayerTwoParticle())
    
    for _ in range(FOOD_COUNT): 
        particles.append(Food())

    start_time = pygame.time.get_ticks()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        current_time = pygame.time.get_ticks()
        if current_time - start_time > GAME_DURATION:
            running = False
            break

        screen.fill(WHITE)

        for particle in particles:    
            particle.acc, particle.angle = particle.update_velocity(particles)
            
        for particle in particles:
            particle.update()
            particle.draw(screen)

        for i, p1 in enumerate(particles):
            if p1.team == FOOD: 
                continue
            for p2 in particles[i+1:]:
                if p1.in_range(p2):
                    if p2.team == FOOD: 
                        p1.health += p2.health
                        particles.remove(p2)
                        particles.append(Food())
                        continue

                    if p1.team == p2.team:
                        continue

                    if p1.team != p2.team:

                        team1_count = sum(1 for p in particles if p.team == p1.team and p.in_range(p2))
                        team2_count = sum(1 for p in particles if p.team == p2.team and p.in_range(p1))

                        if (p1.is_facing(p2)): 
                            p1.attack = PARTICLE_ATTACK_BOOST
                        
                        if (p2.is_facing(p1)):
                            p2.attack = PARTICLE_ATTACK_BOOST

                        p1.health -= p2.attack / (team2_count + 1)
                        p2.health -= p1.attack / (team1_count + 1)

                        if p1.health <= 0 and p1 in particles:
                            particles.remove(p1)
                        if p2.health <= 0 and p2 in particles:
                            particles.remove(p2)

        p2_health = int(sum(p.health for p in particles if p.team == PLAYER_TWO))
        p1_health = int(sum(p.health for p in particles if p.team == PLAYER_ONE))

        draw_text(screen, f"{PLAYER_TWO}: {p2_health}", 10, 10)
        draw_text(screen, f"{PLAYER_ONE}: {p1_health}", 650, 10)
        draw_text(screen, f"Time: {max(0, (GAME_DURATION - (current_time - start_time)) // 1000)}", 370, 10)
        
        if p2_health <= 0 or p1_health <= 0:
            running = False

        pygame.display.flip()
        clock.tick(30)

    winner = PLAYER_TWO if p2_health > p1_health else PLAYER_ONE if p1_health > p2_health else None
    winner_color = PLAYER_TWO_COLOR if winner == PLAYER_TWO else PLAYER_ONE_COLOR
    if winner:
            draw_text(screen, f"{winner} wins!!", 370, 300, font_size=50, COLOR=winner_color)
    else: 
        draw_text(screen, f"{winner} wins!!", 370, 300, font_size=50)

    pygame.display.flip()
    sleep(3)
    pygame.quit()

if __name__ == "__main__":
    main()
