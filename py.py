import pygame
import sys

# 망함 이거 


def init():
    pygame.init()

    screen_width, screen_height = 800, 600
    screen = pygame.display.set_mode((screen_width, screen_height))

    paddle = screen_width / 2 
    ball = [screen_width / 2, screen_height / 2]
    ball_speed = [2, 2]
    
    score = 0
    life = 1

    bricks = []
    brick_width, brick_height = 60, 20 
    for i in range(10):  
        for j in range(4): 
            brick_x = i * (brick_width + 10)  
            brick_y = j * (brick_height + 10) + 50  
            brick_rect = pygame.Rect(brick_x, brick_y, brick_width, brick_height)  
            brick_color = (255, 255, 255) 
            bricks.append({'rect': brick_rect, 'color': brick_color})

    game_state = {
        "screen": screen,
        "paddle": paddle,
        "ball": ball,
        "ball_speed": ball_speed,
        "score": score,
        "lives": life,
        "bricks": bricks,

    }

    return game_state

def update_screen(game_state):
    screen = game_state['screen']

    screen.fill((0,0,0))

    draw_ball_and_paddle(game_state)
    draw_bricks(game_state)

    pygame.display.flip()


def keybord_event(game_state):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                game_state['paddle'] -= 15
            elif event.key == pygame.K_RIGHT:
                game_state['paddle'] += 15
            
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                pass 

def draw_bricks(game_state):
    screen = game_state['screen']
    bricks = game_state['bricks']

    for brick in bricks:
        pygame.draw.rect(screen, brick['color'], brick['rect'])
    
def draw_ball_and_paddle(game_state):
    screen = game_state['screen']
    ball = game_state['ball']
    paddle = game_state['paddle']

    paddle_width, paddle_height = 100, 10  
    paddle_rect = pygame.Rect(paddle, screen.get_height() - paddle_height, paddle_width, paddle_height)
    pygame.draw.rect(screen, (255, 255, 255), paddle_rect)  

    ball_radius = 10  
    pygame.draw.circle(screen, (255, 255, 255), ball, ball_radius) 

def crash(game_state):
    ball = game_state['ball']
    ball_speed = game_state['ball_speed']
    paddle = game_state['paddle']
    bricks = game_state['bricks']
    
    if paddle <= ball[0] <= paddle + 100 and game_state['screen'].get_height() - 10 <= ball[1] <= game_state['screen'].get_height():
        ball_speed[1] = -ball_speed[1]  

    for brick in bricks:
        if brick['rect'].colliderect(pygame.Rect(ball[0] - 10, ball[1] - 10, 20, 20)):  
            bricks.remove(brick) 
            ball_speed[1] = -ball_speed[1]  
            game_state['score'] += 1
            break 

def main():
    game_state = init()
    
    clock = pygame.time.Clock()
    
    while True:
        keybord_event(game_state)
        game_state['ball'][0] += game_state['ball_speed'][0]
        game_state['ball'][1] += game_state['ball_speed'][1]
        crash(game_state)
        update_screen(game_state)
        clock.tick(60)  # 60 FPS

if __name__ == "__main__":
    main()
