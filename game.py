 
import pygame

# Initialize the game
pygame.init()

# Set up the game window
screen = pygame.display.set_mode((960, 680))
pygame.display.set_caption("Travel Explore")
#set the background 
background= pygame.image.load("cartoon-forest-background-pk4lm7s01x1t3ckt.jpg")
screen.blit(background,(0,0))



# Game loop
running = True
while running:  
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
         running = False

# Update game logic heres
    
    player = pygame.image.load("10995.png")
    player = player.convert_alpha()
    player.rect = player.get_rect()
    player_size = (50, 80)
    player.rect.topleft = (x, y)
    player = pygame.transform.scale(player, player_size)
    
    screen.blit(player,(100,500))
    pygame.draw.rect(screen,(255,0,0),(150,650,200,30))
    
    
    # More code here

    # Render graphics here


    

    pygame.display.update()

# Quit the game
pygame.quit()