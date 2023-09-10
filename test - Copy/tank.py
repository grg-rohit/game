import pygame
from pygame.locals import *
import math
from maps import draw_map

def run_game(screen, background_image, obstacles):
    # Constants
    SCREEN_WIDTH, SCREEN_HEIGHT = screen.get_size()
    PLAYER_SPEED = 0.05
    PROJECTILE_SPEED = 3

    # Colors
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)

    # Load the tank image and set its size
    tank_image = pygame.image.load("tank1.png")  # Replace with your tank image file
    tank_width = 40  # Set the desired width of the tank
    tank_height = 40  # Set the desired height of the tank
    tank_image = pygame.transform.scale(tank_image, (tank_width, tank_height))

    # Player variables
    player_width = tank_width
    player_height = tank_height
    player_x = (SCREEN_WIDTH - player_width) // 2
    player_y = (SCREEN_HEIGHT - player_height) // 2

    # Calculate the initial angle for the tank's rotation
    mouse_x, mouse_y = pygame.mouse.get_pos()
    angle = math.atan2(mouse_y - (player_y + player_height // 2), mouse_x - (player_x + player_width // 2))
    player_angle = math.degrees(angle)

    # List to store projectiles
    projectiles = []

    # Function to create a projectile
    def create_projectile(start_x, start_y, angle):
        return {
            'x': start_x,
            'y': start_y,
            'angle': angle
        }

    # Main game loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            elif event.type == MOUSEBUTTONDOWN and event.button == 1:
                # Update the angle of the projectile to match player_angle
                projectiles.append(create_projectile(player_x + player_width // 2, player_y + player_height // 2, math.radians(player_angle)))

        keys = pygame.key.get_pressed()

        dx, dy = 0, 0
        if keys[K_w]:
            dy = -PLAYER_SPEED
        if keys[K_s]:
            dy = PLAYER_SPEED
        if keys[K_a]:
            dx = -PLAYER_SPEED
        if keys[K_d]:
            dx = PLAYER_SPEED

        player_x += dx
        player_y += dy

        mouse_x, mouse_y = pygame.mouse.get_pos()

        # Calculate the angle to align the tank with the mouse
        angle = math.atan2(mouse_y - (player_y + player_height // 2), mouse_x - (player_x + player_width // 2))
        player_angle = math.degrees(angle)

        updated_projectiles = []
        for projectile in projectiles:
            projectile['x'] += PROJECTILE_SPEED * math.cos(projectile['angle'])
            projectile['y'] += PROJECTILE_SPEED * math.sin(projectile['angle'])
            if 0 <= projectile['x'] <= SCREEN_WIDTH and 0 <= projectile['y'] <= SCREEN_HEIGHT:
                updated_projectiles.append(projectile)
        projectiles = updated_projectiles

        screen.fill(BLACK)

        # Draw the background image
        screen.blit(background_image, (0, 0))

        # Draw the tank image with rotation
        rotated_tank = pygame.transform.rotate(tank_image, -player_angle)  # Use player_angle to rotate the tank
        player_rect = rotated_tank.get_rect(center=(player_x + player_width // 2, player_y + player_height // 2))
        screen.blit(rotated_tank, player_rect)

        # Draw the map with obstacles and terrains
        draw_map(screen, obstacles)

        for projectile in projectiles:
            pygame.draw.circle(screen, RED, (int(projectile['x']), int(projectile['y'])), 3)

        pygame.display.flip()
