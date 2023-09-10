import pygame
import random

def generate_obstacles(num_obstacles, screen_width, screen_height):
    obstacles = []

    for _ in range(num_obstacles):
        # Generate random obstacle properties (x, y, width, height)
        x = random.randint(0, screen_width - 100)
        y = random.randint(0, screen_height - 100)
        width = random.randint(20, 100)
        height = random.randint(20, 100)

        obstacles.append(pygame.Rect(x, y, width, height))

    return obstacles

def is_colliding(rect, obstacles):
    for obstacle in obstacles:
        if rect.colliderect(obstacle):
            return True
    return False
