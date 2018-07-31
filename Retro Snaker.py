
import pygame
import random
from sys import exit
pygame.init()
screen = pygame.display.set_mode((800,800),0,32)
pygame.display.set_caption('Retro Snaker')
background = pygame.image.load('bg.jpg').convert()

class Body:
    def restart(self):
        self.x = 384
        self.y = 400
    def __init__(self):
        self.restart()
        self.image = pygame.image.load('body.png').convert_alpha()
    def setxy(self,a,b):
        self.x = a
        self.y = b
    def move(self,m):
        pass
    
class Food:
    def restart(self):
        self.x = random.randint(2,49)*16-8
        self.y = random.randint(2,49)*16-8
    def __init__(self):
        self.restart()
        self.image = pygame.image.load('body.png').convert_alpha()
    
class Head:
    def restart(self):
        self.x = 400-8
        self.y = 400-8
    def __init__(self):
        self.restart()
        self.image = pygame.image.load('body.png').convert_alpha()
    def setxy(self,a,b):
        self.x = a
        self.y = b
    def move(self,m):
        if m==0:
            self.x = self.x+16
        elif m==1:
            self.y = self.y+16
        elif m==2:
            self.x = self.x-16
        elif m==3:
            self.y = self.y-16
        else:
            pass
    


def checkEat(head,food):
    if head.x==food.x and head.y==food.y:
        return True
    else:
        return False
def checkHit(s):
    for i in s[1:]:
        if s[0].x==i.x and s[0].y==i.y:
            return True
    if s[0].x<=8 or s[0].x>=796 or s[0].y<=0 or s[0].y>=796:
        return True
    return False

gameover = False
head = Head()
snakes = [head]
for i in range(2):
    snakes.append(Body())
snakes[1].setxy(384-8,400-8)
snakes[2].setxy(368-8,400-8)
food = Food()
m=0
bodies = []
score = 0
font = pygame.font.SysFont('simhei',32)

while 1:
    speedlevel = score/500+1
    speed = int(500/speedlevel)
    pygame.time.delay(speed)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:         #运动状态控制
            if event.key == pygame.K_RIGHT:
                if m!=2:
                    m = 0
            if event.key == pygame.K_DOWN:
                if m!=3:
                    m = 1
            if event.key == pygame.K_LEFT:
                if m!=0:
                    m = 2
            if event.key == pygame.K_UP:
                if m!=1:
                    m = 3
        if gameover and event.key==pygame.K_SPACE:
            head.restart()
            snakes = [head]
            for i in range(2):
                snakes.append(Body())
            snakes[1].setxy(384-8,400-8)
            snakes[2].setxy(368-8,400-8)
            food.restart()
            m=0
            score = 0
            gameover = False
            

    screen.blit(background,(0,0))

    if not gameover:
        screen.blit(food.image,(food.x,food.y))   #绘制随机出现的食物
        bodies = []                              #坐标更迭
        for s in snakes[1:]:
            bodies.append((s.x,s.y))
        for i in range(len(snakes)-2):
            snakes[i+2].setxy(bodies[i][0],bodies[i][1])
        snakes[1].setxy(snakes[0].x,snakes[0].y)
        for s in snakes:
            s.move(m)
            
            screen.blit(s.image,(s.x,s.y))    #绘制蛇
        if checkHit(snakes):
            gameover = True
            
    
        if checkEat(snakes[0],food):
            body = Body()
            body.setxy(food.x,food.y)
            snakes.append(body)
            food.restart()
            score += 100
        text1 = font.render('得分：%d'%score,1,(0,0,0))
        screen.blit(text1,(0,0))
        text2 = font.render('等级：%d'%speedlevel,1,(0,0,0))
        screen.blit(text2,(0,50))
    else:
        text = font.render('你死了！\n得分：%d\n按空格重新开始'%score,1,(0,0,0))
        screen.blit(text,(250,350))
        
    pygame.display.update()
