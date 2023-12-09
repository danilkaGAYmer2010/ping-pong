from pygame import *
window  = display.set_mode((700,500))
display.set_caption("ПеПонг")
back = transform.scale(image.load("back.jpg"),(700,500))

mixer.init()
mixer.music.load('kaef.mp3')
mixer.music.set_volume(0.3)
mixer.music.play(-1)
font.init()
game = True
finish = False
dx = 3
dy = 3
text = font.Font(None,35)
lose = text.render('первый игрок лох',True,(150,0,0))
text1 = font.Font(None,35)
lose1 = text1.render('второй игрок лох',True,(150,0,0))
class GameSprite(sprite.Sprite):
    def __init__(self,player_image,speed,x,y,size_x,size_y):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(size_x,size_y))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):    
    def update_1(self):       
        keys = key.get_pressed()
        if  keys[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
        if  keys[K_s] and self.rect.y < 300:
              self.rect.y += self.speed
class Player1(GameSprite):    
    def update_2(self):       
        keys = key.get_pressed()
        if  keys[K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed
        if  keys[K_DOWN] and self.rect.y < 300:
              self.rect.y += self.speed

class Ball(GameSprite):
    def update_3(self):
        pass

player = Player("platform1.jpg",5,50,20,50,200)
player1 = Player1("platform1.jpg",5,600,20,50,200)
ball=Ball("ball.jpg",3,285,225,75,75)




while game:  
    for e in event.get():
        if e.type == QUIT:
            game = False
    if not finish:
        window.blit(back,(0,0))
        player.reset()
        player.update_1()
        player1.reset()
        player1.update_2()
        ball.update_3()
        ball.reset()
        ball.rect.x += dx
        ball.rect.y += dy
        if ball.rect.x < 0:
            finish = True
            window.blit(lose,(200,200))
        if ball.rect.x > 700:
            finish = True
            window.blit(lose1,(200,200))
        if  ball.rect.y < 0 or ball.rect.y > 425 :
            dy *= -1
        if sprite.collide_rect(player,ball) or sprite.collide_rect(player1,ball):
            dx*=-1
        
        
    display.update()
    time.delay(30)
display.update()    