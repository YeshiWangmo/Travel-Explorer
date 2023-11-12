import unittest
import pygame

class TestGame(unittest.TestCase):
   def setUp(self):
       pygame.init()
       self.WIDTH, self.HEIGHT = 800, 600
       self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
       self.player_x = 150
       self.player_y = 350
       self.velocity = 80

   def test_player_movement(self):
       player_rect = pygame.Rect(self.player_x, self.player_y, 50, 50)
       self.assertEqual(player_rect.x, self.player_x)
       self.assertEqual(player_rect.y, self.player_y)

       # Simulate moving the player to the right
       self.player_x += self.velocity
       player_rect.x += self.velocity
       self.assertEqual(player_rect.x, self.player_x)

       # Simulate moving the player to the left
       self.player_x -= self.velocity
       player_rect.x -= self.velocity
       self.assertEqual(player_rect.x, self.player_x)

if __name__ == '__main__':
   unittest.main()
