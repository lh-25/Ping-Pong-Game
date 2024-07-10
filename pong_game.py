from pygame import *
init()
font.init()

FPS = 60
WIDTH = 800
HEIGHT = 600
BALL_SIZE = 50
PADDLE_WIDTH = 10
PADDLE_HEIGHT = 100

WHITE = (255,255,255)
BLACK = (0,0,0)

ball_pos = [WIDTH / 2, HEIGHT / 2]
ball_vel = [7,7]

paddle1_pos = [PADDLE_WIDTH, HEIGHT / 2 - PADDLE_HEIGHT / 2]
paddle2_pos = [WIDTH - 2 * PADDLE_WIDTH, HEIGHT / 2 - PADDLE_HEIGHT / 2]
paddle_speed = 6

score1 = 0
score2 = 0

font = font.SysFont(None, 74)
screen = display.set_mode((WIDTH,HEIGHT))
display.set_caption("Pong Game")
clock = time.Clock()

def draw_paddle(position):
    draw.rect(screen,WHITE,Rect(position[0],position[1],PADDLE_WIDTH, PADDLE_HEIGHT))
    
def draw_ball(position): 
    draw.circle(screen,WHITE,position, BALL_SIZE / 5)
    
    
def draw_scores(score1, score2):
    score1_text = font.render(str(score1), True, WHITE)
    score2_text = font.render(str(score2), True, WHITE)
    screen.blit(score1_text, (WIDTH / 4,20))
    screen.blit(score2_text, (3 * WIDTH / 4,20))

def update_ball():
    global ball_pos, ball_vel, score1, score2
    
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]
    
    if ball_pos[1] <= BALL_SIZE / 2 or ball_pos[1] >= HEIGHT - BALL_SIZE / 2:
        ball_vel[1] = -ball_vel[1]
        
    if (ball_pos[0] <= PADDLE_WIDTH + BALL_SIZE / 2 and paddle1_pos[1] < ball_pos[1] < paddle1_pos[1] + PADDLE_HEIGHT) or  (ball_pos[0] >= WIDTH - PADDLE_WIDTH - BALL_SIZE / 2 and paddle2_pos[1] < ball_pos[1]< paddle2_pos[1] + PADDLE_HEIGHT):
        ball_vel[0] = -ball_vel[0]
        
    if ball_pos[0] <= BALL_SIZE / 2:
        score2 += 1
        reset_ball()
    elif ball_pos[0] >= WIDTH - BALL_SIZE / 2:
        score1 += 1
        reset_ball()
        
def reset_ball():
    global ball_pos, ball_vel
    ball_pos = [WIDTH / 2, HEIGHT / 2]
    ball_vel = [4,4]

run = True
while run:
    for e in event.get():
        if e.type == QUIT:
            quit()
            run = False
            
    keys = key.get_pressed()
    if keys[K_w] and paddle1_pos[1] > 0:
        paddle1_pos[1] -= paddle_speed
    if keys[K_s] and paddle1_pos[1] < HEIGHT - PADDLE_HEIGHT:
        paddle1_pos[1] += paddle_speed
        
    if keys[K_UP] and paddle2_pos[1] > 0:
        paddle2_pos[1] -= paddle_speed
    if keys[K_DOWN] and paddle2_pos[1] < HEIGHT - PADDLE_HEIGHT:
        paddle2_pos[1] += paddle_speed
    
    update_ball()
    screen.fill(BLACK)
    draw_paddle(paddle1_pos)
    draw_paddle(paddle2_pos)
    draw_ball(ball_pos)
    draw_scores(score1,score2)
    display.flip()
    display.update()
    clock.tick(FPS)