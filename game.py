import pygame
import random

# Set up some constants
WIDTH, HEIGHT = 800, 640
VELOCITY = 80


def initialize_game():
    pygame.init()
    return pygame.display.set_mode((WIDTH, HEIGHT)), pygame.image.load("forest.jpg"), pygame.mixer.music.load("best-adventure-ever-122726.mp3")



def load_images():
    return (
        pygame.image.load("boy left.png"),
        pygame.image.load("boy.png"),
        pygame.transform.scale(pygame.image.load("bo.png"), (50, 80)),
        pygame.transform.scale(pygame.image.load("Map_thumbnail.png"), (100, 120)),
        pygame.transform.scale(pygame.image.load("tent_thumbnail.png"), (100, 90)),
        pygame.transform.scale(pygame.image.load("boom.webp"), (50, 50)),
        pygame.transform.scale(pygame.image.load("start button.jpg"), (800, 650)),
    )

def create_player():
    return "left", player_left.get_rect(topleft=(150, 400))

def create_items():
    return [
        {"image": bottle_resized, "rect": bottle_resized.get_rect(topleft=(random.randint(0, WIDTH - 20), 0)), "speed": 1.3},
        {"image": map_resized, "rect": map_resized.get_rect(topright=(random.randint(0, WIDTH - 10), 0)), "speed": 1.5},
        {"image": tent_resized, "rect": tent_resized.get_rect(topleft=(random.randint(0, WIDTH - 20), 0)), "speed": 1.0},
        {"image": boom_resized, "rect": boom_resized.get_rect(topleft=(random.randint(0, WIDTH - 20), 0)), "speed": 1.0},
    ]

def reset_item_position(item):
    item["rect"].y = 0
    item["rect"].x = random.randint(0, WIDTH - item["rect"].width)

def draw_start_screen(screen):
    screen.blit(start_button_resized, (0, 0))
    font = pygame.font.Font(None, 36)
    text = font.render("Welcome to collect things for your travel experience", 1, ("black"))
    text_1 = font.render(" Press SPACE to start", 1, ("magenta"))
    screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 3 - text.get_height() // 19))
    screen.blit(text_1, (WIDTH // 3 - text.get_width() // 9, HEIGHT // 2 - text.get_height() // 15))
    pygame.display.flip()

def draw_game_over_screen(screen):
    font = pygame.font.Font(None, 72)
    text = font.render("Game Over", 1, (255, 0, 0))
    screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 - text.get_height() // 2))
    pygame.display.flip()
    pygame.time.delay(200)

def game_loop(screen, background, player_direction, player_rect, player_x, player_y, items, player_lives, score):
    pygame.mixer.music.play(-1)
    running = True
    while running:
        screen.blit(background, (0, 0))

        if player_direction == "left":
            screen.blit(player_left, player_rect)
        else:
            screen.blit(player_right, player_rect)

        player_rect.x = player_x
        player_rect.y = player_y

        for item in items:
            screen.blit(item["image"], item["rect"])
            item["rect"].y += item["speed"]

            if item["rect"].y > HEIGHT:
                reset_item_position(item)

            if player_rect.colliderect(item["rect"]):
                if item is not items[-1]:
                    reset_item_position(item)
                    score += 1
                else:
                    player_lives -= 1
                    reset_item_position(item)

        font = pygame.font.Font(None, 36)
        text_lives = font.render("Lives: " + str(player_lives), 1, ("orange"))
        text_score = font.render("Final Score: " + str(score), 1, ("purple"))
        screen.blit(text_lives, (10, 10))
        screen.blit(text_score, (WIDTH // 2 - text_score.get_width() // 2, HEIGHT // 2 + text_score.get_height()))

        if player_lives <= 0:
            draw_game_over_screen(screen)
            running = False

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    player_x += VELOCITY
                    player_direction = "right"
                elif event.key == pygame.K_LEFT:
                    player_x -= VELOCITY
                    player_direction = "left"

        if player_lives <= 0:
            running = False

    pygame.quit()

# Main execution
screen, background, music = initialize_game()
player_left, player_right, bottle_resized, map_resized, tent_resized, boom_resized, start_button_resized = load_images()
player_direction, player_rect = create_player()
items = create_items()

# Other variables
player_x, player_y = 150, 400
player_lives, score = 3, 0
start_game = False

# Start screen loop
while not start_game:
    draw_start_screen(screen)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            start_game = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                start_game = True

# Game loop
game_loop(screen, background, player_direction, player_rect, player_x, player_y, items, player_lives, score)
