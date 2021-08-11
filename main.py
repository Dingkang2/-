import pygame
import sys

from pygame.display import iconify
import snake
import random
from pygame import K_ESCAPE, K_w, K_s, K_a, K_d
from time import sleep
import collision_detection
import wall
import food
import pygame.freetype

def main():

    pygame.init()
    size = width, height = 600, 400
    BLACK = 0, 0, 0
    WHITE = 255, 255, 255
    RED = pygame.Color('red')
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('贪吃蛇')
    icon = pygame.image.load('.\\image\\icon.png')
    background = pygame.image.load('.\\image\\background.jpg')
    head_img = pygame.image.load('.\\image\\ball_up.png')
    head_img_rect = head_img.get_rect()
    pygame.display.set_icon(icon)

    fclock = pygame.time.Clock()
    fps = 20

    typeface = pygame.freetype.Font('C://Windows//Fonts//msyh.ttc', 36)

    body_len = 1
    initial_position = [296, 200]
    initial_speed = [vertical_speed, level_speed] = [8, 8]
    speed = [0, 8]
    Rote_date = []
    Rote_date.append(initial_position)
    add_body_len = 0

    Whether_to_proceed = 1

    Whether_food_exit = 0

    score = 0
    draw_score = False

    while True:
        screen.blit(background, (0, 0))
        Snake = snake.SNAKE(screen)
        food_ = food.Food(screen)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                if event.key == pygame.K_b:
                    body_len = 1
                    initial_position = [296, 200]
                    initial_speed = [vertical_speed, level_speed] = [8, 8]
                    speed = [0, 8]
                    Rote_date = []
                    Rote_date.append(initial_position)
                    add_body_len = 0
                    Whether_to_proceed = 1
                    Whether_food_exit = 0
                    score = 0
                    draw_score = False
                if event.key == pygame.K_w:
                    speed[0] = -initial_speed[0]
                    speed[1] = 0
                if event.key == pygame.K_s:
                    speed[0] = initial_speed[0]
                    speed[1] = 0
                if event.key == pygame.K_a:
                    speed[0] = 0
                    speed[1] = -initial_speed[1]
                if event.key == pygame.K_d:
                    speed[0] = 0
                    speed[1] = initial_speed[1]
                if event.key == pygame.K_UP:
                    add_body_len = 1
                    body_len += 1
                    score += 1
        if Whether_to_proceed != 0:
            if Whether_food_exit == 0:
                level = list(range(16, 584, 8)) # 71个
                vertical = list(range(16, 384, 8)) # 46 个

                level_num = random.randint(0, 70)
                vertical_num = random.randint(0, 45)

                food_position = [level[level_num], vertical[vertical_num]]
                print(food_position)
                Whether_food_exit = 1
                # sleep(3)
            print('food:', food_position)
            food_.Draw_Food(food_position)
            if Rote_date[0] == food_position:
                add_body_len = 1
                body_len += 1
                score += 1
                Whether_food_exit = 0

            Cache_local = [Rote_date[0][0] + speed[1], Rote_date[0][1] + speed[0]]
            # print(Cache_local)
            Rote_date.insert(0, Cache_local)
            print('Roto_date', Rote_date)
            if add_body_len == 0:
                Rote_date = Rote_date[: len(Rote_date) - 1]
                print(Rote_date)
            add_body_len = 0
            
            Snake.Draw_Snake(body_len, Rote_date)
            head_img_rect.left = Rote_date[0][0] - 5
            head_img_rect.top = Rote_date[0][1] - 5
            screen.blit(head_img, head_img_rect)
            Hit_Wall = wall.Draw_Wall(screen, Rote_date[0])

            if collision_detection.Collision_Detection(Rote_date) == 'yes' or Hit_Wall == 'yes':
                print('失败')
                score_surf, score_rect = typeface.render('成绩：' + str(score), fgcolor= WHITE, size= 36)
                score_rect.left = (600 - score_rect.width)/2
                score_rect.top = (400 - score_rect.height)/2
                print('成绩：', str(score))
                draw_score = True
        if draw_score == True:
            left_wall = pygame.draw.rect(screen, (255, 255, 255), (0, 0, 8, 400), 0)
            top_wall = pygame.draw.rect(screen, (255, 255, 255), (8, 0, 592, 8), 0)
            right_wall = pygame.draw.rect(screen, (255, 255, 255), (592, 8, 8, 392), 0)
            bottom_wall = pygame.draw.rect(screen, (255, 255, 255), (8, 392, 584, 8), 0)
            screen.blit(score_surf, score_rect)
            Whether_to_proceed = 0
        pygame.display.update()
        fclock.tick(fps)
        # sleep(0.05)

if __name__ == '__main__':
    main()