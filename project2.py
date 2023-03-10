import pygame
import sys

# Initialize Pygame
pygame.init()
# Initializing surface

white=(255,255,255)
# Initializing Color

red = (255,0,0)
green = (0,255,0)
# points_hexgon = [(443.30, 125),(421.65, 164.33),(378.35, 164.33),(356.70, 125),(378.35, 85.67),(421.65, 85.67)]
points_triangle = [(460, 25), (460, 225), (510, 125)]
points_hexgon = [(300,44.22649731),(230.04809472,84.61324865),(230.04809472,165.38675135),(300,205.77350269),(369.95190528,165.38675135),(369.95190528,84.61324865)]
points_triangle_border = [(455,246.18033989),(455.00,3.81966011),(515.59016994,125)]
# points_triangle_border = 
# Set the dimensions of the screen
screen = pygame.display.set_mode((600, 250))
pygame.draw.rect(screen, white, pygame.Rect(5,5,590,240))
pygame.draw.rect(screen,green,pygame.Rect(95,5,60,105))
pygame.draw.rect(screen, red, pygame.Rect(100, 5, 50, 100))
pygame.draw.rect(screen, green, pygame.Rect(95, 140, 60, 105))
pygame.draw.rect(screen, red, pygame.Rect(100, 145, 50, 100))
# pygame.draw.polygon(screen, green, points_triangle_border)
pygame.draw.polygon(screen, red, points_triangle)
pygame.draw.polygon(screen, red, points_hexgon)

# Infinite loop to hold the canvas
while True:
    # Event loop to handle user inputs
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Update the screen
    pygame.display.update()