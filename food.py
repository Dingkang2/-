import pygame



class Food:

    def __init__(self, screen):
        self.screen = screen
        self.WHITE = 255, 255, 255
    
    def Draw_Food(self, Food_position):
        width, height = 8, 8
        size_and_position =Food_position[0], Food_position[1], width, height
        pygame.draw.rect(self.screen, self.WHITE, size_and_position, 0)