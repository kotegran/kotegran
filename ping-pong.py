import pygame

# CREATING CANVAS
window = pygame.display.set_mode((500, 700))

# TITLE OF CANVAS
pygame.display.set_caption("ping-pong")
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
        keys = pygame.key.get_pressed()
        if keys[pygame.K_W] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[pygame.K_S] and self.rect.y < 700:
            self.rect.y += self.speed
    def update_r(self,):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN] and self.rect.y < 700:
            self.rect.y += self.speed

while not exit:

    canvas.blit(bg, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = True
    pygame.display.update()