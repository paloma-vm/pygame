# Import and initialize pygame
import pygame
pygame.init()

# Color constants
RED = (255, 0, 0)
ORANGE = (255, 165, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
LIGHT_BLUE = (102, 204, 255)

# position Variables
red_x = 50
red_y = 50


# Configure the screen size
screen = pygame.display.set_mode([500, 500])

# self.spots = [[0 for i in range(3)] for j in range(3)]

# Create the game loop
running = True
while running:
    # Looks at events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill((255, 255, 255))
    # ^color value is expressed as a tuple
    # Draw a circle
    # color = (255, 0, 255)
    
    # position = (250, 250)
    # ^ x and y coords
    # pygame.draw.circle(screen, color, position, 75)
    # pygame.draw.circle(screen, (255, 0, 0), (75, 75), 75)
    # pygame.draw.circle(screen, (255, 165, 0), (425, 75), 75)
    # pygame.draw.circle(screen, (255, 255, 0), (250, 250), 75)
    # pygame.draw.circle(screen, (0, 255, 0), (75, 425), 75)
    # pygame.draw.circle(screen, (102, 204, 255), (425, 425), 75)

    # challenge 2
    # pygame.draw.circle(screen, (100, 100, 100), (75, 75), 75)
    # pygame.draw.circle(screen, (255, 165, 0), (425, 75), 75)
    # pygame.draw.circle(screen, (255, 255, 0), (250, 250), 75)
    # pygame.draw.circle(screen, (0, 255, 0), (75, 425), 75)
    # pygame.draw.circle(screen, (102, 204, 255), (425, 425), 75)

    for y in range(9):
        for x in range (9):
            pygame.draw.circle(screen, (100, 100, 100), ((((x//3)*175)+75), ((((x%3)+1)*175)-(100))), 75)
            

    # Update the display
    pygame.display.flip()
