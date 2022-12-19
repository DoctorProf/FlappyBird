import pygame, sys
from Score import Score
from Bird import Bird
from Columns import Columns


pygame.init()
pygame.display.set_caption('FlappyBird')
screen = pygame.display.set_mode((500, 700))
bird = Bird(screen)
col = [Columns(screen)]
sc = Score(screen)

while True:
    bird.update()

    for i in range(len(col)):
        if round(col[i].x, 3) == round(screen.get_width() / 2, 3):
            col.append(Columns(screen))
    
    for i in range(len(col)):   
        col[i].update()

    for i in range(len(col)):

        if (col[i].x < bird.rect.right < col[i].x + col[i].w) or (col[i].x < bird.rect.left < col[i].x + col[i].w):
            if not (bird.rect.top > col[i].space and col[i].space + col[i].prolet > bird.rect.bottom):
                print("Game Over")
                exit()
    
    if col[0].x + col[0].w < 0:
        col.pop(0)
        sc.score +=1
        print(sc.score)
    
    if bird.rect.bottom >= screen.get_height():
        print("Game Over")
        exit()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                bird.birdY -= 50

    screen.fill((128, 166, 255))
    bird.draw()
    rectBirdCenter = pygame.Rect(bird.rect.x, bird.rect.y, 5, 5)
    pygame.draw.rect(screen,(0,255,0), rectBirdCenter)
    for i in range(len(col)):
        col[i].draw()
    sc.ScoreImage()
    sc.showScore()
    pygame.display.update()