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

import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("My 2D Game")

# Player settings
player_size = 50
player_color = (255, 0, 0)
player_x, player_y = width // 2, height // 2
player_speed = 5

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_x -= player_speed
    if keys[pygame.K_RIGHT]:
        player_x += player_speed
    if keys[pygame.K_UP]:
        player_y -= player_speed
    if keys[pygame.K_DOWN]:
        player_y += player_speed

    # Fill the screen with a color (RGB)
    screen.fill((0, 0, 255))

    # Draw the player
    pygame.draw.rect(screen, player_color, (player_x, player_y, player_size, player_size))

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()


import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("My 2D Game")

# Player settings
player_size = 50
player_color = (255, 0, 0)
player_x, player_y = width // 2, height // 2
player_speed = 5

# Enemy settings
enemy_size = 50
enemy_color = (0, 255, 0)
enemy_x, enemy_y = width // 4, height // 4
enemy_speed = 3
enemy_direction = 1

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_x -= player_speed
    if keys[pygame.K_RIGHT]:
        player_x += player_speed
    if keys[pygame.K_UP]:
        player_y -= player_speed
    if keys[pygame.K_DOWN]:
        player_y += player_speed

    # Move the enemy
    enemy_x += enemy_speed * enemy_direction
    if enemy_x <= 0 or enemy_x + enemy_size >= width:
        enemy_direction *= -1

    # Fill the screen with a color (RGB)
    screen.fill((0, 0, 255))

    # Draw the player
    pygame.draw.rect(screen, player_color, (player_x, player_y, player_size, player_size))

    # Draw the enemy
    pygame.draw.rect(screen, enemy_color, (enemy_x, enemy_y, enemy_size, enemy_size))

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()



import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("My 2D Game")

# Player settings
player_size = 50
player_color = (255, 0, 0)
player_x, player_y = width // 2, height // 2
player_speed = 5

# Enemy settings
enemy_size = 50
enemy_color = (0, 255, 0)
enemy_x, enemy_y = width // 4, height // 4
enemy_speed = 3
enemy_direction = 1

def detect_collision(player_x, player_y, enemy_x, enemy_y, size):
    if (player_x < enemy_x + size and
        player_x + size > enemy_x and
        player_y < enemy_y + size and
        player_y + size > enemy_y):
        return True
    return False

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_x -= player_speed
    if keys[pygame.K_RIGHT]:
        player_x += player_speed
    if keys[pygame.K_UP]:
        player_y -= player_speed
    if keys[pygame.K_DOWN]:
        player_y += player_speed

    # Move the enemy
    enemy_x += enemy_speed * enemy_direction
    if enemy_x <= 0 or enemy_x + enemy_size >= width:
        enemy_direction *= -1

    # Fill the screen with a color (RGB)
    screen.fill((0, 0, 255))

    # Draw the player
    pygame.draw.rect(screen, player_color, (player_x, player_y, player_size, player_size))

    # Draw the enemy
    pygame.draw.rect(screen, enemy_color,) (enemy_x, enemy)

