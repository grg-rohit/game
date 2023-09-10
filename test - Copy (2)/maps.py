


# maps.py
import pygame
import random
import os
from obstacles import load_obstacle_images

def load_background(image_path, size):
    background_image = pygame.image.load(image_path)
    return pygame.transform.scale(background_image, size)

def draw_map(screen, obstacles):
    for obstacle in obstacles:
        screen.blit(obstacle['image'], obstacle['rect'])

def generate_map(screen_width, screen_height):
    obstacles = []

    # Define the minimum and maximum number of obstacles
    min_obstacles = 10
    max_obstacles = 20

    num_obstacles = random.randint(min_obstacles, max_obstacles)  # Randomly select a number of obstacles

    obstacle_images = load_obstacle_images()  # Load obstacle images from the "assets/obstacles" directory

    for _ in range(num_obstacles):
        obstacle_image = random.choice(obstacle_images)  # Select a random obstacle image

        # Ensure that obstacle dimensions do not exceed screen dimensions
        max_x = screen_width - obstacle_image.get_width()
        max_y = screen_height - obstacle_image.get_height()

        if max_x < 0 or max_y < 0:
            continue  # Skip this obstacle if it doesn't fit within the screen

        while True:
            obstacle_rect = pygame.Rect(
                random.randint(0, max_x),
                random.randint(0, max_y),
                obstacle_image.get_width(),
                obstacle_image.get_height()
            )

            # Check if the new obstacle collides with any existing obstacles
            if not any(obstacle_rect.colliderect(existing_obstacle['rect']) for existing_obstacle in obstacles):
                break  # No collision, add this obstacle

        obstacles.append({'image': obstacle_image, 'rect': obstacle_rect})

    return obstacles

