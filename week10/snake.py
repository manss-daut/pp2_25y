import pygame, sys, random, time
from connect import connect
from config import load_config

pygame.init()

#настройки экрана и клетки
WIDTH, HEIGHT = 600, 400
CELL_SIZE = 20
GRID_WIDTH = WIDTH // CELL_SIZE
GRID_HEIGHT = HEIGHT // CELL_SIZE

# цвета
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED   = (255, 0, 0)
BLACK = (0, 0, 0)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake")

#загружаю конфиг и спрашиваю имя
config = load_config()
username = input("enter your username: ")

#если пользователь новый — создаю, если уже есть — вытаскиваю уровень
def get_or_create_user(username):
    conn = connect(config)
    if conn:
        with conn:
            with conn.cursor() as cur:
                cur.execute("SELECT id, level FROM users WHERE username = %s", (username,))
                user = cur.fetchone()
                if user:
                    print(f"welcome back, {username}! your level: {user[1]}")
                    return user[0], user[1]
                else:
                    cur.execute("INSERT INTO users (username) VALUES (%s) RETURNING id, level", (username,))
                    new_user = cur.fetchone()
                    print(f"new user created: {username}")
                    return new_user[0], new_user[1]

#сохраняю очки и уровень в базу
def save_game_state(user_id, score, level):
    conn = connect(config)
    if conn:
        with conn:
            with conn.cursor() as cur:
                cur.execute("INSERT INTO user_scores (user_id, score, level) VALUES (%s, %s, %s)",
                            (user_id, score, level))
                print("game saved to database")

#получаю айди игрока и уровень
user_id, level = get_or_create_user(username)

# очки, цель уровня и шрифт
score = 0
level_goal = 5
font = pygame.font.SysFont("Verdana", 20)

#стены по краям
walls = [(0, y) for y in range(GRID_HEIGHT)] + \
        [(GRID_WIDTH-1, y) for y in range(GRID_HEIGHT)] + \
        [(x, 0) for x in range(GRID_WIDTH)] + \
        [(x, GRID_HEIGHT-1) for x in range(GRID_WIDTH)]

#класс змеи
class Snake:
    def __init__(self):
        self.body = [(5, 5)]
        self.direction = (1, 0)

    def move(self):
        head = self.body[-1]
        new_head = (head[0] + self.direction[0], head[1] + self.direction[1])
        self.body.append(new_head)
        self.body.pop(0)

    def grow(self):
        self.body.insert(0, self.body[0])

    def draw(self):
        for segment in self.body:
            pygame.draw.rect(screen, GREEN, (segment[0]*CELL_SIZE, segment[1]*CELL_SIZE, CELL_SIZE, CELL_SIZE))

#генерация еды вне змеи и стен
def random_food_position(snake):
    while True:
        pos = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))
        if pos not in snake.body and pos not in walls:
            weight = random.choice([1, 2, 3])
            created_at = time.time()
            return {'pos': pos, 'weight': weight, 'created_at': created_at}

snake = Snake()
foods = [random_food_position(snake)]
clock = pygame.time.Clock()
speed = 10

#основной цикл
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:  #сохраняю состояние игры
                save_game_state(user_id, score, level)

    #управление стрелками
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and snake.direction != (0, 1):
        snake.direction = (0, -1)
    if keys[pygame.K_DOWN] and snake.direction != (0, -1):
        snake.direction = (0, 1)
    if keys[pygame.K_LEFT] and snake.direction != (1, 0):
        snake.direction = (-1, 0)
    if keys[pygame.K_RIGHT] and snake.direction != (-1, 0):
        snake.direction = (1, 0)

    #двигаю змею
    snake.move()
    head_x, head_y = snake.body[-1]
    if head_x < 0 or head_x >= GRID_WIDTH or head_y < 0 or head_y >= GRID_HEIGHT:
        pygame.quit()
        sys.exit()

    #если съел еду
    for f in foods:
        if snake.body[-1] == f['pos']:
            snake.grow()
            score += f['weight']
            foods.remove(f)
            break

    #переход на новый уровень
    if score >= level * level_goal:
        level += 1
        speed += 1

    #если еды меньше 3 — добавляю
    if len(foods) < 3:
        foods.append(random_food_position(snake))

    #удаляю просроченную еду
    current_time = time.time()
    foods = [f for f in foods if current_time - f['created_at'] < 5]

    #отрисовка
    screen.fill(BLACK)
    snake.draw()
    for f in foods:
        pygame.draw.rect(screen, WHITE, (f['pos'][0]*CELL_SIZE, f['pos'][1]*CELL_SIZE, CELL_SIZE, CELL_SIZE))

    #очки и уровень
    score_text = font.render(f"score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))
    level_text = font.render(f"level: {level}", True, WHITE)
    screen.blit(level_text, (WIDTH - 100, 10))

    #граница поля
    pygame.draw.rect(screen, (100, 100, 100), (0, 0, WIDTH, HEIGHT), 4)

    pygame.display.flip()
    clock.tick(speed)