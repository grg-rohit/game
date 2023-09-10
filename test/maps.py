


# maps.py
import pygame
import random
import os
from obstacles import load_obstacle_images

from npc import NPC


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

    # Generate NPCs
    num_npcs = random.randint(1, 5)  # Generate between 1 and 5 NPCs
    npc_images = [pygame.image.load(f"assets/NPC/npc{n}.png") for n in range(1, 6)]  # Load NPC images

    for _ in range(num_npcs):
        npc_image = random.choice(npc_images)  # Select a random NPC image

        while True:
            npc_rect = pygame.Rect(
                random.randint(0, screen_width - npc_image.get_width()),
                random.randint(0, screen_height - npc_image.get_height()),
                npc_image.get_width(),
                npc_image.get_height()
            )

            # Check if the new NPC collides with any existing obstacles or NPCs
            if (
                not any(obstacle_rect.colliderect(existing_obstacle['rect']) for existing_obstacle in obstacles)
                and not any(npc_rect.colliderect(existing_npc['rect']) for existing_npc in obstacles)
            ):
                break  # No collision, add this NPC

        obstacles.append({'image': npc_image, 'rect': npc_rect})

    return obstacles

# def generate_map(screen_width, screen_height):
#     obstacles = []

#     # Define the minimum and maximum number of obstacles
#     min_obstacles = 10
#     max_obstacles = 20

#     num_obstacles = random.randint(min_obstacles, max_obstacles)  # Randomly select a number of obstacles

#     obstacle_images = load_obstacle_images()  # Load obstacle images from the "assets/obstacles" directory

#     for _ in range(num_obstacles):
#         obstacle_image = random.choice(obstacle_images)  # Select a random obstacle image

#         # Ensure that obstacle dimensions do not exceed screen dimensions
#         max_x = screen_width - obstacle_image.get_width()
#         max_y = screen_height - obstacle_image.get_height()

#         if max_x < 0 or max_y < 0:
#             continue  # Skip this obstacle if it doesn't fit within the screen

#         while True:
#             obstacle_rect = pygame.Rect(
#                 random.randint(0, max_x),
#                 random.randint(0, max_y),
#                 obstacle_image.get_width(),
#                 obstacle_image.get_height()
#             )

#             # Check if the new obstacle collides with any existing obstacles
#             if not any(obstacle_rect.colliderect(existing_obstacle['rect']) for existing_obstacle in obstacles):
#                 break  # No collision, add this obstacle

#         obstacles.append({'image': obstacle_image, 'rect': obstacle_rect})

#     return obstacles

