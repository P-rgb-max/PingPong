from paddle import Paddle
from ball import Ball
import pygame

pygame.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
ORANGE = (255, 165, 0)

size = (700, 500)
scr = pygame.display.set_mode(size)
pygame.display.set_caption('Ping Pong Gameplay')

# Left
paddleA = Paddle(BLUE, 10, 100)
paddleA.rect.x = 20
paddleA.rect.y = 200
# Right
paddleB = Paddle(GREEN, 10, 100)
paddleB.rect.x = 670
paddleB.rect.y = 200

ball = Ball(RED, 10, 10)
ball.rect.x = 345
ball.rect.y = 195

all_sprites_list = pygame.sprite.Group()
all_sprites_list.add(paddleA)
all_sprites_list.add(paddleB)
all_sprites_list.add(ball)

run = True
pause = False

clock = pygame.time.Clock()

scoreA = 0
scoreB = 0

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_x:
                run = False
            elif event.key == pygame.K_SPACE:
                pause = not pause

    if pause:
        continue

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        paddleA.moveUp(5)
    if keys[pygame.K_s]:
        paddleA.moveDown(5)
    if keys[pygame.K_UP]:
        paddleB.moveUp(5)
    if keys[pygame.K_DOWN]:
        paddleB.moveDown(5)

    all_sprites_list.update()

    if ball.rect.x >= 690:
        scoreA += 1
        ball.velocity[0] = -ball.velocity[0]
    if ball.rect.x <= 0:
        scoreB += 1
        ball.velocity[0] = -ball.velocity[0]
    if ball.rect.y > 490:
        ball.velocity[1] = -ball.velocity[1]
    if ball.rect.y < 0:
        ball.velocity[1] = -ball.velocity[1]

    if pygame.sprite.collide_mask(ball, paddleA) or pygame.sprite.collide_mask(ball, paddleB):
        ball.bounce()

    scr.fill(ORANGE)
    pygame.draw.line(scr, WHITE, (349, 0), (349, 500), 5)
    all_sprites_list.draw(scr)
    font = pygame.font.Font(None, 74)
    text = font.render(str(scoreA), 1, WHITE)
    scr.blit(text, (250, 10))
    text = font.render(str(scoreB), 1, WHITE)
    scr.blit(text, (420, 10))
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
