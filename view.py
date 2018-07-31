#-*- coding: utf-8 -*-
# by Yipeng Zhang

import pygame

pygame.init()
screen = pygame.display.set_mode((800, 800), 0, 32)
pygame.display.set_caption('Retro Snaker')
background = pygame.image.load('bg.jpg').convert()

font = pygame.font.SysFont('simhei', 32)