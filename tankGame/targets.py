# targets.py

import pygame
import random
import os
import math
from obstacles import is_colliding

# Directory path for target images
TARGET_IMAGE_DIR = "assets/targets"

def load_target_images():
    target_images = []
    for file_name in os.listdir(TARGET_IMAGE_DIR):
        if file_name.endswith(".png"):
            image_path = os.path.join(TARGET_IMAGE_DIR, file_name)
            loaded_image = pygame.image.load(image_path)

            # Check if the loaded image dimensions are within the desired range
            min_dimension = 20
            max_dimension = 40

            if (
                min_dimension <= loaded_image.get_width() <= max_dimension
                and min_dimension <= loaded_image.get_height() <= max_dimension
            ):
                target_images.append(loaded_image)
            else:
                # Resize the image to fit within the desired range
                resized_image = pygame.transform.scale(loaded_image, (max_dimension, max_dimension))
                target_images.append(resized_image)

    return target_images

def generate_targets(num_targets, screen_width, screen_height, existing_obstacles=None):
    targets = []

    target_images = load_target_images()

    for _ in range(num_targets):
        # Select a random target image
        target_image = random.choice(target_images)
        target_width, target_height = target_image.get_size()

        while True:
            # Generate random target properties (x, y, width, height)
            x = random.randint(0, screen_width - target_width)
            y = random.randint(0, screen_height - target_height)
            target_rect = pygame.Rect(x, y, target_width, target_height)

            # Check if the new target collides with existing obstacles (if provided)
            if (
                existing_obstacles is None
                or (not is_colliding(target_rect, existing_obstacles) and not target_rect.colliderect(tank_rect))
            ):
                break  # No collision, add this target

        targets.append({
            'image': target_image,
            'rect': target_rect
        })

    return targets

# def generate_targets(num_targets, screen_width, screen_height, existing_obstacles=None):
#     targets = []

#     target_images = load_target_images()

#     for _ in range(num_targets):
#         # Select a random target image
#         target_image = random.choice(target_images)
#         target_width, target_height = target_image.get_size()

#         while True:
#             # Generate random target properties (x, y, width, height)
#             x = random.randint(0, screen_width - target_width)
#             y = random.randint(0, screen_height - target_height)
#             target_rect = pygame.Rect(x, y, target_width, target_height)

#             # Check if the new target collides with existing obstacles (if provided)
#             if existing_obstacles is None or not is_colliding(target_rect, existing_obstacles):
#                 # Check if the new target collides with other targets
#                 if not check_target_collision(target_rect, targets):
#                     break  # No collision, add this target

#         targets.append({
#             'image': target_image,
#             'rect': target_rect
#         })

#     return targets

def check_target_collision(rect, targets):
    for target in targets:
        if rect.colliderect(target['rect']):
            targets.remove(target)
            return True
    return False



# def generate_targets(num_targets, screen_width, screen_height, existing_obstacles=None):
#     targets = []

#     target_images = load_target_images()

#     for _ in range(num_targets):
#         # Select a random target image
#         target_image = random.choice(target_images)
#         target_width, target_height = target_image.get_size()

#         while True:
#             # Generate random target properties (x, y, width, height)
#             x = random.randint(0, screen_width - target_width)
#             y = random.randint(0, screen_height - target_height)
#             target_rect = pygame.Rect(x, y, target_width, target_height)

#             # Check if the new target collides with existing obstacles (if provided)
#             if existing_obstacles is None or not is_colliding(target_rect, existing_obstacles):
#                 break  # No collision, add this target

#         targets.append({
#             'image': target_image,
#             'rect': target_rect
#         })

#     return targets



# def check_target_collision(rect, targets):
#     for target in targets:
#         if rect.colliderect(target['rect']):
#             targets.remove(target)
#             return True
#     return False

