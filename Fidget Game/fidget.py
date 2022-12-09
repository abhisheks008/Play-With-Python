import pygame
import sys
from math import *

pygame.init()

WIDTH = 500
HEIGHT = 500

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
pygame.display.set_caption("Fidget Spinner")

# Colors
background = (0,191,173)
body_color = (0,96,101)
white = (240, 240, 240)
black = (0 , 0 , 0)
red = (176, 58, 46)
yellow = (250,212,2)
dark_yellow = (190, 152, 8)

LINE_WIDTH = 60

# Drawing of Fidget Spinner on Pygame Window
def show_spinner(angle):
    d = 80
    innerd = 50
    x = WIDTH/2 - d/2
    y = HEIGHT/2
    l = 200
    r = l/(3**0.5)
    w = 10
    
    # A little math for calculation the coordinates after rotation by some 'angle'
    # x = originx + r*cos(angle)
    # y = originy + r*sin(angle)
    
    centre = [x, y, d, d]
    centre_inner = [x + d/2 - innerd/2, y + d/2 - innerd/2, innerd, innerd]
    
    top = [x, y - l/(3)**0.5, d, d]
    top_inner = [x, y - l/(3)**0.5, innerd, innerd]

    top[0] = x + r*cos(radians(angle))
    top[1] = y + r*sin(radians(angle))
    top_inner[0] = x + d/2 - innerd/2 + r*cos(radians(angle))
    top_inner[1] = y + d/2 - innerd/2 + r*sin(radians(angle))
    
    left = [x - l/2, y + l/(2*(3)**0.5), d, d]
    left_inner = [x, y - l/(3)**0.5, innerd, innerd]

    left[0] = x + r*cos(radians(angle - 120))
    left[1] = y + r*sin(radians(angle - 120))
    left_inner[0] = x + d/2 - innerd/2 + r*cos(radians(angle - 120))
    left_inner[1] = y + d/2 - innerd/2 + r*sin(radians(angle - 120))
    
    
    right = [x + l/2, y + l/(2*(3)**0.5), d, d]
    right_inner = [x, y - l/(3)**0.5, innerd, innerd]

    right[0] = x + r*cos(radians(angle + 120))
    right[1] = y + r*sin(radians(angle + 120))
    right_inner[0] = x + d/2 - innerd/2 + r*cos(radians(angle + 120))
    right_inner[1] = y + d/2 - innerd/2 + r*sin(radians(angle + 120))
    
    # Drawing shapes on Pygame Window
    pygame.draw.line(screen, body_color, (top[0] + d/2, top[1] + d/2), (centre[0] + d/2, centre[1] + d/2), LINE_WIDTH)
    pygame.draw.line(screen, body_color, (left[0] + d/2, left[1] + d/2), (centre[0] + d/2, centre[1] + d/2), LINE_WIDTH)
    pygame.draw.line(screen, body_color, (right[0] + d/2, right[1] + d/2), (centre[0] + d/2, centre[1] + d/2), LINE_WIDTH)
    pygame.draw.ellipse(screen, yellow, tuple(centre))
    pygame.draw.ellipse(screen, dark_yellow, tuple(centre_inner))
    pygame.draw.ellipse(screen, body_color, tuple(top))
    pygame.draw.ellipse(screen, background, tuple(top_inner), 10)
    pygame.draw.ellipse(screen, body_color, tuple(left))
    pygame.draw.ellipse(screen, background, tuple(left_inner), 10)
    pygame.draw.ellipse(screen, body_color, tuple(right))
    pygame.draw.ellipse(screen, background, tuple(right_inner), 10)
    

# Displaying Information on Pygame Window
def show_info(friction, speed):
    font = pygame.font.SysFont("Times New Roman", 22)
    speedText = font.render("Click ←Left or Right→ to Spin ", True, black)
    screen.blit(speedText, (15, 15))
    tempText = font.render("Press 'Q' to exit", True, black)
    screen.blit(tempText, (15, 45))

# The Main Function
def main():
    spin = True
    angle = 0
    speed = 0.0
    friction = 0.03
    rightPressed = False
    leftPressed = False
    direction = 1
    
    while spin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    sys.exit()
                if event.key == pygame.K_RIGHT:
                    rightPressed = True
                    direction = 1
                if event.key == pygame.K_LEFT:
                    leftPressed = True
                    direction = -1
            if event.type == pygame.KEYUP:
                leftPressed = False
                rightPressed = False

        # Changing the Angle of rotation
        if direction == 1:
            if rightPressed:
                speed += 0.3
            else:
                speed -= friction
                if speed < 0:
                    speed = 0.0
        else:
            if leftPressed:
                speed -= 0.3
            else:
                speed += friction
                if speed > 0:
                    speed = 0.0
                    
        screen.fill(background)
        
        angle += speed

        # Displaying Information and the Fidget Spinner
        show_spinner(angle)
        show_info(friction, speed)
        
        pygame.display.update()
        clock.tick(90)

main()
