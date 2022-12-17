import pygame
import math
import random
import time

pygame.init()
clock = pygame.time.Clock()

# Set Screensize
screen_width, screen_height = 640, 480
screen = pygame.display.set_mode((screen_width, screen_height))

# Set Caption
pygame.display.set_caption("Baller")

# Set Background Color
screen.fill((0, 0, 0))



# Set Objects
ball_radius = 20
ball_pos = [320, 400]
ball_speed = 0.3

wall_height = 20
wall_width = 100
wall_pos = [0, 2]
wall_speed = 0.5

points = 0


running = True
while running:
    clock.tick(1000)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move Ball
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        ball_pos[0] -= ball_speed
    if keys[pygame.K_RIGHT]:
        ball_pos[0] += ball_speed

    # Limit Ball to Screen

    if ball_pos[0]  <= 0:
        ball_pos[0] = 0
    if ball_pos[0] >= 640:
        ball_pos[0] = 640



    # Move Wall
    if wall_pos[1] >= 460:
        wall_pos[1] = 2
        wall_pos[0] = random.randint(0,440)
        points += 1
    else:
        wall_pos[1] += wall_speed

    # Check Collision

    if (400 == (wall_pos[1] + 20)) and ((ball_pos[0] + ball_radius) >= wall_pos[0] and (ball_pos[0] - ball_radius) <= (wall_pos[0] + 100)):
        break

    # Draw Screen
    screen.fill((230, 230, 255))
    pygame.draw.circle(screen, (0, 0, 0), ball_pos, ball_radius)
    pygame.draw.rect(screen, (0, 0, 0), (*wall_pos, wall_width, wall_height))
    go_font = pygame.font.Font('freesansbold.ttf', 35)
    go_text = go_font.render('Punkte: ' + str(points), True, (0, 0, 0))
    screen.blit(go_text, (0, 0))
    pygame.display.flip()

# Game Over Screen (does not work)
#screen.fill((230, 230, 255))
#goii_font = pygame.font.Font('freesansbold.ttf', 65)

#goII_text = goii_font.render('Game Over', True, (0, 0, 0))
#screen.blit(goII_text, (320, 200))
#time.sleep(5)

#L = 10
#while L != 0:
#    goII_text = goii_font.render(str(L), True, (0, 0, 0))
#    screen.blit(goII_text, (320, 200))
#    L -= 1
#    time.sleep(1)


 # End Pygame
print(points)
pygame.quit()
