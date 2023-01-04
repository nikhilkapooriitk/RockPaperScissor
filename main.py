import random
import sys
import pygame

# Initialize Pygame
pygame.init()

# Set the window size and create a display surface
window_size = (640, 480)
screen = pygame.display.set_mode(window_size)

# Create a clock object to control the frame rate
clock = pygame.time.Clock()

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

rock_image = pygame.image.load("rock.png")
rock_image = pygame.transform.scale(rock_image, (100, 100))

paper_image = pygame.image.load("paper.png")
paper_image = pygame.transform.scale(paper_image, (100, 100))

scissor_image = pygame.image.load("scissor.png")
scissor_image = pygame.transform.scale(scissor_image, (100, 100))

rock_objects = []
paper_objects = []
scissor_objects = []
