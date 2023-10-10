from pygame import *

window = display.set_mode((1000,700))
display.set_caption('понг пиг')
fon = transform.scale(image.load('pawel-kot-mk2-hd-armory3.jpg'),(1000,700))



font.init()
font = font.Font(None,35)

class Game_Sprite(sprite.Sprite):
    def __init__(self,player_image , player_x, player_y , size_x , size_y , player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(size_x , size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))
class Player(Game_Sprite):
    def update1(self):
        knopky = key.get_pressed()
        if knopky[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
        if knopky[K_s] and self.rect.y < 920:
            self.rect.y += self.speed
    def update2(self):
        knopky = key.get_pressed()
        if knopky[K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed
        if knopky[K_DOWN] and self.rect.y < 920:
            self.rect.y += self.speed
   

game = True
finish = False
clock = time.Clock()
Player1 = Player ('kisspng-sub-zero-scorpion-mortal-kombat-shaolin-monks-5b0d2bb990b0d1.6488181215275898175927 (2).png', 80,200,100,100,20)
Player2 = Player('png-transparent-mortal-kombat-deception-mortal-kombat-armageddon-scorpion-mortal-kombat-mythologies-sub-zero-mortal-kombat-x-scorpion-insects-fictional-character-mortal-kombat (2).png',800,200,100,100,20)
ball = Player('28282181_transparent-mario-fireball-png-deadpool-logo-pixel-art.png',200,200,40,50,0)
lose_1 = font.render('Scorpion Wins',True,(255,255,255))
lose_2 = font.render('Sub-Zero Wins',True,(255,255,255))
ball_x = 20
ball_y = 20


while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    if not finish:
        window.blit(fon,(0,0))
        Player1.reset()
        Player1.update1()
        Player2.reset()
        Player2.update2()
        ball.reset()
        ball.rect.x += ball_x
        ball.rect.y += ball_y
        if sprite.collide_rect(Player1,ball) or sprite.collide_rect(Player2, ball):
            ball_x *= -1
            ball_y *= 1
        if ball.rect.y < 0 or ball.rect.y >630:
            ball_y *= -1
        if ball.rect.x <-40:
            finish = True
            window.blit(lose_1,(400,200))
        if ball.rect.x > 1000:
            finish = True
            window.blit(lose_2,(400,200))
        
        display.update()
    time.delay(60)