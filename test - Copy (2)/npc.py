# npc.py
import pygame
import random

class NPC:
    def __init__(self, screen_width, screen_height):
        self.image = pygame.image.load("assets/npc.png")  # Replace with your NPC image file
        self.width, self.height = self.image.get_size()
        
        self.x = random.randint(0, screen_width - self.width)
        self.y = random.randint(0, screen_height - self.height)

        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.is_visible = True  # Flag to track if the NPC is visible

    def draw(self, screen):
        if self.is_visible:
            screen.blit(self.image, (self.x, self.y))

    def check_collision(self, projectile_rect):
        if self.is_visible and self.rect.colliderect(projectile_rect):
            self.is_visible = False
            return True
        return False
