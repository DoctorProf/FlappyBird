import pygame

class Bird:
    def __init__(self, screen):
        self.screen = screen
        self.image = pygame.image.load(r'bird.png')
        self.rect = self.image.get_rect()
        self.rect.x = 30
        self.rect.y = screen.get_height() / 2
        self.birdY = self.rect.y

    def draw(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        self.birdY += 0.05
        self.rect.y = self.birdY
        print(self.rect.y)