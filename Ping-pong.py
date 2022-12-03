from pygame import *

window = display.set_mode((700, 500))

ball = image.load("ball.png")
ball = transform.scale(ball, (30, 30))

clock = time.Clock()
game = True
ball_x = 50
ball_y = 50
while game:
    clock.tick(60)

    for e in event.get():
        if e.type == QUIT:
            game = False

#правила
    ball_x += 3
    ball_y += 3

#отрисовка
    window.fill((15, 50, 50))
    window.blit(ball, (ball_x, ball_y))
    display.update()