import pygame

class Ship:
    def __init__(self, ai_game):
        self.screen = ai_game.screen                            #Initialize the ship and set its starting position.
        self.screen_rect = ai_game.screen.get_rect()        

        self.image = pygame.image.load('images/ship.bmp')       # Load the ship image and get its rect.
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        self.screen.blit(self.image, self.rect)                 #Draw the ship at its current location