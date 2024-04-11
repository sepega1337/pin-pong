from pygame import *
init()
display.set_mode((700, 500))
fps = time.Clock()
window = display.set_mode((700,500))
window.fill((200,20,100))
bg = transform.scale(image.load('5D__3254.jpg'),(700,500))

sprite1 = transform.scale(image.load('безымянный.png'),(20,200))
hitbox_sprit1 = sprite1.get_rect()
hitbox_sprit1.x = 0
hitbox_sprit1.x = 650

sprite2 = transform.scale(image.load('безымянный.png'),(20,200))
hitbox_sprit2 = sprite2.get_rect()
hitbox_sprit2.x = 0
hitbox_sprit2.x = 50

run = True

while run:
    for i in event.get():
        if i.type == QUIT:
            run = False
        if i.type == KEYDOWN:
            if i.key == K_w:
                hitbox_sprit1.y -= 20
            if i.key == K_s:
                hitbox_sprit1.y += 20

#спрайт 2:
            if i.key == K_DOWN:
                hitbox_sprit2.y += 20
            if i.key == K_UP:
                hitbox_sprit2.y -= 20


            





    window.blit(bg,(0, 0))
    window.blit(sprite1,hitbox_sprit1)
    window.blit(sprite2,hitbox_sprit2)
    display.update()
    fps.tick(60)
