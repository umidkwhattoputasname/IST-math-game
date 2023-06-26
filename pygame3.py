import os
import pygame
from pygame.locals import *
pygame.init()
os.system('clear')

X = 1000
Y = 564
width,height = 1000,564
window = pygame.display.set_mode((width,height))            #screen/display size
pygame.display.set_caption('Tamathgotchi Game')           #setting name of pygame window

bg_img = pygame.image.load('yr10/Images/background.jpg')    #image ref 
bg_img = pygame.transform.scale(bg_img,(width,height))      #sizing image

white = (255,255,255)
black = (50,50,50)
test = (92,77,74)
font = pygame.font.Font('yr10/Style/minecraft_font.ttf',60)  #font, size
text = font.render('Tamathgotchi Game', True, test)  #text, smth, text colour, box colour
textRect = text.get_rect()
textRect.center = (X//2,Y//4)

width_sprite,height_sprite = 210,300
postion_sprite = 20,264
normal = pygame.image.load('yr10/Images/Tamagotchi.png')        #normal 
normal = pygame.transform.scale(normal,(width_sprite,height_sprite))
happy = pygame.image.load('yr10/Images/Tamagotchihappy.png')    #happy
happy = pygame.transform.scale(happy,(width_sprite,height_sprite))
dying = pygame.image.load('yr10/Images/Tamagotchihurt.png')     #dying 
dying = pygame.transform.scale(dying,(width_sprite,height_sprite))
dead = pygame.image.load('yr10/Images/Tamagotchided.png')       #dead 
dead = pygame.transform.scale(dead,(width_sprite,height_sprite))

click = pygame.mouse.get_pressed()

running = True 
life = 3                         

def end():
    global running
    if event.type == QUIT:
        running = False

while running:
    window.fill(white)
    window.blit(bg_img,(0,0))           #background image
    window.blit(text, textRect)         #Text/title

    for event in pygame.event.get():  
        if event.type == MOUSEBUTTONUP:
            while life > 0 and running:
                for event in pygame.event.get():
                    window.blit(normal,(postion_sprite))  
                    pygame.display.update()
                    if event.type == QUIT:
                        running = False
            
        end()            
    pygame.display.update()
             
pygame.quit()


