# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import sys
import pygame
from pygame.locals import QUIT

def main():
    pygame.init()
    window_surface = pygame.display.set_mode((1280, 720))
    pygame.display.set_caption('Black Jack')
    window_surface.fill((255, 255, 255))
    # 宣告 font 文字物件
    head_font = pygame.font.SysFont(None, 60)
    # 渲染方法會回傳 surface 物件
    bg = pygame.image.load("./image/table.png")
    # 更新畫面，等所有操作完成後一次更新（若沒更新，則元素不會出現）
    window_surface.blit(bg, (0, 0))
    pygame.display.update()
    # 事件迴圈監聽事件，進行事件處理
    while True:
        # 迭代整個事件迴圈，若有符合事件則對應處理
        for event in pygame.event.get():
            # 當使用者結束視窗，程式也結束
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

if __name__ == '__main__':
    main()

