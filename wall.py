import pygame
def Draw_Wall(screen, head):
    left_wall = pygame.draw.rect(screen, (255, 255, 255), (0, 0, 8, 400), 0)
    top_wall = pygame.draw.rect(screen, (255, 255, 255), (8, 0, 592, 8), 0)
    right_wall = pygame.draw.rect(screen, (255, 255, 255), (592, 8, 8, 392), 0)
    bottom_wall = pygame.draw.rect(screen, (255, 255, 255), (8, 392, 584, 8), 0)

    YesorNO = 0
    if head[0] < 8 or head[0] > 592:
        YesorNO = 'yes'
    if head[1] < 6 or head[1] > 384:
        YesorNO = 'yes'
    return YesorNO