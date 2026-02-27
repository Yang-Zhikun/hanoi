import pygame
pygame.init()
screen = pygame.display.set_mode((800, 600))
# screen.fill((255, 0, 0))          # 这里指定颜色 (紫色)
# pygame.display.flip()          # 或者 pygame.display.update()
pygame.display.set_caption("Hello, Pygame!显示中文") # 标题可以显示中文，但surface不能直接显示中文，需要使用字体渲染

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 填充背景颜色
    screen.fill((30, 30, 30))  # 深灰背景

    # 绘制几何图形
    pygame.draw.rect(screen, (0, 128, 255), (50, 50, 200, 100))       # 矩形
    pygame.draw.circle(screen, (255, 100, 0), (400, 300), 75)          # 圆
    pygame.draw.line(screen, (0, 255, 0), (0, 0), (800, 600), 5)       # 线
    pygame.draw.ellipse(screen, (255, 255, 0), (300, 400, 150, 80), 3) # 椭圆

    # 刷新屏幕
    pygame.display.flip()

# pygame.quit()