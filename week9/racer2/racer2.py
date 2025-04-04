import pygame, sys
from pygame.locals import *
import random, time
 
#Initializing 
pygame.init()
 
#Setting up FPS 
FPS = 60
FramePerSec = pygame.time.Clock()
 
#Creating colors
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
 
#Other Variables for use in the program
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
#Adding Speed variable
SPEED = 5
#Nu points variable ponyatno
SCORE = 0
#Nu dobavim tenge
TENGE = 0
LAST_TENGE = 0

#Setting up Fonts
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)

background = pygame.image.load("Back.png")

#Create a white screen 
DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Game")
 
 
#Creating class and adding png like a sprite 
class Enemy(pygame.sprite.Sprite):
      def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("Enemy1-removebg-preview.png")
        self.image = pygame.transform.scale(self.image, (85, 85))
        self.rect = self.image.get_rect()
        self.rect.inflate_ip(-50, -15)
#Spawn in random position
        self.rect.center = (random.randint(40,SCREEN_WIDTH-40), 0)    
#For moves(falling from top of the screen) 
      def move(self):
        global SCORE
        self.rect.move_ip(0,SPEED)
        if (self.rect.top > 600):
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(30, 370), 0)
 
#Same class fro player sprite
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("Player1-removebg-preview.png")
        self.image = pygame.transform.scale(self.image, (85, 85))
        self.rect = self.image.get_rect()
        self.rect.inflate_ip(-50, -15)
        self.rect.center = (160, 520)

#Moving by keys left, right        
    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -5)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0,5)
#First if for not to let out of screen         
        if self.rect.left > 0:
            if pressed_keys[K_LEFT]:
                self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH:        
            if pressed_keys[K_RIGHT]:
                self.rect.move_ip(5, 0)

#Class dlya tenge
class Tenge(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("tenge-removebg-preview.png")
        self.image = pygame.transform.scale(self.image, (30, 30))
        self.rect = self.image.get_rect()
        self.rect.inflate_ip(5, 5)
        #poo umolchaniyu = 1
        self.value = 1
        self.respawn()

#chtob do move ne dokopalis'
    def move(self):
        pass
#randomnuy spawn po screen
    def respawn(self):
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), random.randint(100, SCREEN_HEIGHT - 200))
        #randomny value 1-5
        self.value = random.choice([1, 2, 3, 4, 5])


#Setting up Sprites        
P1 = Player()
E1 = Enemy()
TG = Tenge()

#Creating Sprites Groups
enemies = pygame.sprite.Group()
enemies.add(E1)
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)
all_sprites.add(TG)
 
#Adding a new User event for increasing speed(+1 for unic userevent number)
#INC_SPEED = pygame.USEREVENT + 1
#pygame.time.set_timer(INC_SPEED, 1000)

#Game Loop
while True:
       
    #Cycles through all events occuring  
    for event in pygame.event.get():
        #if event.type == INC_SPEED:
              #SPEED += 0.5
           
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    DISPLAYSURF.blit(background, (0,0))
    
 
    #Moves and Re-draws all Sprites
    for entity in all_sprites:
        DISPLAYSURF.blit(entity.image, entity.rect)
        entity.move()
    
    #To be run if collision occurs between Player and Enemy
    if pygame.sprite.spritecollideany(P1, enemies):
          pygame.mixer.Sound('crash.wav').play()
          time.sleep(0.5)
                    
          DISPLAYSURF.fill(RED)
          DISPLAYSURF.blit(game_over, (30,250))
           
          pygame.display.update()
          for entity in all_sprites:
                entity.kill() 
          time.sleep(2)
          pygame.quit()
          sys.exit()            

    #nu collide s tenge i + v zavisimosti ot randoma value  
    if pygame.sprite.collide_rect(P1, TG):
        TENGE += TG.value
        TG.respawn()
        #delenie bez ostatka i last tenge countit eti 5
        if TENGE // 5 > LAST_TENGE:
            SPEED += 1
            LAST_TENGE = TENGE // 5
    #nu dispay strok
    scores = font_small.render("Score: " + str(SCORE), True, BLACK)
    DISPLAYSURF.blit(scores, (10, 10))
    tenge = font_small.render("Tenge: " + str(TENGE), True, BLACK)
    DISPLAYSURF.blit(tenge, (SCREEN_WIDTH - 100, 10))
    

    pygame.display.update()
    FramePerSec.tick(FPS)