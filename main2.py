#-*- coding: utf-8 -*-
# by Yipeng Zhang

from model2 import *
import bfs, bfs2


# 初始化
pygame.init()
# screen = pygame.display.set_mode((400, 400), 0, 32)
pygame.display.set_caption('Retro Snaker')
background = pygame.image.load('bg.jpg').convert()
font = pygame.font.SysFont('simhei', 16)
font1 = pygame.font.SysFont('simhei', 10)

snake = Snake()
food = Food()
direction = 0
isGameover = False
score = 0
g = GameBoard()
start = 0
isAi = False
i = 0

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
            if event.key == pygame.K_a:
                isAi = True
            if event.key == pygame.K_p:
                isAi = False
            if isGameover and event.key == pygame.K_SPACE:
                snake.reset()
                food.reset()
                direction = 0
                score = 0
                isGameover = False

    screen.blit(background, (0, 0))
    pygame.draw.line(screen, (0, 0, 0), (0, 0), (400, 0), 2)
    pygame.draw.line(screen, (0, 0, 0), (0, 0), (0, 400), 2)
    pygame.draw.line(screen, (0, 0, 0), (0, 400-24), (400-24, 400-24), 2)
    pygame.draw.line(screen, (0, 0, 0), (400-24, 0), (400-24, 400-24), 2)


    if not isGameover:

        if 1:
            # dire = bfs.ai(g.gamemap, snake._head.val, food.val)
            print(g.gamemap, snake._head.val, food.val)
            dire = bfs2.maze_solver_queue(g.gamemap, snake._head.val, food.val)
            print(dire)
            if 0:
                direction = dire[i]
            # if dire:
            #     for d in dire:
            #         direction = d
            # else:
            #     direction = random.choice([0, 1, 2, 3])
        g.reset()
        g.updata(food.val)

        snake.move(direction)
        i += 1
        # g.updata(up[0])
        # g.delt(up[1])
        for s in snake.elements():
            g.updata(s.val)
        g.show()
        # print(g.gamemap)

        if snake.checkHit():
            isGameover = True
            i = 0

        if snake.checkEat(food):
            snake.append(Body((food.val[0], food.val[1])))
            food.reset()
            score += 100

        _score = font.render('得分：%d' % score, 1, (0, 0, 0))
        _level = font.render('等级：%d' % speedlevel, 1, (0, 0, 0))
        screen.blit(_score, (0, 380))
        screen.blit(_level, (100, 380))

    else:
        _dead2 = font.render('你死了！ 得分：%d' % score, 1, (0, 0, 0))
        _dead3 = font1.render('按空格重新开始', 1, (0, 0, 0))
        screen.blit(_dead2, (120, 170))
        screen.blit(_dead3, (150, 240))

    pygame.display.update()