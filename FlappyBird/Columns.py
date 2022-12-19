import pygame
from random import randint

class Columns:

    def __init__(self, screen):
        self.screen = screen
        self.prolet = 100
        self.space = randint(self.prolet, screen.get_height() - 2*self.prolet) 
        self.w = 50
        self.x = screen.get_width()
    
    def draw(self):
        pygame.draw.rect(self.screen,(0,255,0),self.rectTop)
        pygame.draw.rect(self.screen,(0,255,0),self.rectBottom)

    def update(self):
        self.rectTop = pygame.Rect(self.x, 0, self.w, self.space)
        self.rectBottom = pygame.Rect(self.x, self.space + self.prolet, self.w, self.screen.get_height() - self.space - self.prolet)
        self.x -= 0.05