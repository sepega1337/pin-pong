from pygame import *

init()
display.set_mode((700, 500))
fps = time.Clock()
window = display.set_mode((700,500))
window.fill((200,20,100))
bg = transform.scale(image.load('5D__3254.jpg'),(700,500))

class Rocket():
    def __init__(self, img, x, y, width_rocket, hight_rocket, speed):
        self.image = transform.scale(image.load(img), (width_rocket, hight_rocket))
        self.image_hit = self.image.get_rect()
        self.image_hit.x = x
        self.image_hit.y = y
        self.speed = speed

    def show_s(self):
        window.blit(self.image, (self.image_hit.x, self.image_hit.y))

class Rocket_player2(Rocket):
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] :
            self.image_hit.y -= self.speed
        if keys[K_DOWN] :
            self.image_hit.y += self.speed

class Rocket_player1(Rocket):
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_w] :
            self.image_hit.y -= self.speed
        if keys[K_s] :
            self.image_hit.y += self.speed

        

rocket1 = Rocket_player1('безымянный.png', 30, 200, 25, 250, 6)
rocket2 = Rocket_player2('безымянный.png', 650, 200, 25, 250, 6)
ball = Rocket('image-removebg-preview.png', 200, 200, 50, 50, 7)




fps = time.Clock()

run = True
speed_x = 3
speed_y = 3
while run:
    for i in event.get():
        if i.type == QUIT:
            run = False
    

    if sprite.collide_rect(rocket1, ball) or sprite.collide_rect(rocket2, ball):
        speed_x *= -1
        speed_y *= -1

    if ball.image_hit.y < 10:
        speed_y *= -1
    
    if ball.image_hit.y > 470:
        speed_y *= -1




    window.blit(bg,(0, 0))

    ball.image_hit.x += speed_x
    ball.image_hit.y += speed_y


    rocket1.show_s( )
    rocket1.update_r()
    rocket2.show_s( )
    rocket2.update_r()
    ball.show_s()
    display.update()
    fps.tick(60)
