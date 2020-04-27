import time as tm
import pygame
import sys
from pygame import *
from math import *
import random

def night_to_day():
    r = 2
    g = 35
    b = 68
    arr = []
    while g < 255 and b < 255:
        if g != 255:
            g += 1
        if b != 255:
            b += 1
        color_ = tuple([r, g ,b])
        arr.append(color_)
    return arr

def draw_car():
    car.fill(unvis)
    draw.rect(car, WHITE, [0, 300, 300, 40])
    draw.rect(car, BLACK, [80, 220, 150, 80])
    draw.rect(car, WINDOW, [82, 222, 70, 78])
    draw.rect(car, WINDOW, [155, 222, 73, 78])
    draw.circle(car, BLACK, [195, 260] , 10)
    draw.line(car, BLACK, [195,260], [195,300])
    draw.line(car, BLACK, [218,275], [228, 300])
    draw.circle(car, BLACK, [218, 280] , 7)
    draw.line(car, BLACK, [195, 280],[218,275])
    draw.rect(car, YELLOW, [280, 310, 20, 10])
    draw.rect(car, RED, [0, 310, 20, 10])
    draw.rect(car, BLACK, [90, 310, 15, 5])
    draw.rect(car, BLACK, [165, 310, 15, 5])

def draw_wheel():
    wheel.fill(unvis)
    draw.circle(wheel, ORANGE, [50, 50], 25)
    draw.line(wheel, BLACK, [50,50], [50,25])
    draw.line(wheel, BLACK, [50,50], [25,50])
    draw.line(wheel, BLACK, [50,50], [50,75])
    draw.line(wheel, BLACK, [50,50], [75,50])

def draw_man(y):
    man.fill(unvis)
    draw.circle(man, BLACK, [100, 100], 10)
    draw.line(man, BLACK, [100,100], [100, 145])
    draw.line(man, BLACK, [100,145], [105,168])
    draw.line(man, BLACK, [100,145], [90, 160])
    draw.line(man, BLACK, [90,160], [90, 168])
    draw.line(man, BLACK, [100, 115], [90, 130])
    draw.line(man, BLACK, [90, 130], [85, 125])
    draw.line(man, BLACK, [100, 115], [125, y])

def draw_clouds():
    cloud.fill(unvis)
    for i in range(20,100,20):
        draw.circle(cloud, WHITE, [i,20], 15)
    for i in range(0,100,20):
        draw.circle(cloud, WHITE, [i + 100, 70], 15)
    for i in range(0,100,20):
        draw.circle(cloud, WHITE, [i + 200,20], 15)
    for i in range(0,100,20):
        draw.circle(cloud, WHITE, [i + 400,20], 15)
    for i in range(0,100,20):
        draw.circle(cloud, WHITE, [i + 300, 70], 15)

def draw_tree():
    tree.fill(unvis)
    draw.rect(tree, GREEN, [182, 222, 70, 83])

def draw_moon():
    moon.fill(unvis)
    starss.fill(unvis)
    draw.ellipse(moon, LIGHT_GREY, Rect((0, 300), (40,40)),0)
    draw.ellipse(moon, unvis, Rect((10, 300), (40,40)),0)
    for star in stars:
        xxx, yyy = star[0], star[1]
        draw.line(starss, WHITE, (xxx, yyy), (xxx, yyy))

def draw_sun():
    sun.fill(unvis)
    x=10
    draw.ellipse(sun,YELLOW,Rect((0,300),(40,40)),0)
    
def draw_road():
    x = 0
    y = 320
    road.fill(unvis)
    draw.rect(road, GREY, [0,250,600,200]) 
    for i in range(20):
        draw.rect(road, WHITE, [x,y,20, 10])
        x += 40

def rotate(surf, rect, angle):
    new_sur = transform.rotate(surf, angle)
    rect = new_sur.get_rect(center = rect.center)
    return new_sur, rect

pygame.init()
clock = time.Clock()

unvis = (186, 1, 146)
NIGHT = (2, 36, 69)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (15, 231, 255)
LIGHT_GREY = (215, 213, 215)
GREY = (136, 132, 132)
YELLOW = (246, 255, 0)
WINDOW = (157, 214, 232)
ORANGE = (247, 112, 2)
night_day_grad = night_to_day()

screen = display.set_mode((1600,1400),0,32)
display.set_caption("Animation")

bg = Surface(screen.get_size())
car = Surface((400,400))
wheel = Surface((100,100))
man = Surface((200,200))
cloud = Surface((600,300))
sun = Surface((600,600))
moon = Surface((600,400))
starss = Surface((400, 400))
road = Surface((600, 400))
tree = Surface((200, 200))

man.set_colorkey(unvis)
car.set_colorkey(unvis)
bg.set_colorkey(unvis)
wheel.set_colorkey(unvis)
screen.set_colorkey(unvis)
cloud.set_colorkey(unvis)
sun.set_colorkey(unvis)
moon.set_colorkey(unvis)
starss.set_colorkey(unvis)
road.set_colorkey(unvis)
tree.set_colorkey(unvis)

bg.fill(NIGHT)

orig_wheel = wheel
rect = wheel.get_rect(center=(50,50))
angle = 0
stars = [(random.randint(0, 600), random.randint(0, 600)) for x in range(100)]
x = 0
y = 320
    
car_x = 0
cloud_X = -500
angle = -1
y = 100
step = 0.5

draw_car()
draw_wheel()
draw_clouds()
draw_sun()
draw_moon()
draw_road()
draw_tree()
#GRAVITY
delta_t = 0.01
m = 1
g = 9.8
fx = 0
fy = m * g
sun_x = -50
sun_y = 0
angle = 60
theta = radians(angle)

v = 90
vx = v * cos(theta) 
vy = -v * sin(theta)

day = True
done = False
flag = False
col = 0
tick = 0
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    tick += 1
    draw_man(y)
    screen.blit(bg, (0,0))
    if day:
        tick += 1
        if tick < 2500:
            if col < 185:
                col += 1
            bg.fill(night_day_grad[col])
        
        if tick > 2500:
            if col > 2:
                col -= 1
            bg.fill(night_day_grad[col])
        
        screen.blit(bg, (0,0))
        screen.blit(sun,(int(sun_x), int(sun_y)))
    else:
        col = 0
        tick = 0
        bg.fill(NIGHT)
        screen.blit(starss, (50,-150))
        screen.blit(moon, (int(sun_x),int(sun_y)))
    screen.blit(man, [400,80])
    screen.blit(road, (0,0))
    screen.blit(cloud, [cloud_X,0])
    screen.blit(tree,(100,100))
    screen.blit(car,(car_x,0))
    
    wheel, rect = rotate(orig_wheel, rect, angle)
    x1 = rect[0]
    y1 = rect[1]
    screen.blit(wheel,[x1+ car_x, y1 + 288])
    screen.blit(wheel,[x1 + car_x + 200, y1 + 288])
    
    if cloud_X > 600:
        cloud_X = -500
    if car_x > 600:
        car_x = -400
    if y > 125 or y < 100:
        step *= -1
    if sun_x > 600:
        day = not day
        sun_x = -50
        sun_y = 0
        
        vx = v * cos(theta) 
        vy = -v * sin(theta)
        vx = vx + (fx / m) * delta_t
        vy = vy + (fy / m) * delta_t
        sun_x = sun_x + vx * delta_t
        sun_y = sun_y + vy * delta_t

    car_x += 2
    angle -= 2
    cloud_X += 0.2
    y += step

    vx = vx + (fx / m) * delta_t
    vy = vy + (fy / m) * delta_t
    sun_x = sun_x + vx * delta_t
    sun_y = sun_y + vy * delta_t

    display.flip()
    clock.tick(60)
    display.update()
    
pygame.quit()

