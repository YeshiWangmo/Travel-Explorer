#UNIT TEST

#importing necessary modules
import unittest
import pygame
import random
import sys
from io import StringIO

# Import the functions for the test
from game import reset_item_position

#define a test class thst inherits from unittest. Test case
class TestGameFunctions(unittest.TestCase):
     # Set up method to initialize resources before each test
    def setUp(self):
        pygame.init() 
                # Redirect standard output to a StringIO object to capture print statements

        self.original_stdout = sys.stdout
        sys.stdout = StringIO()
# Tear down method to clean up resources after each test
    def tearDown(self):
        pygame.quit()
        # Restore the original standard output
        sys.stdout = self.original_stdout

 # Test method for the reset_item_position function
    def test_reset_item_position(self):
        # Define a mock item
        item = {"rect": pygame.Rect(0, 0, 50, 50)}

        # Call the function to reset the item position
        reset_item_position(item)

        # Assert that the item's y-coordinate is reset to 0
        self.assertEqual(item["rect"].y, 0)

        # Assert that the item's x-coordinate is within the valid range
        self.assertTrue(0 <= item["rect"].x <= 800)

# Run the tests if the script is executed directly
if __name__ == '__main__':
    unittest.main() # Invoke the unittest framework


