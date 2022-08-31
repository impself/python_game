from turtle import Screen
import pygame
from pygame.sprite import Sprite
class Alien(Sprite):
    #表示单个外星人的类
    def __init__(self, ai_game) -> None:
        super().__init__()#初始化外星人并设置起始位置
        self.screen=ai_game.screen
        self.settings=ai_game.settings
        #加载外星人图像并设置其rect属性
        self.image=pygame.image.load('alien.bmp')
        self.rect=self.image.get_rect()
        #每个外星人都会出现在屏幕左上角附近
        self.rect.x=self.rect.width
        self.rect.y=self.rect.height
        #储存外星人的精确水平位置
        self.x=float(self.rect.x)
    def check_edges(self):
        screen_rect=self.screen.get_rect()
        if self.rect.right>=screen_rect.right or self.rect.left<0:
            return  True
    def update(self):
        self.x+=(self.settings.alien_speed*self.settings.fleet_direction)
        self.rect.x=self.x
        
        