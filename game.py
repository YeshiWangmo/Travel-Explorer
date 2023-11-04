import pygame
import random

# Initialize Pygame
pygame.init()
# Set up some constants
WIDTH, HEIGHT = 800, 600

# Set up the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Travel Explore")

# Set the background
background = pygame.image.load("forest.jpg")
background = pygame.transform.scale(background, (WIDTH, HEIGHT))

# Insert this line to load the background sound
pygame.mixer.music.load("best-adventure-ever-122726.mp3")

# Set the background sound to loop infinitely
pygame.mixer.music.play(-1)

# Create the player
player = pygame.image.load("boy.png")
player_right = pygame.image.load("boy.png")
player_left = pygame.image.load("boy left.png")  # Fixed filename typo
player_direction = "left"

player_rect = player.get_rect(topleft=(150, 400))

# Create the things to catch
Map = pygame.image.load("Map_thumbnail.png")
tent = pygame.image.load("tent_thumbnail.png")
bottle = pygame.image.load("bo.png")
boom = pygame.image.load("boom.webp")

# Scale the images size
bottle_resized = pygame.transform.scale(bottle, (50, 80))
map_resized = pygame.transform.scale(Map, (100, 120))
tent_resized = pygame.transform.scale(tent, (100, 90))
boom_resized = pygame.transform.scale(boom, (50, 50))

boom_speed = 1.5

items = [
    {"image": bottle_resized, "rect": bottle_resized.get_rect(topleft=(random.randint(0, WIDTH - 20), 0)), "speed": 1.3},
    {"image": map_resized, "rect": map_resized.get_rect(topright=(random.randint(0, WIDTH - 10), 0)), "speed": 1.5},
    {"image": tent_resized, "rect": tent_resized.get_rect(topleft=(random.randint(0, WIDTH - 20), 0)), "speed": 1},
]

boom_item = {
    "image": boom_resized,
    "rect": boom_resized.get_rect(topleft=(random.randint(0, WIDTH - 20), 0)),
    "speed": 1
}
items.append(boom_item)

# Game variables
player_x = 150
player_y = 350
velocity = 80
player_lives = 3  # Initial player lives
score = 0  # Player's score
start_game = False

def reset_item_position(item):
    item["rect"].y = 0
    item["rect"].x = random.randint(0, WIDTH - item["rect"].width)


# Start screen loop
while not start_game:
    # Draw the start screen
    screen.blit(background, (0, 0))
    font = pygame.font.Font(None, 36)
    text = font.render("Press SPACE to start", 1, (255, 255, 255))
    screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 - text.get_height() // 2))

    # Update the display
    pygame.display.flip()

    # Handle events for the start screen
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            start_game = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                start_game = True

# Game loop
running = True
while running:
    # Draw the background
    screen.blit(background, (0, 0))

    # Draw the player
    if player_direction == "left":
        screen.blit(player_left, player_rect)
    else:
        screen.blit(player_right, player_rect)

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
            reset_item_position(item)

        # If the item hits the player, reset its position and update the score
        if player_rect.colliderect(item["rect"]):
            if item is not boom_item:
                reset_item_position(item)
                score += 1
            else:
                player_lives -= 1
                reset_item_position(item)

    # Display player lives
    font = pygame.font.Font(None, 36)
    text = font.render("Lives: " + str(player_lives), 1, ("orange"))
    screen.blit(text, (10, 10))

    
    font = pygame.font.Font(None, 36)
    text = font.render("Final Score: " + str(score), 1, ("purple"))
    screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 + text.get_height()))

    # Check for game over
    if player_lives <= 0:
        font = pygame.font.Font(None, 72)
        text = font.render("Game Over", 1, (255, 0, 0))
        screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 - text.get_height() // 2))

    # Update the display
    pygame.display.flip()

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                player_x += velocity
                player_direction = "right"
            elif event.key == pygame.K_LEFT:
                player_x -= velocity
                player_direction = "left"

    # Quit Pygame if player lives are over
    if player_lives <= 0:
        running = False
    

# Quit Pygame
pygame.quit()
