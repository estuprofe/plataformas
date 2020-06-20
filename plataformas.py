import pygame
from pygame.locals import *
 
#pip install pygame into cmd, use 3.7 21/12/2019
 
pygame.init()
clock = pygame.time.Clock()
WINDOW_SIZE = (400, 400)
pygame.display.set_caption("Game")
screen = pygame.display.set_mode(WINDOW_SIZE, 0, 32)
# Image
player_image = pygame.image.load("player.png")
# other variables for movements
location = [50, 50]
moving_right = False
moving_left = False
 
# collitions
# rectangle that wraps the player
player_rect = pygame.Rect(location[0], location[1], player_image.get_width(), player_image.get_height())
# another rectangle for test
test = pygame.Rect(100, 100, 100, 50)
momentum = 0
 
loop = 1
while loop:
    # clear the screen
    screen.fill((146, 244, 255))
    # show the player
    screen.blit(player_image, location)
 
    # check if the player collide the test rectangle
    if player_rect.colliderect(test):
        print("collided")
        # if they collide the rectangle goes red
        pygame.draw.rect(screen, (255, 0, 0), test)
    else:
        # if not it is drawed in black
        pygame.draw.rect(screen, (0, 0, 0), test)
 
    player_rect.x = location[0]
    player_rect.y = location[1]
 
    # Goes down until reaches 0 then goes up til top and down again...
    if location[1] > WINDOW_SIZE[1] - player_image.get_height():
        momentum = -momentum
    else:
        momentum += 0.2
    location[1] += momentum
 
    if moving_right == True:
        location[0] += 4
 
    if moving_left == True:
        location[0] -= 4
 
    for event in pygame.event.get():
        if event.type == QUIT:
            loop = 0
        if event.type == KEYDOWN:
            if event.key == K_RIGHT:
                moving_right = True
            if event.key == K_LEFT:
                moving_left = True
        if event.type == KEYUP:
            if event.key == K_RIGHT:
                moving_right = False
            if event.key == K_LEFT:
                moving_left = False
 
    pygame.display.update()
    clock.tick(60)
 
pygame.quit()
