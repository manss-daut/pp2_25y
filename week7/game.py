import pygame
import datetime

pygame.init()

WIDTH, HEIGHT = 500, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mickey Clock")

mickey_img = pygame.image.load("mickeyclock.jpeg")
mickey_img = pygame.transform.scale(mickey_img, (WIDTH, HEIGHT))

right_hand_rect = pygame.Rect(200, 100, 100, 200)
left_hand_rect = pygame.Rect(100, 100, 100, 200)

right_hand = mickey_img.subsurface(right_hand_rect).copy()
left_hand = mickey_img.subsurface(left_hand_rect).copy()

center = (WIDTH // 2, HEIGHT // 2)

clock = pygame.time.Clock()
running = True
while running:
    screen.fill((255, 255, 255))
    screen.blit(mickey_img, (0, 0))
    
    now = datetime.datetime.now()
    minutes, seconds = now.minute, now.second
    
    angle_minutes = -minutes * 6
    angle_seconds = -seconds * 6
    
    rotated_right = pygame.transform.rotate(right_hand, angle_minutes)
    rotated_left = pygame.transform.rotate(left_hand, angle_seconds)
    
    rh_rect = rotated_right.get_rect(center=center)
    lh_rect = rotated_left.get_rect(center=center)
    
    screen.blit(rotated_right, rh_rect.topleft)
    screen.blit(rotated_left, lh_rect.topleft)
    
    pygame.display.flip()
    clock.tick(30)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()