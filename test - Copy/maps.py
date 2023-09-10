import pygame

def load_background(image_path, size):
    background_image = pygame.image.load(image_path)
    return pygame.transform.scale(background_image, size)

def generate_map(screen_width, screen_height):
    # Generate your map, including obstacles and terrains, as needed
    obstacles = [
        pygame.Rect(200, 200, 100, 50),  # Example obstacle 1 (x, y, width, height)
        pygame.Rect(500, 400, 80, 60),  # Example obstacle 2 (x, y, width, height)
        # Add more obstacles as needed
    ]
    return obstacles

def draw_map(screen, obstacles):
    # Draw obstacles and terrains on the screen
    for obstacle in obstacles:
        pygame.draw.rect(screen, (0, 0, 255), obstacle)  # Blue color for obstacles
