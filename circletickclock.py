import pygame
import sys
import datetime
import math

pygame.init()

screen = pygame.display.set_mode((750, 450))
clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 50)
pygame.display.set_caption("hieeNewClock")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Get current time
    now = datetime.datetime.now()
    current_time = now.strftime("%H:%M:%S")

    # Fill the screen with white
    screen.fill((255, 255, 255))

    # Draw the circle
    circle_center = (750 // 2, 450 // 2)
    circle_radius = 150
    pygame.draw.circle(screen, (0, 0, 0), circle_center, circle_radius, 2)  # Draw the outline of the circle

    # Render the current time text
    time_text = font.render(current_time, True, (0, 0, 0))
    text_rect = time_text.get_rect(center=circle_center)

    # Blit the text inside the circle
    screen.blit(time_text, text_rect)

    # Update the display
    pygame.display.flip()

    # Cap the frame rate to 1 frame per second
    clock.tick(1)
