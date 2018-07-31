#-*- coding: utf-8 -*-
# by Yipeng Zhang
import pygame
import random
from ListNode import ListNode, LinkList


class Body(ListNode):

    def __init__(self, val=(384, 400), _next=None):
        self.val = list(val)
        self._next = _next
        self.image = pygame.image.load('body.png').convert_alpha()

    def reset(self, _next=None):
        self.val = [384, 400]
        if _next:
            self._next = _next

    def set(self, val, _next=None):
        self.val = list(val)
        if _next:
            self._next = _next

class Head(Body):

    def __init__(self, val=(382, 382), _next=None):
        self.val = list(val)
        self._next = _next
        self.image = pygame.image.load('body.png').convert_alpha()

    def reset(self, _next=None):
        self.val = [382, 382]
        if _next:
            self._next = _next

    def move(self, direction):
        if direction == 0:
            self.val[0] += 16
        elif direction == 1:
            self.val[1] += 16
        elif direction == 2:
            self.val[0] -= 16
        elif direction == 3:
            self.val[1] -= 16
        else:
            pass


class Food:

    def reset(self):
        x = random.randint(2, 24)*16-8
        y = random.randint(2, 24)*16-8
        self.val = [x, y]

    def __init__(self):
        self.reset()
        self.image = pygame.image.load('body.png').convert_alpha()

class Snake(LinkList):

    def __init__(self):
        self.reset()

    def reset(self):
        self._head = Head((192 + 8, 200))
        self.append(Body((192 - 8, 200)))
        self.append(Body((184 - 8, 200)))
        self.count = 3

    def checkEat(self, food):
        return self._head.val == food.val

    def checkHit(self):
        p = self._head._next
        while p:
            if self._head.val[0] == p.val[0] and self._head.val[1] == p.val[1]:
                return True
            if self._head.val[0] <= 8 or self._head.val[0] >= 392 or self._head.val[1] <= 0 or self._head.val[1] >= 392:
                return True
            p = p._next
        return False

    def move(self, direction):
        self._head.move(direction)
        if direction == 0:
            x = self._head.val[0] - 16
            y = self._head.val[1]
        elif direction == 1:
            x = self._head.val[0]
            y = self._head.val[1] - 16
        elif direction == 2:
            x = self._head.val[0] + 16
            y = self._head.val[1]
        else:
            x = self._head.val[0]
            y = self._head.val[1] + 16
        # x = (self._head.val[0] + self._head._next.val[0]) / 2
        # y = (self._head.val[1] + self._head._next.val[1]) / 2
        new_body = Body((x, y), self._head._next)
        self._head._next = new_body
        self.pop_last()


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
