# import and initialize pygame
import pygame
pygame.init()
# configure the screen
screen = pygame.display.set_mode([500, 500])
# create a new instance of Surface
# surf = pygame.Surface((50, 50))
# surf.fill((255, 111, 33))



# make a class that draws a rectangle
class GameObject(pygame.sprite.Sprite):
    # def __init__(self, x, y, width, height):
    def __init__(self, x, y, image):

        super(GameObject, self).__init__()
        # self.surf = pygame.Surface((width, height))
        # self.surf.fill((255, 0, 255))
        self.surf = pygame.image.load(image)
        # self.rect = self.surf.get_rect()
        self.x = x
        self.y = y

    def render(self, screen):
        screen.blit(self.surf, (self.x, self.y))

# make an instance of GameObject
# box = GameObject(120, 300, 50, 50)
apple_1 = GameObject(75, 75, 'apple.png')
strawberry_1 = GameObject(250, 75, 'strawberry.png')
apple_2 = GameObject(425, 75, 'apple.png')
strawberry_2 = GameObject(75, 250, 'strawberry.png')
apple_3 = GameObject(250, 250, 'apple.png')
strawberry_3 = GameObject(250, 425, 'strawberry.png')
apple_4 = GameObject(75, 425, 'apple.png')
strawberry_4 = GameObject(250, 425, 'strawberry.png')
apple_5 = GameObject(425, 425, 'apple.png')

# create the time loop
running = True
while running:
    # looks at events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with white (clear the screen)
    screen.fill((255, 255, 255))
    # draw the surface
    # screen.blit(surf, (100, 120))

    # draw box
    # box.render(screen)
    apple.render(screen)
    strawberry.render(screen)#do something with even/odd
    # update the window
    pygame.display.flip()

