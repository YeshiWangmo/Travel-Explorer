import pygame
import random

# Initialize Pygame
pygame.init()

# Set up some constants
WIDTH, HEIGHT = 800, 600 
BACKGROUND_COLOR = (0, 0, 0)
FOOD_COLOR = (255, 255, 255)
player_COLOR = (255, 0, 0)

# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))


# Create the player
player = pygame.image.load("boy.png")
player_rect = player.get_rect(topleft=(200,300))

# Create the food
food = pygame.Rect(random.randint(0, WIDTH - 20), 0, 20, 20)

# Game loop
running = True
while running:
  # Fill the screen with the background color
  screen.fill(BACKGROUND_COLOR)

  # Draw the player
  screen.blit(player, player_rect)

  # Draw the food
  pygame.draw.rect(screen, FOOD_COLOR, food)

  # Move the food down
  food.y += 1

  # If the food hits the bottom of the screen, reset its position
  if food.y > HEIGHT:
      food.x = random.randint(0, WIDTH - 20)
      food.y = 0

  # If the food hits the player, reset its position
  if player_rect.colliderect(food):
      food.x = random.randint(0, WIDTH - 20)
      food.y = 0

  # Handle events
  for event in pygame.event.get():
      if event.type == pygame.QUIT:
          running = False
      elif event.type == pygame.KEYDOWN:
          if event.key == pygame.K_LEFT:
              player_rect.x -= 50
          elif event.key == pygame.K_RIGHT:
              player_rect.x += 50

  # Update the display
  pygame.display.flip()

# Quit Pygame
pygame.quit()






  


