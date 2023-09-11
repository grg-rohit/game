# main.py
import pygame
from pygame.locals import *
from tank import run_game
from maps import load_background, generate_map
from targets import generate_targets

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 700
tank_width = 40
tank_height = 40

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Tank Game - Level 1")  # Initialize with Level 1

# Load the background image
background_image = load_background("assets/maps/warzone1.jpg", (1000, 700))

# Define the number of targets for each level
level_data = {
    1: {'num_targets': 5},
    2: {'num_targets': 10}
}

current_level = 1

# Define player variables
player_width = tank_width
player_height = tank_height
player_x = (SCREEN_WIDTH - player_width) // 2
player_y = (SCREEN_HEIGHT - player_height) // 2

# Ensure player_rect is defined correctly
player_rect = pygame.Rect(player_x, player_y, player_width, player_height)

obstacles = generate_map(SCREEN_WIDTH, SCREEN_HEIGHT, player_rect)
targets = generate_targets(level_data[current_level]['num_targets'], SCREEN_WIDTH, SCREEN_HEIGHT)

# Font for displaying the current level
level_font = pygame.font.Font(None, 36)
level_color = (255, 255, 255)

# Main game loop
while current_level <= 2:
    # Print the number of generated obstacles for the current level
    print(f"Level {current_level}: Number of obstacles = {len(obstacles)}")

    # Update the window caption to display the current level
    pygame.display.set_caption(f"TANK SHOOT - Level {current_level}")

    # Clear the screen
    screen.fill((0, 0, 0))

    # Draw the background image
    screen.blit(background_image, (0, 0))

    # Run the game for the current level
    player_rect = run_game(screen, background_image, obstacles, targets)

    # Check if the current level is completed
    if len(targets) == 0:
        current_level += 1

        if current_level <= 2:
            # Generate new obstacles and targets for Level 2
            obstacles = generate_map(SCREEN_WIDTH, SCREEN_HEIGHT, player_rect)
            targets = generate_targets(level_data[current_level]['num_targets'], SCREEN_WIDTH, SCREEN_HEIGHT)

    pygame.display.flip()

