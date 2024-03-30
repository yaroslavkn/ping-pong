from pygame import *
from random import randint

font.init()
font_text = font.Font(None, 36)

WIDTH = 600
HEIGHT = 500
FPS = 60
WIN_SCORE = 10
RESTERT_TIME = 3000

def generate_color():
    return (randint(0, 255), randint(0, 255), randint(0, 255))

background = generate_color()
window = display.set_mode((WIDTH, HEIGHT))
display.set_caption("PING-PONG")
clock = time.Clock()

class GameSprite(sprite.Sprite):
    def __init__(self, img, x, y, w, h, speed):
        super().__init__()
        self.image = transdorm.scale(image.load(img), (w, h))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect,y))

color_selection = False
run = True
finish = False

while run:
    for e in event.get():
        if e.type == QUIT:
            run = False
        elif e.type == KEYDOWN:
            if e.key == K_SPACE:
                color_selection = True
        elif e.type == KEYUP:
            if e.key == K_SPACE:
                color_selection = False

    if not finish:
        if color_selection:
            background = generate_color()
        window.fill(background)
    else:
        pass


    display.update()
    clock.tick(FPS)