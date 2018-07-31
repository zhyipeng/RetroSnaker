#-*- coding: utf-8 -*-
# by Yipeng Zhang

from ListNode import ListNode, LinkList
import pygame
import random


screen = pygame.display.set_mode((400-24, 400), 0, 32)


class GameBoard:
    # 25*25
    def __init__(self):
        self.gamemap = [[0 for i in range(25)] for j in range(25)]
        self.img = pygame.image.load('body.png').convert_alpha()

    def reset(self):
        self.gamemap = [[0 for i in range(25)] for j in range(25)]

    def updata(self, val):
        self.gamemap[val[0]][val[1]] = 1

    def delt(self, val):
        self.gamemap[val[0]][val[1]] = 0

    def show(self):
        for i in range(25):
            for j in range(25):
                if self.gamemap[i][j] == 1:
                    screen.blit(self.img, (i*16-8, j*16-8))




class Body(ListNode):

    def __init__(self, val=(0, 0), _next=None):
        self.val = list(val)
        self._next = _next
        self.image = pygame.image.load('body.png').convert_alpha()

    def reset(self, _next=None):
        self.val = [12, 12]
        if _next:
            self._next = _next

    def set(self, val, _next=None):
        self.val = list(val)
        if _next:
            self._next = _next

class Head(Body):

    def __init__(self, val=(12, 12), _next=None):
        self.val = list(val)
        self._next = _next
        self.image = pygame.image.load('body.png').convert_alpha()

    def reset(self, _next=None):
        self.val = [12, 12]
        if _next:
            self._next = _next

    def move(self, direction):
        if direction == 0:
            self.val[0] += 1
        elif direction == 1:
            self.val[1] += 1
        elif direction == 2:
            self.val[0] -= 1
        elif direction == 3:
            self.val[1] -= 1
        else:
            pass


class Food:

    def reset(self):
        x = random.randint(1, 23)
        y = random.randint(1, 23)
        self.val = [x, y]

    def __init__(self):
        self.reset()
        self.image = pygame.image.load('body.png').convert_alpha()

class Snake(LinkList):

    def __init__(self):
        self.reset()

    def reset(self):
        self._head = Head((12, 12))
        self.append(Body((11, 12)))
        self.append(Body((10, 12)))
        self.count = 3

    def checkEat(self, food):
        return self._head.val == food.val

    def checkHit(self):
        p = self._head._next
        while p:
            if self._head.val == p.val:
                return True
            if self._head.val[0] <= 0 or self._head.val[0] >= 24 or self._head.val[1] <= 0 or self._head.val[1] >= 24:
                return True
            p = p._next
        return False

    def move(self, direction):
        self._head.move(direction)
        if direction == 0:
            x = self._head.val[0] - 1
            y = self._head.val[1]
        elif direction == 1:
            x = self._head.val[0]
            y = self._head.val[1] - 1
        elif direction == 2:
            x = self._head.val[0] + 1
            y = self._head.val[1]
        else:
            x = self._head.val[0]
            y = self._head.val[1] + 1
        # x = (self._head.val[0] + self._head._next.val[0]) / 2
        # y = (self._head.val[1] + self._head._next.val[1]) / 2
        new_body = Body((x, y), self._head._next)
        self._head._next = new_body
        delt = self.pop_last()

        return (new_body.val, delt)



        # for p in self.elements():
        #     temp = p
        #     p.val = last.val
        #     last = temp



    def elements(self):     # 迭代器
        p = self._head
        while p:
            yield p
            p = p._next

    def append(self, node):      # 在表后插入元素
        if not self._head:
            self._head = node
            # self.count += 1
            return
        p = self._head
        while p._next:
            p = p._next
        p._next = node




if __name__ == '__main__':
    g = GameBoard()
    print(g.gamemap)
    print(len(g.gamemap))