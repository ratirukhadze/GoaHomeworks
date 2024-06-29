



import pygame

import sys

# Initialize Pygame
pygame.init()

# Set up display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Simple 2D Game")

# Define colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

# Player settings
player_size = 50
player_pos = [width // 2, height // 2]
player_speed = 5

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    # Get pressed keys
    keys = pygame.key.get_pressed()
    
    # Update player position
    if keys[pygame.K_LEFT]:
        player_pos[0] -= player_speed
    if keys[pygame.K_RIGHT]:
        player_pos[0] += player_speed
    if keys[pygame.K_UP]:
        player_pos[1] -= player_speed
    if keys[pygame.K_DOWN]:
        player_pos[1] += player_speed
    
    # Fill screen with white
    screen.fill(white)
    
    # Draw player (a red square)
    pygame.draw.rect(screen, red, (player_pos[0], player_pos[1], player_size, player_size))
    
    # Update display
    pygame.display.flip()

    # Frame rate
    pygame.time.Clock().tick(30)
