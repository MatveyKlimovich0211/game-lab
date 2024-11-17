#подключение
import pygame
pygame.init()
pygame.mixer.init()
pygame.mixer.music.load('jungles.ogg')
pygame.mixer.music.play()


Windows = pygame.display.set_mode((700,500))

#pygame.display.set_caption('Гонка')

FPS = pygame.time.Clock()
    
fon = pygame.image.load("background.jpg")
fon = pygame.transform.scale(fon,(700,500))
class gameObjekt(pygame.sprite.Sprite):
    def __init__(self, image, visota, shirina, x,y, speed):
        super().__init__()
        self.img_sprite = pygame.image.load(image)
        self.img_sprite = pygame.transform.scale(self.img_sprite,(visota,shirina))
        self.hitbox = self.img_sprite.get_rect()
        self.hitbox.x = x
        self.hitbox.y = y 
        self.speed = speed
        self.move = ''
    def show(self):
        Windows.blit(self.img_sprite, self.hitbox)

class  gamePlaer(gameObjekt): 
    def ypravlenie(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]  and self.hitbox.y > 0:
            self.hitbox.y -= self.speed
        if keys[pygame.K_s]  and self.hitbox.y < 450:
            self.hitbox.y += self.speed
        if keys[pygame.K_d]  and self.hitbox.x < 650:
            self.hitbox.x += self.speed
        if keys[pygame.K_a]  and self.hitbox.x > 0 :
            self.hitbox.x -= self.speed

class Wall(pygame.sprite.Sprite):   
        def __init__(self, wall_visota, wall_shirina, wall_x,wall_y, wall_r, wall_g, wall_b  ):  
            super().__init__() 
            self.wall_shirina =  wall_shirina
            self.wall_visota = wall_visota
            self.wall_r = wall_r
            self.wall_g = wall_g
            self.wall_b = wall_b
            self.wall_image = pygame.Surface((self.wall_shirina, self.wall_visota))
            self.wall_image.fill((self.wall_r,self.wall_g,self.wall_b))

            self.wall_hitbox = self.wall_image.get_rect()
            self.wall_hitbox.x = wall_x
            self.wall_hitbox.y = wall_y
        def show(self):
            Windows.blit(self.wall_image, self.wall_hitbox)

class Enemy(gameObjekt):
    def forward(self):
        if self.hitbox.x <= 450:
            self.move = 'pravo'
        if self.hitbox.x >= 600:
            self.move = 'levo'

        if self.move == 'levo':
            self.hitbox.x -= self.speed

        else: 
            self.hitbox.x += self.speed



player = gamePlaer('hero.png',60,60, 20, 50,3)
cyborg = Enemy('cyborg.png',60,60, 300, 50, 2)
money = gameObjekt('treasure.png',60,60, 400, 90, 0)
w1 = Wall(200, 10, 200, 20, 10,13,120)
w2 = Wall(800, 10, 100, 600, 10,13,120)
w3 = Wall(10, 600, 50, 450, 10,13,120)
w4 = Wall(10, 200, 90, 20, 10,13,120)
w5 = Wall(300, 10, 300, 50, 10,13,120)
w6 = Wall(10, 100, 500, 70, 10,13,120)

run = True
         
while run:
    for i in pygame.event.get():
         if i.type == pygame.QUIT:
             run = False
    Windows.blit(fon,(0,0))
    player.show()
    player.ypravlenie()
    cyborg.show()
    cyborg.forward()
    money.show()
    w1.show()
    w2.show()
    w3.show()
    w4.show()
    w5.show()
    w6.show()
    if player.hitbox.colliderect(w1.wall_hitbox) or player.hitbox.colliderect(w2.wall_hitbox) or player.hitbox.colliderect(w3.wall_hitbox) or player.hitbox.colliderect(w4.wall_hitbox) or player.hitbox.colliderect(w5.wall_hitbox) or player.hitbox.colliderect(w6.wall_hitbox):
        run = False 
    if player.hitbox.colliderect(cyborg.hitbox):
        run = False 

    pygame.display.update()
    FPS.tick(100)
                                                                                                                                                                                                                                                                                                                                                                            
    








































#параметры экрана
pygame.init()
shirina = 800
vusota = 500
#создание окна
Windows = pygame.display.set_mode((shirina,vusota))
pygame.display.set_caption('Гонка')
#создание дороги
background_image = pygame.image.load("1687798045_bogatyr-club-p-doroga-sverkhu-foni-vkontakte-1.png")
background_image = pygame.transform.scale(background_image, (shirina,vusota))

FPS = pygame.time.Clock()
#создание машины
car = pygame.image.load('png-transparent-sports-car-bird-s-eye-view-race-car-car-color-vehicle.png')
car = pygame.transform.scale(car, (70,100))
car_hit_box = car.get_rect()

car_hit_box.centerx = shirina // 2
car_hit_box.bottom = vusota - 30
car_speed = 10
#СОЗДАНИЕ СКАЛ
obstacle_width = 100
obstacle_height = 20
obstacle_x = random.randint(0, vusota - obstacle_width)
obstacle_y = 0
obstacle_speed = 5
obstacle = pygame.image.load('скала джонсон.jpg')


#обьекты
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and car_hit_box.x > 5: 
        car_hit_box.x -= car_speed
    if keys[pygame.K_RIGHT] and car_hit_box.x < 720: 
        car_hit_box.x += car_speed
    obstacle_y += obstacle_speed
    if obstacle_y > vusota:
        obstacle_x = random.randint(0, vusota - obstacle_width)
        obstacle_y = 0
    if car_hit_box.colliderect((obstacle_x, obstacle_y, obstacle_width, obstacle_height)):
        run = False


    Windows.blit(background_image,(0, 0))
    Windows.blit(car, car_hit_box)

    pygame.draw.rect(Windows,(255,0,0),(obstacle_x,obstacle_y,obstacle_width,obstacle_height))



    pygame.display.update()
    FPS.tick(100)
     














     from pygame import *
import pygame
import random
pygame.init()
pygame.mixer.init()
pygame.mixer.music.load('space.ogg')
pygame.mixer.music.play()
pygame.font

Windows = pygame.display.set_mode((700,500))

#pygame.display.set_caption('Гонка')

FPS = pygame.time.Clock()
    
fon = pygame.image.load("galaxy.jpg")
fon = pygame.transform.scale(fon,(700,500))
class gameObjekt(pygame.sprite.Sprite):
    def __init__(self, image, visota, shirina, x,y, speed):
        super().__init__()
        self.img_sprite = pygame.image.load(image)
        self.img_sprite = pygame.transform.scale(self.img_sprite,(visota,shirina))
        self.rect = self.img_sprite.get_rect()
        self.rect.x = x
        self.rect.y = y 
        self.speed = speed
        self.move = ''
    def show(self):
        Windows.blit(self.img_sprite, self.rect)

class  gamePlaer(gameObjekt): 
    def ypravlenie(self):
        keys = pygame.key.get_pressed()
        
            
        if keys[pygame.K_d]  and self.rect.x < 650:
            self.rect.x += self.speed
        if keys[pygame.K_a]  and self.rect.x > 0 :
            self.rect.x -= self.speed
    def vistril(self):
        fire = Fire("bullet.png", 15, 20, self.rect.x, self.rect.y, 10)   
        fires.add(fire) 
    
class Enemy(gameObjekt):
    def forward(self):
        global miss
        self.rect.y += 2
        if self.rect.y > 400:
           miss += 1
           self.rect.y = -20
           self.rect.x = random.randint(50, 650)
           
                                         
                 

miss = 0


class Fire (gameObjekt):
    def update(self):
        self.rect.y -= self.speed
        if self.rect.y < 0:
            self.kill()
     
           
        
score = 0

player = gamePlaer('rocket.png',60,60, 20, 420,3)

money = gameObjekt('bullet.png',60,60, 400, 90, 0)
 
fires = sprite.Group()
        
run = True
monstrers = pygame.sprite.Group()
for i in range(5):
    monstrer = Enemy('ufo.png', 60, 60, random.randint(80, 1120), -100, 1)  
    monstrers.add(monstrer)      
while run:
    Windows.blit(fon,(0,0))   
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            run = False
        elif i.type == KEYDOWN:
            if i.key == K_SPACE:
                player.vistril()
    kill = pygame.sprite.groupcollide(fires, monstrers , True, True)
    for i in kill:
        score += 1
        monstrer = Enemy('ufo.png', 60, 60, random.randint(80, 1120), -100, 1)  
        monstrers.add(monstrer)   
    
    result = f'Вы уничтожили:{str(score)}'
    bed = font.Font(None, 35).render(result, True, (255,255, 250))

    Windows.blit(bed,(50,250))

    result1 = f'Лохов прошло в тыл:{str(miss)}'
    bed1 = font.Font(None, 35).render(result1, True, (255,255, 250))

    Windows.blit(bed1,(50,10))
    
    player.show()
    player.ypravlenie()
    for i in fires:
        i.show()
        i.update()
    
    if miss > 10:
        run = False


    for i in monstrers:
        i.show()
        i.forward()
        if player.rect.colliderect(i.rect):
            run = False

    pygame.display.update()
    FPS.tick(100)
