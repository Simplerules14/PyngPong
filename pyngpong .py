from pygame import *
from random import randint
win_width = 800
win_height = 500
window = display.set_mode((win_width,win_height))
display.set_caption("PyngPong")

FPS = 60
clock = time.Clock()
game = True

class GameSprite(sprite.Sprite):
    def __init__ (self, imagge,x,y,size_x,size_y,speed):
        super().__init__()
        self.image = transform.scale(image.load(imagge),(size_x,size_y))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.size_x = size_x
        self.size_y = size_y
        self.rect.x = x
        self.rect.y = y
    def redraw(self):
        window.blit(self.image,(self.rect.x,self.rect.y))

class Ball(GameSprite):
    def update(self):
        self.rect.x += self.speed

ball = Ball("Ball.png",300,300,50,50,10)

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

        ball.update()
        ball.redraw()

        display.update()
    clock.tick(FPS)