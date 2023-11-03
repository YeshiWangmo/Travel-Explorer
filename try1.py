import pygame
import random

# Initialize Pygame
pygame.init()
# Set up some constants
WIDTH, HEIGHT = 800, 600 

# Set up the game window
screen = pygame.display.set_mode((960, 680))
pygame.display.set_caption("Travel Explore")

# Set the background 
background= pygame.image.load("cartoon-forest-background-pk4lm7s01x1t3ckt.jpg")
screen.blit(background,(0,0))
# Create the player
player = pygame.image.load("boy.png")
player_rect = player.get_rect(topleft=(200,300))


# Create the things to catch
Map = pygame.image.load("Map_thumbnail.png")
tent = pygame.image.load("tent_thumbnail.png")
bottle = pygame.image.load("bo.png")

# Scale the images size
bottle_resized = pygame.transform.scale(bottle, (50,80))
map_resized = pygame.transform.scale(Map, (100, 120))
tent_resized = pygame.transform.scale(tent, (100, 90))

items = [
 {"image": bottle_resized, "rect": bottle_resized.get_rect(topleft=(random.randint(0, WIDTH - 20), 0)), "speed": 3},
 {"image": map_resized, "rect": map_resized.get_rect(topright=(random.randint(0, WIDTH - 10), 0)), "speed": 2},
 {"image": tent_resized, "rect": tent_resized.get_rect(topleft=(random.randint(0, WIDTH - 20), 0)), "speed": 1},
]


# ... (previous code)

# Game loop
running = True
player_x = 150
player_y = 300
velocity = 5
while running:
    # Fill the screen with a background color
    screen.fill((255, 255, 255))  # Fills the screen with white color, you can choose your own color
    
     # Draw the background
    screen.blit(background, (0, 0))

    # Draw the player
    screen.blit(player, player_rect)

    # Move the player
    player_rect.x = player_x
    player_rect.y = player_y

    # Draw the items and move them down
    for item in items:
        # Draw the item
        screen.blit(item["image"], item["rect"])

        # Move the item down
        item["rect"].y += item["speed"]

        # If the item hits the bottom of the screen, reset its position
        if item["rect"].y > HEIGHT:
            item["rect"].x = random.randint(0, WIDTH - 20)
            item["rect"].y = 0

        # If the item hits the player, reset its position
        if player_rect.colliderect(item["rect"]):
            item["rect"].x = random.randint(0, WIDTH - 20)
            item["rect"].y = 0

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                player_x += velocity
            elif event.key == pygame.K_LEFT:
                player_x -= velocity

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
