import unittest
from unittest.mock import patch, MagicMock
import pygame
from game import *


class TestGame(unittest.TestCase):
   def test_initialize_game(self):
        self.assertIsInstance(screen, pygame.Surface)

   def setUp(self):
        self.screen, _, _ = initialize_game()
        self.images = load_images()
        self.player_direction, self.player_rect = create_player()
        self.items = create_items()
        self.player_x, self.player_y = 150, 400
        self.player_lives, self.score = 3, 0

   @patch('pygame.display.set_mode')
   @patch('pygame.font.Font')
   @patch('pygame.display.flip')
   def test_draw_start_screen(self, mock_flip, mock_font, mock_set_mode):
       mock_screen = MagicMock()
       mock_set_mode.return_value = mock_screen
       mock_font_instance = MagicMock()
       mock_font.return_value = mock_font_instance

       draw_start_screen(mock_screen)

       
       self.assertIsNotNone(mock_screen.get_surface())

       # Check if the correct images are being drawn on the screen
       mock_screen.blit.assert_called_with(mock_font_instance.render.return_value, (WIDTH // 2 - mock_font_instance.render.return_value.get_width() // 2, HEIGHT // 3 - mock_font_instance.render.return_value.get_height() // 19))

       # Check if the screen is being updated correctly
       mock_flip.assert_called_once()

   def test_load_images(self):
       images = load_images()
       self.assertIsInstance(images, tuple)
       for image in images:
           self.assertIsInstance(image, pygame.Surface)
   
   def test_create_player(self):
        self.assertIsInstance(player_rect, pygame.Rect)
        self.assertIn(player_direction, ["left", "right"])
   
   def test_create_items(self):
        for item in items:
            self.assertIsInstance(item["image"], pygame.Surface)
            self.assertIsInstance(item["rect"], pygame.Rect)
            self.assertIsInstance(item["speed"], float)

   def test_reset_item_position(self):
        item = {"rect": pygame.Rect(0, 0, 10, 10)}
        reset_item_position(item)
        self.assertEqual(item["rect"].y, 0)
        self.assertTrue(0 <= item["rect"].x < WIDTH - item["rect"].width)

   def test_game_loop(self):
        # Mocking pygame events for testing purposes
        pygame.event.post(pygame.event.Event(pygame.QUIT))
        pygame.event.post(pygame.event.Event(pygame.KEYDOWN, {'key': pygame.K_RIGHT}))
        pygame.event.post(pygame.event.Event(pygame.KEYDOWN, {'key': pygame.K_LEFT}))
        pygame.event.post(pygame.event.Event(pygame.KEYDOWN, {'key': pygame.K_SPACE}))

   def test_draw_game_over_screen(self):
      pygame.init() # initialize Pygame
      screen = pygame.display.set_mode((800, 600)) # create a screen
      draw_game_over_screen(screen)

   def setUp(self):
       self.player_lives = 0

 

if __name__ == '__main__':
   unittest.main()
