import pygame

class SNAKE:
    def __init__(self, screen):
        self.screen = screen
        self.WHITE = 255, 255, 255

    def Draw_Body_rect(self, position):
        width, height = 8, 8
        size_and_position = position[0], position[1], width, height
        pygame.draw.rect(self.screen, self.WHITE, size_and_position, 0)

    def Draw_Snake(self, body_len, Rote_date):
        self.body_len = body_len
        self.Rote_date = Rote_date
        print('Draw_Snake')

        for len_date in range(body_len):
            self.Draw_Body_rect(Rote_date[len_date])
            print('Draw_Body_rect')