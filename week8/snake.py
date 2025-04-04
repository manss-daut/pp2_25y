import pygame, sys, random

pygame.init()

WIDTH, HEIGHT = 600, 400
CELL_SIZE = 20
GRID_WIDTH = WIDTH // CELL_SIZE
GRID_HEIGHT = HEIGHT // CELL_SIZE

WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED   = (255, 0, 0)
BLACK = (0, 0, 0)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake")
#nu pointy, lvl i skok nado food na next lvl
score = 0
level = 1
level_goal = 5
font = pygame.font.SysFont("Verdana", 20)


#Nu steny, tochnee koordinaty sten
walls = [(0, y) for y in range(GRID_HEIGHT)] + \
        [(GRID_WIDTH-1, y) for y in range(GRID_HEIGHT)] + \
        [(x, 0) for x in range(GRID_WIDTH)] + \
        [(x, GRID_HEIGHT-1) for x in range(GRID_WIDTH)]


#Nu class zmei
class Snake:
    def __init__(self):
        self.body = [(5, 5)] #nachal'naya pos
        self.direction = (1, 0)  #dvizhenie vpravo

    def move(self):
        head = self.body[-1] #golova
        new_head = (head[0] + self.direction[0], head[1] + self.direction[1]) #new golova na next pos
        self.body.append(new_head)
        self.body.pop(0)  #udalyaem proshluyu golovu

    def grow(self):
        self.body.insert(0, self.body[0])  #copy hvost

    def draw(self):
        for segment in self.body:
            pygame.draw.rect(screen, GREEN, (segment[0]*CELL_SIZE, segment[1]*CELL_SIZE, CELL_SIZE, CELL_SIZE)) #risuem zmeyu na pixel no kletka

#Generator of food
def random_food_position(snake):
    while True:
        pos = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1)) #random na pole
        if pos not in snake.body and pos not in walls: #ne v tele ne d stene
            return pos

snake = Snake()
food = random_food_position(snake)

font = pygame.font.SysFont("Verdana", 20)

#Dlya skorosti
clock = pygame.time.Clock()
speed = 10

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    #move by strelki i esli v pravo to nel'zya v levo i td
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and snake.direction != (0, 1):
        snake.direction = (0, -1)
    if keys[pygame.K_DOWN] and snake.direction != (0, -1):
        snake.direction = (0, 1)
    if keys[pygame.K_LEFT] and snake.direction != (1, 0):
        snake.direction = (-1, 0)
    if keys[pygame.K_RIGHT] and snake.direction != (-1, 0):
        snake.direction = (1, 0)

    snake.move()
    #nu vrezaniye v stenu x<0 levo, width pravo
    head_x, head_y = snake.body[-1]
    if head_x < 0 or head_x >= GRID_WIDTH or head_y < 0 or head_y >= GRID_HEIGHT:
        pygame.quit()
        sys.exit()

    #nu grow esli natykaetsya na food
    if snake.body[-1] == food:
        snake.grow()
        score += 1
        food = random_food_position(snake)
        #esli score 5 to + k skorosti i lvl
        if score % level_goal == 0:
            level += 1
            speed += 1

    #risuem zmeyu i food krasnuyu na pixel no na kletke
    screen.fill(BLACK)
    snake.draw()
    pygame.draw.rect(screen, RED, (food[0]*CELL_SIZE, food[1]*CELL_SIZE, CELL_SIZE, CELL_SIZE))
    #dlya scora
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))
    #dlya lvla
    level_text = font.render(f"Level: {level}", True, WHITE)
    screen.blit(level_text, (WIDTH - 100, 10))
    #walls narisovany
    pygame.draw.rect(screen, (100, 100, 100), (0, 0, WIDTH, HEIGHT), 4)

    pygame.display.flip()
    clock.tick(speed)