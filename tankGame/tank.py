# # tank.py
# tank.py
import pygame
from pygame.locals import *
import math
from maps import draw_map
from obstacles import is_colliding
from targets import check_target_collision

def run_game(screen, background_image, obstacles, targets):

    # Constants
    SCREEN_WIDTH, SCREEN_HEIGHT = screen.get_size()
    PLAYER_SPEED = 1
    PROJECTILE_SPEED = 3

    # Colors
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)

    # Load the tank image and set its size
    tank_image = pygame.image.load("assets/tank1.png")  # Replace with your tank image file
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

    # Score variable
    score = 0

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
                # Check for collision with obstacles and targets before adding a projectile
                if not is_colliding(player_rect, obstacles) and not check_target_collision(player_rect, targets):
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

        # Calculate the new player position
        new_player_x = player_x + dx
        new_player_y = player_y + dy

        # Create a temporary rect for the new player position
        new_player_rect = pygame.Rect(new_player_x, new_player_y, player_width, player_height)

        # Check for collision with obstacles and targets before updating the player position
        if (
            not is_colliding(new_player_rect, obstacles)
            and not check_target_collision(new_player_rect, targets)
            and 0 <= new_player_x <= SCREEN_WIDTH - player_width
            and 0 <= new_player_y <= SCREEN_HEIGHT - player_height
        ):
            player_x = new_player_x
            player_y = new_player_y

        mouse_x, mouse_y = pygame.mouse.get_pos()

        # Calculate the angle to align the tank with the mouse
        angle = math.atan2(mouse_y - (player_y + player_height // 2), mouse_x - (player_x + player_width // 2))
        player_angle = math.degrees(angle)

        updated_projectiles = []
        for projectile in projectiles:
            projectile['x'] += PROJECTILE_SPEED * math.cos(projectile['angle'])
            projectile['y'] += PROJECTILE_SPEED * math.sin(projectile['angle'])
            
            # Check for collisions with obstacles
            projectile_rect = pygame.Rect(projectile['x'], projectile['y'], 3, 3)
            if (
                not is_colliding(projectile_rect, obstacles)
                and 0 <= projectile['x'] <= SCREEN_WIDTH
                and 0 <= projectile['y'] <= SCREEN_HEIGHT
            ):
                # Check for collisions with targets
                if not check_target_collision(projectile_rect, targets):
                    updated_projectiles.append(projectile)
                else:
                    # Projectile hit a target, increase the score
                    score += 1
        
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

        for target in targets:
            # Calculate the angle between the target and the tank
            target_x, target_y = target['rect'].center
            angle = math.atan2(target_y - (player_y + player_height // 2), target_x - (player_x + player_width // 2))
            angle_degrees = math.degrees(angle)

            # Rotate the target image to face the tank
            rotated_target = pygame.transform.rotate(target['image'], -angle_degrees)
            rotated_target_rect = rotated_target.get_rect(center=target['rect'].center)

            # Draw the rotated target image
            screen.blit(rotated_target, rotated_target_rect)

        for projectile in projectiles:
            pygame.draw.circle(screen, RED, (int(projectile['x']), int(projectile['y'])), 3)

        # Display the score
        font = pygame.font.Font(None, 36)
        score_text = font.render(f"Score: {score}", True, WHITE)
        screen.blit(score_text, (10, 10))
        
        # Game over condition
        if len(targets) == 0:
            font = pygame.font.Font(None, 72)
            game_over_text = font.render("Game Over", True, RED)
            screen.blit(game_over_text, (SCREEN_WIDTH // 2 - 150, SCREEN_HEIGHT // 2 - 36))
            pygame.display.flip()
            pygame.time.delay(2000)  # Display the "Game Over" message for 2 seconds
            running = False
            
        pygame.display.flip()

    return player_rect
