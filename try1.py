import pygame

# Initialize the game
pygame.init()

# Set up the game window
screen = pygame.display.set_mode((960, 680))
pygame.display.set_caption("Travel Explore1")

# Set the background 
background= pygame.image.load("cartoon-forest-background-pk4lm7s01x1t3ckt.jpg")
screen.blit(background,(0,0))

class player(pygame.sprite.Sprite):
    def_int_(self, pos_x, pos_y)
    super().init_()
    self.sprite= []
    self.sprite.append(pygame.image.load("still.png"))
    self.sprite.append(pygame.image.load("left side.jpg"))
    self.sprite.append(pygame.image.load("rifht side.jpg"))




# Game loop
running = True
player_x = 100
player_y = 500
velocity = 5

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                player_x += velocity
            elif event.key == pygame.K_LEFT:
                player_x -= velocity
            elif event.key == pygame.K_UP:
                player_y -= velocity
            elif event.key == pygame.K_DOWN:
                player_y += velocity

    player = pygame.image.load("still.png")
    player = player.convert_alpha()
    player_size = (100, 80)
    player = pygame.transform.scale(player, player_size)
    player_rect = player.get_rect(topleft=(player_x, player_y))
    screen.blit(player, player_rect)
    pygame.draw.rect(screen,(255,0,0),(150,650,200,30))
    pygame.display.update
# Quit the game
pygame.quit()
