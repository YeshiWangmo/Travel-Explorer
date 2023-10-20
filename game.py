
import pygame

# Initialize the game
pygame.init()

# Set up the game window
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Travel Explore")
#set the background color
bg_color=("purple")
screen.fill(bg_color)
# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update game logic here
    # More code here

    # Render graphics here

    pygame.display.update()

# Quit the game
pygame.quit()