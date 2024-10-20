import pygame
import time
import random
pygame.init()
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)
DisplayWidth = 800
DisplayWeight = 600
dis = pygame.display.set_mode((DisplayWidth, DisplayWeight))
pygame.display.set_caption('Snake')
clock = pygame.time.Clock()
snake_block = 10
snake_speed = 15
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)
def YourScore(score):
    value = score_font.render("Your score: " + str(score), True, yellow)
    dis.blit(value, [0, 0])
def OurSnake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block])
def Message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [DisplayWidth / 6, DisplayWeight / 3])
def GameLoop():
    game_over = False
    game_close = False
    x1 = DisplayWidth / 2
    y1 = DisplayWeight / 2
    x1_change = 0
    y1_change = 0
    snake_List = []
    Length_of_snake = 1
    foodx = round(random.randrange(0, DisplayWidth - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, DisplayWeight- snake_block) / 10.0) * 10.0
    while not game_over:
        while game_close == True:
            dis.fill(blue)
            Message("you lose! Press Q to exit", red)
            YourScore(Length_of_snake - 1)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        GameLoop()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0
        if x1 >= DisplayWidth or x1 < 0 or y1 >= DisplayWeight or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        dis.fill(blue)
        pygame.draw.rect(dis, green, [foodx, foody, snake_block, snake_block])
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]
        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True
        OurSnake(snake_block, snake_List)
        YourScore(Length_of_snake - 1)
        pygame.display.update()
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, DisplayWidth - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, DisplayWeight - snake_block) / 10.0) * 10.0
            Length_of_snake += 1
        clock.tick(snake_speed)
    pygame.quit()
    quit()


GameLoop()