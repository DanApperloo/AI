__author__ = 'Dan Apperloo'
__email__ = "danapperloo@gmail.com"


#########################################################################
# Imports
#########################################################################
import pygame


#########################################################################
# Functions
#########################################################################
class Player(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 50), pygame.SRCALPHA)
        self.image.fill((255, 255, 255, 0))
        pygame.draw.circle(self.image, (0, 0, 255), (25, 25), 25, 0)
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.center = pygame.mouse.get_pos()


class PygameLocalDisplay(object):

    FPS_LIMIT = 30

    def __init__(self):
        # Create a Screen object
        self.screen = pygame.display.set_mode((1024, 768))

        # Setup a background
        self.background = pygame.Surface(self.screen.get_size())
        self.background.fill((255, 255, 255))

        self.player = Player()
        self.all_sprites = pygame.sprite.Group(self.player)

        self.clock = pygame.time.Clock()

        self.screen.blit(self.background, (0, 0))

    def display(self):

        self.clock.tick(self.FPS_LIMIT)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False

        self.all_sprites.clear(self.screen, self.background)
        self.all_sprites.update()
        self.all_sprites.draw(self.screen)

        pygame.display.flip()
        return True
