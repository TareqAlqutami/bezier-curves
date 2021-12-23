import pygame
import os
from positions import Position
from curves import *

# code adapted from https://github.com/Josephbakulikira/Bezier-Curve-animation-using-python

# os.environ["SDL_VIDEO_CENTERED"] = '1'
width,height = 1400,700
size = (width,height)

pygame.init()
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
fps = 60
font = pygame.font.Font("freesansbold.ttf",32)

#colors
white = (235,235,235)
black = (20,20,20)
red = (242,2,2)
green = (2,242,102)
blue = (2,146,255)
purple = (205,163,255)

t = 0
speed = 0.002
linear_positions = [
    Position(100,600,"P0"), 
    Position(300,200,"P1")
    ]

quadratic_positions = [
    Position(460,600,"P0"), 
    Position(680,350,"P1"),
    Position(520,200,"P2")
    ]

cubic_positions = [
    Position(850,600,"P0"), 
    Position(980,350,"P1"),
    Position(1150,600,"P2"),
    Position(1350,200,"P3"),
    ]

quadratic_curve = []
cubic_curve = []
curve1,curve2,curve3 = [],[],[]

run = True

while run:
    clock.tick(fps)
    screen.fill(white)
    pygame.display.set_caption(f"Bezier curves - FPS({int(clock.get_fps())})")

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run = False
    

    text = font.render(f" T = {str(t)[:5]}",True,black)
    textRec = text.get_rect()
    textRec.center = (700, 30)
    screen.blit(text,textRec)


    linear = font.render("Linear " , True, black)
    textRect = linear.get_rect()
    textRect.center = (300, 60)
    screen.blit(linear, textRect)

    quad = font.render("Quadratic", True, black)
    textRect = quad.get_rect()
    textRect.center = (800, 60)
    screen.blit(quad, textRect)

    cubic = font.render("Cubic", True, black)
    textRect = cubic.get_rect()
    textRect.center = (1200, 60)
    screen.blit(cubic, textRect)

    #separator ---- | ----- | ------
    pygame.draw.line(screen, purple, (350, 850), (350, 150), 1)
    pygame.draw.line(screen, purple, (800, 850), (800, 150), 1)

    LinearCurve(linear_positions,t,screen,red)
    QuadraticCurve(quadratic_positions,t,screen,red,quadratic_curve,green)
    CubicCurve(cubic_positions, t, screen, red, cubic_curve, green, blue, curve1, curve2, curve3)

    if len(quadratic_curve)>2:
        pygame.draw.lines(screen,red,False,quadratic_curve,5)

    if len(curve1)>2:
        pygame.draw.lines(screen, (179, 179, 179),False,  curve1, 3)
    if len(curve2)>2:
        pygame.draw.lines(screen, (179, 179, 179),False,  curve2, 3)
    if len(curve3)>2:
        pygame.draw.lines(screen, (179, 179, 179),False,  curve3, 3)
    if len(cubic_curve)>2:
        pygame.draw.lines(screen, red,False,  cubic_curve, 5)

    if t>=1:
        t = 0
        quadratic_curve.clear()
        cubic_curve.clear()
        curve1.clear()
        curve2.clear()
        curve3.clear()

    for point in linear_positions:
        point.display(screen,black)
    for point in quadratic_positions:
        point.display(screen,black)
    for point in cubic_positions:
        point.display(screen,black)

    t+=speed

    pygame.display.update()

pygame.quit()