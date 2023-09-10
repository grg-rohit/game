# obstacles.py
import pygame
import random
import os

# Directory path for obstacle images
OBSTACLE_IMAGE_DIR = "assets/obstacles"

def load_obstacle_images():
    obstacle_images = []
    for file_name in os.listdir(OBSTACLE_IMAGE_DIR):
        if file_name.endswith(".png"):
            image_path = os.path.join(OBSTACLE_IMAGE_DIR, file_name)
            loaded_image = pygame.image.load(image_path)

            # Check if the loaded image dimensions are within the desired range
            min_dimension = 60
            max_dimension = 80

            if (
                min_dimension <= loaded_image.get_width() <= max_dimension
                and min_dimension <= loaded_image.get_height() <= max_dimension
            ):
                obstacle_images.append(loaded_image)
            else:
                # Resize the image to fit within the desired range
                resized_image = pygame.transform.scale(loaded_image, (max_dimension, max_dimension))
                obstacle_images.append(resized_image)

    return obstacle_images

def generate_obstacles(num_obstacles, screen_width, screen_height):
    obstacles = []

    obstacle_images = load_obstacle_images()

    for _ in range(num_obstacles):
        # Select a random obstacle image
        obstacle_image = random.choice(obstacle_images)
        obstacle_width, obstacle_height = obstacle_image.get_size()

        # Generate random obstacle properties (x, y, width, height)
        x = random.randint(0, screen_width - obstacle_width)
        y = random.randint(0, screen_height - obstacle_height)

        obstacles.append({
            'image': obstacle_image,
            'rect': pygame.Rect(x, y, obstacle_width, obstacle_height)
        })

    return obstacles

def is_colliding(rect, obstacles):
    for obstacle in obstacles:
        if rect.colliderect(obstacle['rect']):
            return True
    return False




