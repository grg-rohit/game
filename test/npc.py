# npc.py
import pygame
import math
import random

class Opponent:
    def __init__(self, screen_width, screen_height, player_x, player_y):
        self.image = pygame.image.load("assets/tank1.png")  # Replace with your NPC image file
        self.width, self.height = self.image.get_size()
        
        self.x = random.randint(0, screen_width - self.width)
        self.y = random.randint(0, screen_height - self.height)

        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.is_visible = True  # Flag to track if the opponent is visible

        self.speed = 1  # Adjust the speed as needed
        self.shooting_delay = random.randint(50, 200)  # Random delay before the first shot
        self.shooting_timer = 0
        self.projectiles = []

    def draw(self, screen):
        if self.is_visible:
            screen.blit(self.image, (self.x, self.y))

    def update(self, player_x, player_y):
        if not self.is_visible:
            return

        # Move towards the player (You can implement more advanced AI here)
        angle = math.atan2(player_y - (self.y + self.height // 2), player_x - (self.x + self.width // 2))
        self.x += self.speed * math.cos(angle)
        self.y += self.speed * math.sin(angle)
        self.rect.topleft = (self.x, self.y)

        # Check for shooting delay
        self.shooting_timer += 1
        if self.shooting_timer >= self.shooting_delay:
            self.shooting_timer = 0

            # Calculate angle towards the player
            angle = math.atan2(player_y - (self.y + self.height // 2), player_x - (self.x + self.width // 2))

            # Create a projectile directed towards the player
            self.projectiles.append({
                'x': self.x + self.width // 2,
                'y': self.y + self.height // 2,
                'angle': angle
            })

    def get_projectiles(self):
        return self.projectiles

    def update_projectiles(self):
        updated_projectiles = []
        for projectile in self.projectiles:
            projectile['x'] += PROJECTILE_SPEED * math.cos(projectile['angle'])
            projectile['y'] += PROJECTILE_SPEED * math.sin(projectile['angle'])

            # Remove projectiles that go out of bounds
            if (
                0 <= projectile['x'] <= SCREEN_WIDTH
                and 0 <= projectile['y'] <= SCREEN_HEIGHT
            ):
                updated_projectiles.append(projectile)
        
        self.projectiles = updated_projectiles

    def check_collision(self, player_rect):
        if self.is_visible and self.rect.colliderect(player_rect):
            self.is_visible = False
            return True
        return False
