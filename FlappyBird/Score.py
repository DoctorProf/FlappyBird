import pygame

class Score():

    def __init__(self, screen):

        self.screen = screen
        self.score = 0
        self.screenRect = screen.get_rect()
        self.textColor = (0,0,0)
        self.font = pygame.font.SysFont(None, 36)
        self.ScoreImage()
        

    def ScoreImage(self):

        self.ScoreImg = self.font.render(str(self.score), True, self.textColor, (255,255,255))
        self.scoreRect = self.ScoreImg.get_rect()
        self.scoreRect.right = self.screenRect.right - 40
        self.scoreRect.top = 20

    
    def showScore(self):
        self.screen.blit(self.ScoreImg, self.scoreRect)