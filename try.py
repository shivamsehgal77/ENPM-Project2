
import pygame
import functions
import sys
# Initialize Pygame
pygame.init()

# Set up the window
width = 800
height = 600
screen = pygame.display.set_mode((width, height))

# Set up the pixel
pixel_color = (255, 0, 0) # Red
pixel_x = 0
pixel_y = height // 2

# Game loop
clock = pygame.time.Clock()
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Move the pixel
    pixel_x += 1

    # Draw the pixel
    screen.fill((255, 255, 255)) # Fill the screen with white
    pygame.draw.line(screen, pixel_color, (0, pixel_y), (pixel_x, pixel_y), 1)

    # Update the display
    pygame.display.update()

    # Limit the frame rate
    clock.tick(60)