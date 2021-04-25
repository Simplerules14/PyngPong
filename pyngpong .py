from pygame import *
from random import randint
win_width = 800
win_height = 500
window = display.set_mode((win_width,win_height))
display.set_caption("PyngPong")

bg = transform.scale(image.load("background.jpg"),(win_width,win_height))

FPS = 60
clock = time.Clock()
game = True

class GameSprite(sprite.Sprite):
    def __init__ (self, imagge,x,y,size,speed,xsp,ysp):
        super().__init__()
        self.image = transform.scale(image.load(imagge),(size,size))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.size = size
        self.rect.x = x
        self.rect.y = y
        self.xsp = xsp
        self.ysp = ysp
    def redraw(self):
        window.blit(self.image,(self.rect.x,self.rect.y))
    
class Ball(GameSprite):
    def update(self):
        if self.rect.y > win_height - self.size:
            self.ysp = -1
        if self.rect.y < 0:
            self.ysp = 1
        if self.rect.x > win_width - self.size:
            self.xsp = -1
        if self.rect.x < 0 :
            self.xsp = 1
        self.rect.x += self.speed * self.xsp
        self.rect.y += self.speed * self.ysp

        

ball = Ball("Ball.png",300,300,50,2,1,1)

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    window.blit(bg,(0,0))

    ball.update()
    ball.redraw()

    display.update()
    clock.tick(FPS)
