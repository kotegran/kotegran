from pygame import *

init()

win_width=500
win_height=500
FPS=60
clock=time.Clock()
exit=False

# CREATING CANVAS

bg = image.load("bg.png")
bg = transform.scale(bg, (win_width, win_height))

window = display.set_mode((win_width, win_height))
# TITLE OF CANVAS
display.set_caption("ping-pong")
exit = False

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, wight, height):
        super().__init__()
        self.image=transform.scale(image.load(player_image), (wight, height))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x= player_x
        self.rect.y= player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_l(self,):
        keys = key.get_pressed()
        if keys[K_W] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_S] and self.rect.y < 500:
            self.rect.y += self.speed
    def update_r(self,):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 500:
            self.rect.y += self.speed

class Ball(GameSprite):
    def update(self, speed_x, speed_y):
        self.rect.x += speed_x
        self.rect.y += speed_y

player_r=Player("bg.png",0,100, 10, 80, 80)
player_l=Player("bg.png",win_width - 80, 100, 10, 80, 80)
ball = Ball("bg.png", 100, 100, 5, 50, 50)
speed_x=5
speed_y=5
finish=False

font = font.Font(None, 35)
lose=1

while exit != True:
    for e in event.get():
        if e.type == QUIT:
            exit = True
    window.blit(bg, (0, 0))
    if finish != True:
        if sprite.collide_rect(player_1,ball) or sprite.collide_rect(player_r,ball):
            speed_x *= -1
        if ball.rect.y > win_height - 80 or ball.rect.y < 0:
            speed.y *= -1
        if ball.rect.y < 0:
            lose=font.render("Plater 1 lose", True, (180, 0, 0))
            finish=True
        if ball.rect.y > win_width:
            lose=font.render("Plater 2 lose", True, (180, 0, 0))
            finish=True
        ball.update(speed_x,speed_y)
        player_l.update_l()
        plater_r.update_r()
    else:
        window.blit(lose, (250, 250))
        player_l.reset()
        plater_r.reset()
        ball.reset()
        display.update()
        clock.tick(FPS)