import pygame
from pygame.locals import *
from tank import run_game
from maps import load_background, generate_map

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 700

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Character Control with Shooting")

# Load the background image
background_image = load_background("assets/maps/warzone1.jpg", (1000, 700))

# Generate obstacles and terrains
obstacles = generate_map(SCREEN_WIDTH, SCREEN_HEIGHT)


# Print the number of generated obstacles
print("Number of obstacles:", len(obstacles))

# Run the game
run_game(screen, background_image, obstacles)

