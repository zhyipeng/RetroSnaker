#-*- coding: utf-8 -*-
# by Yipeng Zhang

from model import *


# 初始化
pygame.init()
screen = pygame.display.set_mode((400, 400), 0, 32)
pygame.display.set_caption('Retro Snaker')
background = pygame.image.load('bg.jpg').convert()
font = pygame.font.SysFont('simhei', 16)

snake = Snake()
food = Food()
direction = 0
isGameover = False
score = 0

# 主循环
while 1:
    speedlevel = score / 500 + 2
    speed = int(500 / speedlevel)
    pygame.time.delay(speed)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:         # 运动状态控制
            if event.key == pygame.K_RIGHT:
                if direction != 2:
                    direction = 0
            if event.key == pygame.K_DOWN:
                if direction != 3:
                    direction = 1
            if event.key == pygame.K_LEFT:
                if direction != 0:
                    direction = 2
            if event.key == pygame.K_UP:
                if direction != 1:
                    direction = 3
            if isGameover and event.key == pygame.K_SPACE:
                snake.reset()
                food.reset()
                direction = 0
                score = 0
                isGameover = False

    screen.blit(background, (0, 0))

    if not isGameover:
        screen.blit(food.image, (food.val[0], food.val[1]))  # 绘制随机出现的食物

        snake.move(direction)

        for p in snake.elements():
            screen.blit(p.image, (p.val[0], p.val[1]))

        if snake.checkHit():
            isGameover = True

        if snake.checkEat(food):
            snake.append(Body((food.val[0], food.val[1])))
            food.reset()
            score += 100

        _score = font.render('得分：%d' % score, 1, (0, 0, 0))
        _level = font.render('等级：%d' % speedlevel, 1, (0, 0, 0))
        screen.blit(_score, (0, 0))
        screen.blit(_level, (0, 25))

    else:
        _dead = font.render('你死了！\n得分：%d\n按空格重新开始' % score, 1, (0, 0, 0))
        screen.blit(_dead, (120, 175))

    pygame.display.update()