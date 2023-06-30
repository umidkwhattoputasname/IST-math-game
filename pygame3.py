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

bg_img = pygame.image.load('Images/background.jpg')    #image ref 
bg_img = pygame.transform.scale(bg_img,(width,height))      #sizing image

white = (255,255,255)
black = (50,50,50)
test = (92,77,74)
font = pygame.font.Font('Style/minecraft_font.ttf',60)  #font, size
text = font.render('Tamathgotchi Game', True, test)  #text, smth, text colour, box colour
textRect = text.get_rect()
textRect.center = (X//2,Y//4)
startfont = pygame.font.Font('Style/minecraft_font.ttf',24)  #font, size
start = startfont.render('Click to start', True, test)  #text, smth, text colour, box colour
startRect = start.get_rect()
startRect.center = (X//2,Y//2)


width_sprite,height_sprite = 210,300
postion_sprite = 20,264
normal = pygame.image.load('Images/Tamagotchi.png')        #normal 
normal = pygame.transform.scale(normal,(width_sprite,height_sprite))
happy = pygame.image.load('Images/Tamagotchihappy.png')    #happy
happy = pygame.transform.scale(happy,(width_sprite,height_sprite))
dying = pygame.image.load('Images/Tamagotchihurt.png')     #dying 
dying = pygame.transform.scale(dying,(width_sprite,height_sprite))
dead = pygame.image.load('Images/Tamagotchided.png')       #dead 
dead = pygame.transform.scale(dead,(width_sprite,height_sprite))

life = 3
running = True

def end():
    global running
    if event.type == QUIT:
        running = False

page_no = 0
def infopages():
    infofont = pygame.font.Font('Style/minecraft_font.ttf',32)
    instructions = "You have 3 lives"
    info = infofont.render(instructions, True, test)
    infoRect = info.get_rect()
    infoRect.center = (X//2,Y//2)
    if page_no == 0:
        window.blit(text, textRect)         #Text/title
        window.blit(start,startRect)

    if page_no == 1 :
        window.blit(normal,postion_sprite)
        window.blit(info,infoRect)
    
    if page_no == 2:
        window.blit(dead,postion_sprite)
        instructions = "Get a question wrong, lose a life"
        info = infofont.render(instructions, True, test)
        infoRect = info.get_rect()
        infoRect.center = (X//2,Y//2)
        window.blit(info,infoRect)

    if page_no == 3:
        window.blit(dying,postion_sprite)
        instructions = "Click the right answer"
        info = infofont.render(instructions, True, test)
        infoRect = info.get_rect()
        infoRect.center = (X//2,Y//2)
        window.blit(info,infoRect)
    
    if page_no == 4:        
        window.blit(happy,postion_sprite)
        instructions = "Good luck and have fun!"
        info = infofont.render(instructions, True, test)
        infoRect = info.get_rect()
        infoRect.center = (X//2,Y//2)
        window.blit(info,infoRect)

def level1():
    level_font = pygame.font.Font('Style/minecraft_font.ttf',48)
    level_text = "Level 1"
    level = level_font.render(level_text, True, test)
    levelRect = level.get_rect()
    levelRect.center = (X//2,Y//2)
    if page_no == 5:
        window.blit(level,levelRect)


while running:
    window.blit(bg_img,(0,0))           #background image
    infopages()                             #change the page after first click
    level1()

    for event in pygame.event.get():  
        if page_no <= 4:                #stops page turning after instructions
            if event.type == MOUSEBUTTONUP: #if mouse clicked
                page_no = page_no + 1
        
        end()            
    pygame.display.update()
             
pygame.quit()
