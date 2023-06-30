import os
import pygame
from pygame.locals import *
import random
import time
pygame.init()
os.system('clear')

#window formatting
X = 1000
Y = 564
width,height = 1000,564
window = pygame.display.set_mode((width,height))            #screen/display size
pygame.display.set_caption('Tamathgotchi Game')           #setting name of pygame window

#background
bg_img = pygame.image.load('Images/background.jpg')    #image ref 
bg_img = pygame.transform.scale(bg_img,(width,height))      #sizing image

#Title page
white = (255,255,255)
black = (50,50,50)
test = (72,65,68)
font = pygame.font.Font('Style/minecraft_font.ttf',60)  #font, size
text = font.render('Tamathgotchi Game', True, test)  #text, smth, text colour, box colour
textRect = text.get_rect()
textRect.center = (X//2,Y//4)
startfont = pygame.font.Font('Style/minecraft_font.ttf',24)  #font, size
start = startfont.render('Click to start', True, test)  #text, smth, text colour, box colour
startRect = start.get_rect()
startRect.center = (X//2,Y//2)

#Sprites
width_sprite,height_sprite = 175,250
postion_sprite = 20,314
normal = pygame.image.load('Images/Tamagotchi.png')        #normal 
normal = pygame.transform.scale(normal,(width_sprite,height_sprite))
happy = pygame.image.load('Images/Tamagotchihappy.png')    #happy
happy = pygame.transform.scale(happy,(width_sprite,height_sprite))
dying = pygame.image.load('Images/Tamagotchihurt.png')     #dying 
dying = pygame.transform.scale(dying,(width_sprite,height_sprite))
dead = pygame.image.load('Images/Tamagotchided.png')       #dead 
dead = pygame.transform.scale(dead,(width_sprite,height_sprite))

#Questions
quizzes = "hi"
quiz_font = pygame.font.Font('Style/minecraft_font.ttf',21)
quiz = quiz_font.render(quizzes, True, test)  #text, smth, text colour, box colour
quizRect = quiz.get_rect()
position1 = (X//2,80)
position2 = (X//2,110)
position3 = (X//2,140)
position4 = (X//2,170)
quizRect.center = (position1)
answer_font = pygame.font.Font('Style/minecraft_font.ttf',20)

#Life
width_life,height_life = 45,35
postion_heart1 = 150,20
postion_heart2 = 195,20
postion_heart3 = 240,20
heart1 = pygame.image.load('Images/Heart.png')         
heart1 = pygame.transform.scale(heart1,(width_life,height_life))
heart2 = pygame.image.load('Images/Heart.png')         
heart2 = pygame.transform.scale(heart2,(width_life,height_life))
heart3 = pygame.image.load('Images/Heart.png')         
heart3 = pygame.transform.scale(heart3,(width_life,height_life))

page_no = 0
question = 1

life = 3
score = 0
running = True


def end():
    global running
    if event.type == QUIT:
        running = False

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
        instructions = "Click the right answer"
        info = infofont.render(instructions, True, test)
        infoRect = info.get_rect()
        infoRect.center = (X//2,Y//2-35)
        window.blit(info,infoRect)
        instructions = "Get a question wrong, lose a life"
        info = infofont.render(instructions, True, test)
        infoRect = info.get_rect()
        infoRect.center = (X//2,Y//2)
        window.blit(info,infoRect)

    if page_no == 3:
        window.blit(dying,postion_sprite)
        instructions = "Get 5 questions right to progress"
        info = infofont.render(instructions, True, test)
        infoRect = info.get_rect()
        infoRect.center = (X//2,Y//2-80)
        window.blit(info,infoRect)
        instructions = "to the next level"
        info = infofont.render(instructions, True, test)
        infoRect = info.get_rect()
        infoRect.center = (X//2,Y//2-50)
        window.blit(info,infoRect)
        instructions = "There are 3 levels"
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

    if page_no == 99:
        fail()

    if page_no == 13:
        complete()

def fail():
    font = pygame.font.Font('Style/minecraft_font.ttf',40)  #font, size
    text = font.render('Your pet died!', True, test)  #text, smth, text colour, box colour
    textRect = text.get_rect()
    textRect.center = (X//2,Y//4)

    pygame.draw.rect(window, test, pygame.Rect(150,220,200,50), 4,3) #screen, colour, position[x,y,width,height], fill/border, corners
    answer1 = answer_font.render ('Try Again', True, test)
    window.blit(answer1,(195,230))
    pygame.draw.rect(window, test, pygame.Rect(375,220,200,50), 4,3) #screen, colour, position[x,y,width,height], fill/border, corners
    answer2 = answer_font.render ('Main Menu', True, test)
    window.blit(answer2,(420,230))
    pygame.draw.rect(window, test, pygame.Rect(600,220,200,50), 4,3) #screen, colour, position[x,y,width,height], fill/border, corners
    answer3 = answer_font.render ('Quit', True, test)
    window.blit(answer3,(680,230))

    window.blit(text,textRect)
    sprite()
    if life == 0:
        if event.type == MOUSEBUTTONDOWN:
            mouse = pygame.mouse.get_pos()
            if 150 <= mouse[0] <= 350 and 200 <= mouse[1] <= 250:
                return True
            if 375 <= mouse[0] <= 575 and 200 <= mouse[1] <= 250:
                return False
            if 600 <= mouse[0] <= 800 and 200 <= mouse[1] <= 250:
                pygame.quit()

def complete():
    font = pygame.font.Font('Style/minecraft_font.ttf',40)  #font, size
    text = font.render('Congratulations!', True, test)  #text, smth, text colour, box colour
    textRect = text.get_rect()
    textRect.center = (X//2,Y//4)

    pygame.draw.rect(window, test, pygame.Rect(150,200,200,50), 4,3) #screen, colour, position[x,y,width,height], fill/border, corners
    answer1 = answer_font.render ('Play Again', True, test)
    window.blit(answer1,(190,210))
    pygame.draw.rect(window, test, pygame.Rect(375,200,200,50), 4,3) #screen, colour, position[x,y,width,height], fill/border, corners
    answer2 = answer_font.render ('Main Menu', True, test)
    window.blit(answer2,(420,210))
    pygame.draw.rect(window, test, pygame.Rect(600,200,200,50), 4,3) #screen, colour, position[x,y,width,height], fill/border, corners
    answer3 = answer_font.render ('Quit', True, test)
    window.blit(answer3,(680,210))

    window.blit(text,textRect)
    sprite()
    if page_no == 13:
        if event.type == MOUSEBUTTONDOWN:
            mouse = pygame.mouse.get_pos()
            if 150 <= mouse[0] <= 350 and 200 <= mouse[1] <= 250:
                return True
            if 375 <= mouse[0] <= 575 and 200 <= mouse[1] <= 250:
                return False
            if 600 <= mouse[0] <= 800 and 200 <= mouse[1] <= 250:
                pygame.quit()

def level1_question1():     
    quizzes = "Which of the following decimals have"     #first line
    quiz = quiz_font.render(quizzes, True, test)  
    quizRect = quiz.get_rect()
    quizRect.center = (position1)
    window.blit(quiz,quizRect)
    quizzes = "the smallest value?"                     #second line
    quiz = quiz_font.render(quizzes, True, test)    
    quizRect = quiz.get_rect()
    quizRect.center = (position2)
    window.blit(quiz,quizRect)
    sprite()
    pygame.draw.rect(window, test, pygame.Rect(250,200,200,50), 4,3) #screen, colour, position[x,y,width,height], fill/border, corners
    answer1 = answer_font.render ('A) 0.002', True, test)
    window.blit(answer1,(260,210))
    pygame.draw.rect(window, test, pygame.Rect(550,200,200,50), 4,3) #screen, colour, position[x,y,width,height], fill/border, corners
    answer2 = answer_font.render ('B) 0.02', True, test)
    window.blit(answer2,(560,210))
    pygame.draw.rect(window, test, pygame.Rect(250,300,200,50), 4,3) #screen, colour, position[x,y,width,height], fill/border, corners
    answer3 = answer_font.render ('C) 0.2', True, test)
    window.blit(answer3,(260,310))
    pygame.draw.rect(window, test, pygame.Rect(550,300,200,50), 4,3) #screen, colour, position[x,y,width,height], fill/border, corners
    answer4 = answer_font.render ('D) 2.0', True, test)
    window.blit(answer4,(560,310))

def level1_question1_answer():          #answer positions
    if event.type == MOUSEBUTTONDOWN:
        mouse = pygame.mouse.get_pos()
        if 250 <= mouse[0] <= 450 and 200 <= mouse[1] <= 250:
            return True
        if 550 <= mouse[0] <= 750 and 200 <= mouse[1] <= 250:
            return False
        if 250 <= mouse[0] <= 450 and 300 <= mouse[1] <= 350:
            return False
        if 550 <= mouse[0] <= 750 and 300 <= mouse[1] <= 350:
            return False
        else:
            return None

def level1_question2():    
    quizzes = "Suri has a number of 20-cent and 50-cent coins."    
    quiz = quiz_font.render(quizzes, True, test)  
    quizRect = quiz.get_rect()
    quizRect.center = (position1)
    window.blit(quiz,quizRect)
    quizzes = "Which of the following amounts of money is it"                     
    quiz = quiz_font.render(quizzes, True, test)    
    quizRect = quiz.get_rect()
    quizRect.center = (position2)
    window.blit(quiz,quizRect)
    quizzes = "NOT possible for her to make?"                     
    quiz = quiz_font.render(quizzes, True, test)    
    quizRect = quiz.get_rect()
    quizRect.center = (position3)
    window.blit(quiz,quizRect)    
    sprite()
    pygame.draw.rect(window, test, pygame.Rect(250,200,200,50), 4,3) #screen, colour, position[x,y,width,height], fill/border, corners
    answer1 = answer_font.render ('A) 50c', True, test)
    window.blit(answer1,(260,210))
    pygame.draw.rect(window, test, pygame.Rect(550,200,200,50), 4,3) #screen, colour, position[x,y,width,height], fill/border, corners
    answer2 = answer_font.render ('B) 60c', True, test)
    window.blit(answer2,(560,210))
    pygame.draw.rect(window, test, pygame.Rect(250,300,200,50), 4,3) #screen, colour, position[x,y,width,height], fill/border, corners
    answer3 = answer_font.render ('C) 30c', True, test)
    window.blit(answer3,(260,310))
    pygame.draw.rect(window, test, pygame.Rect(550,300,200,50), 4,3) #screen, colour, position[x,y,width,height], fill/border, corners
    answer4 = answer_font.render ('D) 80c', True, test)
    window.blit(answer4,(560,310))

def level1_question2_answer():          #answer positions
    if event.type == MOUSEBUTTONDOWN:
        mouse = pygame.mouse.get_pos()
        if 250 <= mouse[0] <= 450 and 200 <= mouse[1] <= 250:
            return False
        if 550 <= mouse[0] <= 750 and 200 <= mouse[1] <= 250:
            return False
        if 250 <= mouse[0] <= 450 and 300 <= mouse[1] <= 350:
            return True
        if 550 <= mouse[0] <= 750 and 300 <= mouse[1] <= 350:
            return False
        else:
            return None
        
def level1_question3():     
    quizzes = "Six million two hundred and three thousand and"    
    quiz = quiz_font.render(quizzes, True, test)  
    quizRect = quiz.get_rect()
    quizRect.center = (position1)
    window.blit(quiz,quizRect)
    quizzes = "six would be written as:"                     
    quiz = quiz_font.render(quizzes, True, test)    
    quizRect = quiz.get_rect()
    quizRect.center = (position2)
    window.blit(quiz,quizRect)  
    sprite()
    pygame.draw.rect(window, test, pygame.Rect(250,200,200,50), 4,3) #screen, colour, position[x,y,width,height], fill/border, corners
    answer1 = answer_font.render ('A) 62,036', True, test)
    window.blit(answer1,(260,210))
    pygame.draw.rect(window, test, pygame.Rect(550,200,200,50), 4,3) #screen, colour, position[x,y,width,height], fill/border, corners
    answer2 = answer_font.render ('B) 6,230,006', True, test)
    window.blit(answer2,(560,210))
    pygame.draw.rect(window, test, pygame.Rect(250,300,200,50), 4,3) #screen, colour, position[x,y,width,height], fill/border, corners
    answer3 = answer_font.render ('C) 6,203,006', True, test)
    window.blit(answer3,(260,310))
    pygame.draw.rect(window, test, pygame.Rect(550,300,200,50), 4,3) #screen, colour, position[x,y,width,height], fill/border, corners
    answer4 = answer_font.render ('D) 6,203,600', True, test)
    window.blit(answer4,(560,310))

def level1_question3_answer():          #answer positions
    if event.type == MOUSEBUTTONDOWN:
        mouse = pygame.mouse.get_pos()
        if 250 <= mouse[0] <= 450 and 200 <= mouse[1] <= 250:
            return False
        if 550 <= mouse[0] <= 750 and 200 <= mouse[1] <= 250:
            return False
        if 250 <= mouse[0] <= 450 and 300 <= mouse[1] <= 350:
            return True
        if 550 <= mouse[0] <= 750 and 300 <= mouse[1] <= 350:
            return False
        else:
            return None
        
def level1_question4():     
    quizzes = "Which fraction is the smallest?"    
    quiz = quiz_font.render(quizzes, True, test)  
    quizRect = quiz.get_rect()
    quizRect.center = (position1)
    window.blit(quiz,quizRect)
    sprite()
    pygame.draw.rect(window, test, pygame.Rect(250,200,200,50), 4,3) #screen, colour, position[x,y,width,height], fill/border, corners
    answer1 = answer_font.render ('A) 1/2', True, test)
    window.blit(answer1,(260,210))
    pygame.draw.rect(window, test, pygame.Rect(550,200,200,50), 4,3) #screen, colour, position[x,y,width,height], fill/border, corners
    answer2 = answer_font.render ('B) 1/4', True, test)
    window.blit(answer2,(560,210))
    pygame.draw.rect(window, test, pygame.Rect(250,300,200,50), 4,3) #screen, colour, position[x,y,width,height], fill/border, corners
    answer3 = answer_font.render ('C) 2/5', True, test)
    window.blit(answer3,(260,310))
    pygame.draw.rect(window, test, pygame.Rect(550,300,200,50), 4,3) #screen, colour, position[x,y,width,height], fill/border, corners
    answer4 = answer_font.render ('D) 1/3', True, test)
    window.blit(answer4,(560,310))

def level1_question4_answer():          #answer positions
    if event.type == MOUSEBUTTONDOWN:
        mouse = pygame.mouse.get_pos()
        if 250 <= mouse[0] <= 450 and 200 <= mouse[1] <= 250:
            return False
        if 550 <= mouse[0] <= 750 and 200 <= mouse[1] <= 250:
            return True
        if 250 <= mouse[0] <= 450 and 300 <= mouse[1] <= 350:
            return False
        if 550 <= mouse[0] <= 750 and 300 <= mouse[1] <= 350:
            return False
        else:
            return None

def level1_question5():     
    quizzes = "How many tenths are in 6.2?"    
    quiz = quiz_font.render(quizzes, True, test)  
    quizRect = quiz.get_rect()
    quizRect.center = (position1)
    window.blit(quiz,quizRect)
    sprite()
    pygame.draw.rect(window, test, pygame.Rect(250,200,200,50), 4,3) #screen, colour, position[x,y,width,height], fill/border, corners
    answer1 = answer_font.render ('A) 32', True, test)
    window.blit(answer1,(260,210))
    pygame.draw.rect(window, test, pygame.Rect(550,200,200,50), 4,3) #screen, colour, position[x,y,width,height], fill/border, corners
    answer2 = answer_font.render ('B) 12', True, test)
    window.blit(answer2,(560,210))
    pygame.draw.rect(window, test, pygame.Rect(250,300,200,50), 4,3) #screen, colour, position[x,y,width,height], fill/border, corners
    answer3 = answer_font.render ('C) 8', True, test)
    window.blit(answer3,(260,310))
    pygame.draw.rect(window, test, pygame.Rect(550,300,200,50), 4,3) #screen, colour, position[x,y,width,height], fill/border, corners
    answer4 = answer_font.render ('D) 62', True, test)
    window.blit(answer4,(560,310))

def level1_question5_answer():          #answer positions
    if event.type == MOUSEBUTTONDOWN:
        mouse = pygame.mouse.get_pos()
        if 250 <= mouse[0] <= 450 and 200 <= mouse[1] <= 250:
            return False
        if 550 <= mouse[0] <= 750 and 200 <= mouse[1] <= 250:
            return False
        if 250 <= mouse[0] <= 450 and 300 <= mouse[1] <= 350:
            return False
        if 550 <= mouse[0] <= 750 and 300 <= mouse[1] <= 350:
            return True
        else:
            return None

def level1_question6():   
    quizzes = "Leo is waiting in line at school. There are four"    
    quiz = quiz_font.render(quizzes, True, test)  
    quizRect = quiz.get_rect()
    quizRect.center = (position1)
    window.blit(quiz,quizRect)
    quizzes = "students ahead of him and twice as many behind"                     
    quiz = quiz_font.render(quizzes, True, test)    
    quizRect = quiz.get_rect()
    quizRect.center = (position2)
    window.blit(quiz,quizRect)
    quizzes = "him. How many students are in this line?"                     
    quiz = quiz_font.render(quizzes, True, test)    
    quizRect = quiz.get_rect()
    quizRect.center = (position3)
    window.blit(quiz,quizRect)    
    sprite()
    pygame.draw.rect(window, test, pygame.Rect(250,200,200,50), 4,3) #screen, colour, position[x,y,width,height], fill/border, corners
    answer1 = answer_font.render ('A) 12', True, test)
    window.blit(answer1,(260,210))
    pygame.draw.rect(window, test, pygame.Rect(550,200,200,50), 4,3) #screen, colour, position[x,y,width,height], fill/border, corners
    answer2 = answer_font.render ('B) 8', True, test)
    window.blit(answer2,(560,210))
    pygame.draw.rect(window, test, pygame.Rect(250,300,200,50), 4,3) #screen, colour, position[x,y,width,height], fill/border, corners
    answer3 = answer_font.render ('C) 13', True, test)
    window.blit(answer3,(260,310))
    pygame.draw.rect(window, test, pygame.Rect(550,300,200,50), 4,3) #screen, colour, position[x,y,width,height], fill/border, corners
    answer4 = answer_font.render ('D) 9', True, test)
    window.blit(answer4,(560,310))

def level1_question6_answer():          #answer positions
    if event.type == MOUSEBUTTONDOWN:
        mouse = pygame.mouse.get_pos()
        if 250 <= mouse[0] <= 450 and 200 <= mouse[1] <= 250:
            return False
        if 550 <= mouse[0] <= 750 and 200 <= mouse[1] <= 250:
            return False
        if 250 <= mouse[0] <= 450 and 300 <= mouse[1] <= 350:
            return True
        if 550 <= mouse[0] <= 750 and 300 <= mouse[1] <= 350:
            return False
        else:
            return None

def level1_question7():   
    quizzes = "This week at my lemonade stand I sold $29 worth of"    
    quiz = quiz_font.render(quizzes, True, test)  
    quizRect = quiz.get_rect()
    quizRect.center = (position1)
    window.blit(quiz,quizRect)
    quizzes = "lemonade, but I had spent $34 on lemons and $14 on"                     
    quiz = quiz_font.render(quizzes, True, test)    
    quizRect = quiz.get_rect()
    quizRect.center = (position2)
    window.blit(quiz,quizRect)
    quizzes = "sugar. My total loss for the week was"                     
    quiz = quiz_font.render(quizzes, True, test)    
    quizRect = quiz.get_rect()
    quizRect.center = (position3)
    window.blit(quiz,quizRect)   
    sprite()
    pygame.draw.rect(window, test, pygame.Rect(250,200,200,50), 4,3) #screen, colour, position[x,y,width,height], fill/border, corners
    answer1 = answer_font.render ('A) 1', True, test)
    window.blit(answer1,(260,210))
    pygame.draw.rect(window, test, pygame.Rect(550,200,200,50), 4,3) #screen, colour, position[x,y,width,height], fill/border, corners
    answer2 = answer_font.render ('B) 9', True, test)
    window.blit(answer2,(560,210))
    pygame.draw.rect(window, test, pygame.Rect(250,300,200,50), 4,3) #screen, colour, position[x,y,width,height], fill/border, corners
    answer3 = answer_font.render ('C) 19', True, test)
    window.blit(answer3,(260,310))
    pygame.draw.rect(window, test, pygame.Rect(550,300,200,50), 4,3) #screen, colour, position[x,y,width,height], fill/border, corners
    answer4 = answer_font.render ('D) 21', True, test)
    window.blit(answer4,(560,310))

def level1_question7_answer():          #answer positions
    if event.type == MOUSEBUTTONDOWN:
        mouse = pygame.mouse.get_pos()
        if 250 <= mouse[0] <= 450 and 200 <= mouse[1] <= 250:
            return False
        if 550 <= mouse[0] <= 750 and 200 <= mouse[1] <= 250:
            return False
        if 250 <= mouse[0] <= 450 and 300 <= mouse[1] <= 350:
            return True
        if 550 <= mouse[0] <= 750 and 300 <= mouse[1] <= 350:
            return False
        else:
            return None

def level1_question8():   
    quizzes = "At the end of a game of marbles, Lei has 15 marbles,"    
    quiz = quiz_font.render(quizzes, True, test)  
    quizRect = quiz.get_rect()
    quizRect.center = (position1)
    window.blit(quiz,quizRect)
    quizzes = "Dora has 8 and Omar has 4. How many marbles must"                     
    quiz = quiz_font.render(quizzes, True, test)    
    quizRect = quiz.get_rect()
    quizRect.center = (position2)
    window.blit(quiz,quizRect)
    quizzes = "Lei give back to his friends if they want to start"                     
    quiz = quiz_font.render(quizzes, True, test)    
    quizRect = quiz.get_rect()
    quizRect.center = (position3)
    window.blit(quiz,quizRect)   
    quizzes = "the next game with an equal number each?"                     
    quiz = quiz_font.render(quizzes, True, test)    
    quizRect = quiz.get_rect()
    quizRect.center = (position4)
    window.blit(quiz,quizRect)  
    sprite()
    pygame.draw.rect(window, test, pygame.Rect(250,200,200,50), 4,3) #screen, colour, position[x,y,width,height], fill/border, corners
    answer1 = answer_font.render ('A) 6', True, test)
    window.blit(answer1,(260,210))
    pygame.draw.rect(window, test, pygame.Rect(550,200,200,50), 4,3) #screen, colour, position[x,y,width,height], fill/border, corners
    answer2 = answer_font.render ('B) 7', True, test)
    window.blit(answer2,(560,210))
    pygame.draw.rect(window, test, pygame.Rect(250,300,200,50), 4,3) #screen, colour, position[x,y,width,height], fill/border, corners
    answer3 = answer_font.render ('C) 8', True, test)
    window.blit(answer3,(260,310))
    pygame.draw.rect(window, test, pygame.Rect(550,300,200,50), 4,3) #screen, colour, position[x,y,width,height], fill/border, corners
    answer4 = answer_font.render ('D) 9', True, test)
    window.blit(answer4,(560,310))

def level1_question8_answer():          #answer positions
    if event.type == MOUSEBUTTONDOWN:
        mouse = pygame.mouse.get_pos()
        if 250 <= mouse[0] <= 450 and 200 <= mouse[1] <= 250:
            return True
        if 550 <= mouse[0] <= 750 and 200 <= mouse[1] <= 250:
            return False
        if 250 <= mouse[0] <= 450 and 300 <= mouse[1] <= 350:
            return False
        if 550 <= mouse[0] <= 750 and 300 <= mouse[1] <= 350:
            return False
        else:
            return None

def level1_questions_method():         #generate random questions, no repeating questions
    if question == 1:
        level1_question1()
        if level1_question1_answer() == True:
            return True
        elif level1_question1_answer() == False:
            return False
    if question == 2:
        level1_question2()
        if level1_question2_answer() == True:
            return True
        elif level1_question2_answer() == False:
            return False
    if question == 3:
        level1_question3()
        if level1_question3_answer() == True:
            return True
        elif level1_question3_answer() == False:
            return False
    if question == 4:
        level1_question4()
        if level1_question4_answer() == True:
            return True
        elif level1_question4_answer() == False:
            return False
    if question == 5:
        level1_question5()
        if level1_question5_answer() == True:
            return True
        elif level1_question5_answer() == False:
            return False    
    if question == 6:
        level1_question6()
        if level1_question6_answer() == True:
            return True
        elif level1_question6_answer() == False:
            return False
    if question == 7:
        level1_question7()
        if level1_question7_answer() == True:
            return True
        elif level1_question7_answer() == False:
            return False
    if question == 8:
        level1_question8()
        if level1_question8_answer() == True:
            return True
        elif level1_question8_answer() == False:
            return False

def level1():
    level_font = pygame.font.Font('Style/minecraft_font.ttf',48)
    level_text = "Level 1"
    level = level_font.render(level_text, True, test)
    levelRect = level.get_rect()
    levelRect.center = (X//2,Y//2)
    if page_no == 5:
        window.blit(level,levelRect)
    if page_no == 6:
        level1_questions_method()


def level2_question1():     
    quizzes = "There are 14 pieces of fruit in a bowl. There are twice"     #first line
    quiz = quiz_font.render(quizzes, True, test)  
    quizRect = quiz.get_rect()
    quizRect.center = (position1)
    window.blit(quiz,quizRect)
    quizzes = "as many nectarines as pears, and half as many"                     #second line
    quiz = quiz_font.render(quizzes, True, test)    
    quizRect = quiz.get_rect()
    quizRect.center = (position2)
    window.blit(quiz,quizRect)
    quizzes = "nectarines as apples. There are no other types of"                     #second line
    quiz = quiz_font.render(quizzes, True, test)    
    quizRect = quiz.get_rect()
    quizRect.center = (position3)
    window.blit(quiz,quizRect)
    quizzes = "fruit. How many apples are there?"                     #second line
    quiz = quiz_font.render(quizzes, True, test)    
    quizRect = quiz.get_rect()
    quizRect.center = (position4)
    window.blit(quiz,quizRect)
    sprite()
    pygame.draw.rect(window, test, pygame.Rect(250,200,200,50), 4,3) #screen, colour, position[x,y,width,height], fill/border, corners
    answer1 = answer_font.render ('A) 2', True, test)
    window.blit(answer1,(260,210))
    pygame.draw.rect(window, test, pygame.Rect(550,200,200,50), 4,3) #screen, colour, position[x,y,width,height], fill/border, corners
    answer2 = answer_font.render ('B) 4', True, test)
    window.blit(answer2,(560,210))
    pygame.draw.rect(window, test, pygame.Rect(250,300,200,50), 4,3) #screen, colour, position[x,y,width,height], fill/border, corners
    answer3 = answer_font.render ('C) 6', True, test)
    window.blit(answer3,(260,310))
    pygame.draw.rect(window, test, pygame.Rect(550,300,200,50), 4,3) #screen, colour, position[x,y,width,height], fill/border, corners
    answer4 = answer_font.render ('D) 8', True, test)
    window.blit(answer4,(560,310))

def level2_question1_answer():                                      #answer positions
    if event.type == MOUSEBUTTONDOWN:
        mouse = pygame.mouse.get_pos()
        if 250 <= mouse[0] <= 450 and 200 <= mouse[1] <= 250:
            return False
        if 550 <= mouse[0] <= 750 and 200 <= mouse[1] <= 250:
            return False
        if 250 <= mouse[0] <= 450 and 300 <= mouse[1] <= 350:
            return False
        if 550 <= mouse[0] <= 750 and 300 <= mouse[1] <= 350:
            return True
        else:
            return None

def level2_question2():    
    quizzes = "Emma is going to write all the numbers from 1 to 50"    
    quiz = quiz_font.render(quizzes, True, test)  
    quizRect = quiz.get_rect()
    quizRect.center = (position1)
    window.blit(quiz,quizRect)
    quizzes = "in order. She writes 25 digits on the first line of"                     
    quiz = quiz_font.render(quizzes, True, test)    
    quizRect = quiz.get_rect()
    quizRect.center = (position2)
    window.blit(quiz,quizRect)
    quizzes = "her page. What was the last number she wrote"                     
    quiz = quiz_font.render(quizzes, True, test)    
    quizRect = quiz.get_rect()
    quizRect.center = (position3)
    window.blit(quiz,quizRect)    
    quizzes = "on this line?"                     
    quiz = quiz_font.render(quizzes, True, test)    
    quizRect = quiz.get_rect()
    quizRect.center = (position4)
    window.blit(quiz,quizRect)    
    sprite()
    pygame.draw.rect(window, test, pygame.Rect(250,200,200,50), 4,3) #screen, colour, position[x,y,width,height], fill/border, corners
    answer1 = answer_font.render ('A) 13', True, test)
    window.blit(answer1,(260,210))
    pygame.draw.rect(window, test, pygame.Rect(550,200,200,50), 4,3) #screen, colour, position[x,y,width,height], fill/border, corners
    answer2 = answer_font.render ('B) 15', True, test)
    window.blit(answer2,(560,210))
    pygame.draw.rect(window, test, pygame.Rect(250,300,200,50), 4,3) #screen, colour, position[x,y,width,height], fill/border, corners
    answer3 = answer_font.render ('C) 17', True, test)
    window.blit(answer3,(260,310))
    pygame.draw.rect(window, test, pygame.Rect(550,300,200,50), 4,3) #screen, colour, position[x,y,width,height], fill/border, corners
    answer4 = answer_font.render ('D) 19', True, test)
    window.blit(answer4,(560,310))

def level2_question2_answer():          #answer positions
    if event.type == MOUSEBUTTONDOWN:
        mouse = pygame.mouse.get_pos()
        if 250 <= mouse[0] <= 450 and 200 <= mouse[1] <= 250:
            return False
        if 550 <= mouse[0] <= 750 and 200 <= mouse[1] <= 250:
            return False
        if 250 <= mouse[0] <= 450 and 300 <= mouse[1] <= 350:
            return True
        if 550 <= mouse[0] <= 750 and 300 <= mouse[1] <= 350:
            return False
        else:
            return None
        
def level2_question3():     
    quizzes = "A kangaroo is chasing a wallaby that is 42 metres"    
    quiz = quiz_font.render(quizzes, True, test)  
    quizRect = quiz.get_rect()
    quizRect.center = (position1)
    window.blit(quiz,quizRect)
    quizzes = "ahead. For every 4-metre hop the kangaroo makes, the"                     
    quiz = quiz_font.render(quizzes, True, test)    
    quizRect = quiz.get_rect()
    quizRect.center = (position2)
    window.blit(quiz,quizRect) 
    quizzes = " wallaby makes a 1-metre hop. How many hops will the"                     
    quiz = quiz_font.render(quizzes, True, test)    
    quizRect = quiz.get_rect()
    quizRect.center = (position3)
    window.blit(quiz,quizRect)    
    quizzes = "kangaroo have to make to catch up with the wallaby?"                     
    quiz = quiz_font.render(quizzes, True, test)    
    quizRect = quiz.get_rect()
    quizRect.center = (position4)
    window.blit(quiz,quizRect)    
    sprite()
    pygame.draw.rect(window, test, pygame.Rect(250,200,200,50), 4,3) #screen, colour, position[x,y,width,height], fill/border, corners
    answer1 = answer_font.render ('A) 11', True, test)
    window.blit(answer1,(260,210))
    pygame.draw.rect(window, test, pygame.Rect(550,200,200,50), 4,3) #screen, colour, position[x,y,width,height], fill/border, corners
    answer2 = answer_font.render ('B) 14', True, test)
    window.blit(answer2,(560,210))
    pygame.draw.rect(window, test, pygame.Rect(250,300,200,50), 4,3) #screen, colour, position[x,y,width,height], fill/border, corners
    answer3 = answer_font.render ('C) 16', True, test)
    window.blit(answer3,(260,310))
    pygame.draw.rect(window, test, pygame.Rect(550,300,200,50), 4,3) #screen, colour, position[x,y,width,height], fill/border, corners
    answer4 = answer_font.render ('D) 21', True, test)
    window.blit(answer4,(560,310))

def level2_question3_answer():          #answer positions
    if event.type == MOUSEBUTTONDOWN:
        mouse = pygame.mouse.get_pos()
        if 250 <= mouse[0] <= 450 and 200 <= mouse[1] <= 250:
            return False
        if 550 <= mouse[0] <= 750 and 200 <= mouse[1] <= 250:
            return True
        if 250 <= mouse[0] <= 450 and 300 <= mouse[1] <= 350:
            return False
        if 550 <= mouse[0] <= 750 and 300 <= mouse[1] <= 350:
            return False
        else:
            return None
        
def level2_question4():     
    quizzes = "You have 12 metres of ribbon. Each decoration needs"    
    quiz = quiz_font.render(quizzes, True, test)  
    quizRect = quiz.get_rect()
    quizRect.center = (position1)
    window.blit(quiz,quizRect)
    quizzes = "2/5 of a metre of ribbon. How many decorations"                     
    quiz = quiz_font.render(quizzes, True, test)    
    quizRect = quiz.get_rect()
    quizRect.center = (position2)
    window.blit(quiz,quizRect) 
    quizzes = "can you make?"                     
    quiz = quiz_font.render(quizzes, True, test)    
    quizRect = quiz.get_rect()
    quizRect.center = (position3)
    window.blit(quiz,quizRect)    
    sprite()
    pygame.draw.rect(window, test, pygame.Rect(250,200,200,50), 4,3) #screen, colour, position[x,y,width,height], fill/border, corners
    answer1 = answer_font.render ('A) 7', True, test)
    window.blit(answer1,(260,210))
    pygame.draw.rect(window, test, pygame.Rect(550,200,200,50), 4,3) #screen, colour, position[x,y,width,height], fill/border, corners
    answer2 = answer_font.render ('B) 10', True, test)
    window.blit(answer2,(560,210))
    pygame.draw.rect(window, test, pygame.Rect(250,300,200,50), 4,3) #screen, colour, position[x,y,width,height], fill/border, corners
    answer3 = answer_font.render ('C) 24', True, test)
    window.blit(answer3,(260,310))
    pygame.draw.rect(window, test, pygame.Rect(550,300,200,50), 4,3) #screen, colour, position[x,y,width,height], fill/border, corners
    answer4 = answer_font.render ('D) 30', True, test)
    window.blit(answer4,(560,310))

def level2_question4_answer():          #answer positions
    if event.type == MOUSEBUTTONDOWN:
        mouse = pygame.mouse.get_pos()
        if 250 <= mouse[0] <= 450 and 200 <= mouse[1] <= 250:
            return False
        if 550 <= mouse[0] <= 750 and 200 <= mouse[1] <= 250:
            return False
        if 250 <= mouse[0] <= 450 and 300 <= mouse[1] <= 350:
            return False
        if 550 <= mouse[0] <= 750 and 300 <= mouse[1] <= 350:
            return True
        else:
            return None

def level2_question5():     
    quizzes = "A carpet tile measures 50 cm by 50 cm. How many of"    
    quiz = quiz_font.render(quizzes, True, test)  
    quizRect = quiz.get_rect()
    quizRect.center = (position1)
    window.blit(quiz,quizRect)
    quizzes = "these tiles would be needed to cover the floor of"    
    quiz = quiz_font.render(quizzes, True, test)  
    quizRect = quiz.get_rect()
    quizRect.center = (position2)
    window.blit(quiz,quizRect)
    quizzes = "a room 6m long and 4m wide?"    
    quiz = quiz_font.render(quizzes, True, test)  
    quizRect = quiz.get_rect()
    quizRect.center = (position3)
    window.blit(quiz,quizRect)
    sprite()
    pygame.draw.rect(window, test, pygame.Rect(250,200,200,50), 4,3) #screen, colour, position[x,y,width,height], fill/border, corners
    answer1 = answer_font.render ('A) 96', True, test)
    window.blit(answer1,(260,210))
    pygame.draw.rect(window, test, pygame.Rect(550,200,200,50), 4,3) #screen, colour, position[x,y,width,height], fill/border, corners
    answer2 = answer_font.render ('B) 48', True, test)
    window.blit(answer2,(560,210))
    pygame.draw.rect(window, test, pygame.Rect(250,300,200,50), 4,3) #screen, colour, position[x,y,width,height], fill/border, corners
    answer3 = answer_font.render ('C) 24', True, test)
    window.blit(answer3,(260,310))
    pygame.draw.rect(window, test, pygame.Rect(550,300,200,50), 4,3) #screen, colour, position[x,y,width,height], fill/border, corners
    answer4 = answer_font.render ('D) 20', True, test)
    window.blit(answer4,(560,310))

def level2_question5_answer():          #answer positions
    if event.type == MOUSEBUTTONDOWN:
        mouse = pygame.mouse.get_pos()
        if 250 <= mouse[0] <= 450 and 200 <= mouse[1] <= 250:
            return True
        if 550 <= mouse[0] <= 750 and 200 <= mouse[1] <= 250:
            return False
        if 250 <= mouse[0] <= 450 and 300 <= mouse[1] <= 350:
            return False
        if 550 <= mouse[0] <= 750 and 300 <= mouse[1] <= 350:
            return False
        else:
            return None

def level2_question6():   
    quizzes = "A class of 24 students, all of different heights, is"    
    quiz = quiz_font.render(quizzes, True, test)  
    quizRect = quiz.get_rect()
    quizRect.center = (position1)
    window.blit(quiz,quizRect)
    quizzes = "standing in a line from tallest to shortest. Mary is"                     
    quiz = quiz_font.render(quizzes, True, test)    
    quizRect = quiz.get_rect()
    quizRect.center = (position2)
    window.blit(quiz,quizRect)
    quizzes = "the 8th tallest and John is the 6th shortest. How many"                     
    quiz = quiz_font.render(quizzes, True, test)    
    quizRect = quiz.get_rect()
    quizRect.center = (position3)
    window.blit(quiz,quizRect)
    quizzes = "students are standing between them in the line?"                     
    quiz = quiz_font.render(quizzes, True, test)    
    quizRect = quiz.get_rect()
    quizRect.center = (position4)
    window.blit(quiz,quizRect)  
    sprite()
    pygame.draw.rect(window, test, pygame.Rect(250,200,200,50), 4,3) #screen, colour, position[x,y,width,height], fill/border, corners
    answer1 = answer_font.render ('A) 7', True, test)
    window.blit(answer1,(260,210))
    pygame.draw.rect(window, test, pygame.Rect(550,200,200,50), 4,3) #screen, colour, position[x,y,width,height], fill/border, corners
    answer2 = answer_font.render ('B) 8', True, test)
    window.blit(answer2,(560,210))
    pygame.draw.rect(window, test, pygame.Rect(250,300,200,50), 4,3) #screen, colour, position[x,y,width,height], fill/border, corners
    answer3 = answer_font.render ('C) 9', True, test)
    window.blit(answer3,(260,310))
    pygame.draw.rect(window, test, pygame.Rect(550,300,200,50), 4,3) #screen, colour, position[x,y,width,height], fill/border, corners
    answer4 = answer_font.render ('D) 10', True, test)
    window.blit(answer4,(560,310))

def level2_question6_answer():          #answer positions
    if event.type == MOUSEBUTTONDOWN:
        mouse = pygame.mouse.get_pos()
        if 250 <= mouse[0] <= 450 and 200 <= mouse[1] <= 250:
            return False
        if 550 <= mouse[0] <= 750 and 200 <= mouse[1] <= 250:
            return False
        if 250 <= mouse[0] <= 450 and 300 <= mouse[1] <= 350:
            return False
        if 550 <= mouse[0] <= 750 and 300 <= mouse[1] <= 350:
            return True
        else:
            return None

def level2_question7():   
    quizzes = "Sally thinks of a number, multiplies it by 2, adds 2,"    
    quiz = quiz_font.render(quizzes, True, test)  
    quizRect = quiz.get_rect()
    quizRect.center = (position1)
    window.blit(quiz,quizRect)
    quizzes = "divides by 2 and then subtracts 2. Her answer is 2."                     
    quiz = quiz_font.render(quizzes, True, test)    
    quizRect = quiz.get_rect()
    quizRect.center = (position2)
    window.blit(quiz,quizRect)
    quizzes = "What was her original number?"                     
    quiz = quiz_font.render(quizzes, True, test)    
    quizRect = quiz.get_rect()
    quizRect.center = (position3)
    window.blit(quiz,quizRect)  
    sprite()
    pygame.draw.rect(window, test, pygame.Rect(250,200,200,50), 4,3) #screen, colour, position[x,y,width,height], fill/border, corners
    answer1 = answer_font.render ('A) 1', True, test)
    window.blit(answer1,(260,210))
    pygame.draw.rect(window, test, pygame.Rect(550,200,200,50), 4,3) #screen, colour, position[x,y,width,height], fill/border, corners
    answer2 = answer_font.render ('B) 2', True, test)
    window.blit(answer2,(560,210))
    pygame.draw.rect(window, test, pygame.Rect(250,300,200,50), 4,3) #screen, colour, position[x,y,width,height], fill/border, corners
    answer3 = answer_font.render ('C) 3', True, test)
    window.blit(answer3,(260,310))
    pygame.draw.rect(window, test, pygame.Rect(550,300,200,50), 4,3) #screen, colour, position[x,y,width,height], fill/border, corners
    answer4 = answer_font.render ('D) 4', True, test)
    window.blit(answer4,(560,310))

def level2_question7_answer():          #answer positions
    if event.type == MOUSEBUTTONDOWN:
        mouse = pygame.mouse.get_pos()
        if 250 <= mouse[0] <= 450 and 200 <= mouse[1] <= 250:
            return False
        if 550 <= mouse[0] <= 750 and 200 <= mouse[1] <= 250:
            return False
        if 250 <= mouse[0] <= 450 and 300 <= mouse[1] <= 350:
            return True
        if 550 <= mouse[0] <= 750 and 300 <= mouse[1] <= 350:
            return False
        else:
            return None

def level2_question8():   
    quizzes = "Greg is 19 years old, Karin is 26 and Anthony is 31."    
    quiz = quiz_font.render(quizzes, True, test)  
    quizRect = quiz.get_rect()
    quizRect.center = (position1)
    window.blit(quiz,quizRect)
    quizzes = "In how many years from now will their ages add to 100?"                     
    quiz = quiz_font.render(quizzes, True, test)    
    quizRect = quiz.get_rect()
    quizRect.center = (position2)
    window.blit(quiz,quizRect)
    sprite()
    pygame.draw.rect(window, test, pygame.Rect(250,200,200,50), 4,3) #screen, colour, position[x,y,width,height], fill/border, corners
    answer1 = answer_font.render ('A) 8', True, test)
    window.blit(answer1,(260,210))
    pygame.draw.rect(window, test, pygame.Rect(550,200,200,50), 4,3) #screen, colour, position[x,y,width,height], fill/border, corners
    answer2 = answer_font.render ('B) 16', True, test)
    window.blit(answer2,(560,210))
    pygame.draw.rect(window, test, pygame.Rect(250,300,200,50), 4,3) #screen, colour, position[x,y,width,height], fill/border, corners
    answer3 = answer_font.render ('C) 24', True, test)
    window.blit(answer3,(260,310))
    pygame.draw.rect(window, test, pygame.Rect(550,300,200,50), 4,3) #screen, colour, position[x,y,width,height], fill/border, corners
    answer4 = answer_font.render ('D) 26', True, test)
    window.blit(answer4,(560,310))

def level2_question8_answer():          #answer positions
    if event.type == MOUSEBUTTONDOWN:
        mouse = pygame.mouse.get_pos()
        if 250 <= mouse[0] <= 450 and 200 <= mouse[1] <= 250:
            return True
        if 550 <= mouse[0] <= 750 and 200 <= mouse[1] <= 250:
            return False
        if 250 <= mouse[0] <= 450 and 300 <= mouse[1] <= 350:
            return False
        if 550 <= mouse[0] <= 750 and 300 <= mouse[1] <= 350:
            return False
        else:
            return None

def level2_questions_method():         #generate random questions, no repeating questions
    if question == 1:
        level2_question1()
        if level2_question1_answer() == True:
            return True
        elif level2_question1_answer() == False:
            return False
    if question == 2:
        level2_question2()
        if level2_question2_answer() == True:
            return True
        elif level2_question2_answer() == False:
            return False
    if question == 3:
        level2_question3()
        if level2_question3_answer() == True:
            return True
        elif level2_question3_answer() == False:
            return False
    if question == 4:
        level2_question4()
        if level2_question4_answer() == True:
            return True
        elif level2_question4_answer() == False:
            return False
    if question == 5:
        level2_question5()
        if level2_question5_answer() == True:
            return True
        elif level2_question5_answer() == False:
            return False    
    if question == 6:
        level2_question6()
        if level2_question6_answer() == True:
            return True
        elif level2_question6_answer() == False:
            return False
    if question == 7:
        level2_question7()
        if level2_question7_answer() == True:
            return True
        elif level2_question7_answer() == False:
            return False
    if question == 8:
        level2_question8()
        if level2_question8_answer() == True:
            return True
        elif level2_question8_answer() == False:
            return False

def level2():
    level_font = pygame.font.Font('Style/minecraft_font.ttf',48)
    level_text = "Level 2"
    level = level_font.render(level_text, True, test)
    levelRect = level.get_rect()
    levelRect.center = (X//2,Y//2)
    if page_no == 8:
        window.blit(level,levelRect)
    if page_no == 9:
        level2_questions_method()


def level3_question1():     
    quizzes = "Lola went on a train trip. During her journey she"     #first line
    quiz = quiz_font.render(quizzes, True, test)  
    quizRect = quiz.get_rect()
    quizRect.center = (position1)
    window.blit(quiz,quizRect)
    quizzes = "slept for 3/4 of an hour and stayed awake for 3/4 of"                     #second line
    quiz = quiz_font.render(quizzes, True, test)    
    quizRect = quiz.get_rect()
    quizRect.center = (position2)
    window.blit(quiz,quizRect)
    quizzes = "the journey. How long did the trip take?"                     #second line
    quiz = quiz_font.render(quizzes, True, test)    
    quizRect = quiz.get_rect()
    quizRect.center = (position3)
    window.blit(quiz,quizRect)
    sprite()
    pygame.draw.rect(window, test, pygame.Rect(250,200,200,50), 4,3) #screen, colour, position[x,y,width,height], fill/border, corners
    answer1 = answer_font.render ('A) 1 hr', True, test)
    window.blit(answer1,(260,210))
    pygame.draw.rect(window, test, pygame.Rect(550,200,200,50), 4,3) #screen, colour, position[x,y,width,height], fill/border, corners
    answer2 = answer_font.render ('B) 2 hrs', True, test)
    window.blit(answer2,(560,210))
    pygame.draw.rect(window, test, pygame.Rect(250,300,200,50), 4,3) #screen, colour, position[x,y,width,height], fill/border, corners
    answer3 = answer_font.render ('C) 2 1/2 hrs', True, test)
    window.blit(answer3,(260,310))
    pygame.draw.rect(window, test, pygame.Rect(550,300,200,50), 4,3) #screen, colour, position[x,y,width,height], fill/border, corners
    answer4 = answer_font.render ('D) 3 hrs', True, test)
    window.blit(answer4,(560,310))

def level3_question1_answer():                                      #answer positions
    if event.type == MOUSEBUTTONDOWN:
        mouse = pygame.mouse.get_pos()
        if 250 <= mouse[0] <= 450 and 200 <= mouse[1] <= 250:
            return False
        if 550 <= mouse[0] <= 750 and 200 <= mouse[1] <= 250:
            return False
        if 250 <= mouse[0] <= 450 and 300 <= mouse[1] <= 350:
            return False
        if 550 <= mouse[0] <= 750 and 300 <= mouse[1] <= 350:
            return True
        else:
            return None

def level3_question2():    
    quizzes = "I have a jug containing 100 mL of liquid, which is"    
    quiz = quiz_font.render(quizzes, True, test)  
    quizRect = quiz.get_rect()
    quizRect.center = (position1)
    window.blit(quiz,quizRect)
    quizzes = "half vinegar and half olive oil. How much vinegar must"                     
    quiz = quiz_font.render(quizzes, True, test)    
    quizRect = quiz.get_rect()
    quizRect.center = (position2)
    window.blit(quiz,quizRect)
    quizzes = "I add to make a mixture which is one-third olive oil?"                     
    quiz = quiz_font.render(quizzes, True, test)    
    quizRect = quiz.get_rect()
    quizRect.center = (position3)
    window.blit(quiz,quizRect)       
    sprite()
    pygame.draw.rect(window, test, pygame.Rect(250,200,200,50), 4,3) #screen, colour, position[x,y,width,height], fill/border, corners
    answer1 = answer_font.render ('A) 50ml', True, test)
    window.blit(answer1,(260,210))
    pygame.draw.rect(window, test, pygame.Rect(550,200,200,50), 4,3) #screen, colour, position[x,y,width,height], fill/border, corners
    answer2 = answer_font.render ('B) 40ml', True, test)
    window.blit(answer2,(560,210))
    pygame.draw.rect(window, test, pygame.Rect(250,300,200,50), 4,3) #screen, colour, position[x,y,width,height], fill/border, corners
    answer3 = answer_font.render ('C) 90ml', True, test)
    window.blit(answer3,(260,310))
    pygame.draw.rect(window, test, pygame.Rect(550,300,200,50), 4,3) #screen, colour, position[x,y,width,height], fill/border, corners
    answer4 = answer_font.render ('D) 100ml', True, test)
    window.blit(answer4,(560,310))

def level3_question2_answer():          #answer positions
    if event.type == MOUSEBUTTONDOWN:
        mouse = pygame.mouse.get_pos()
        if 250 <= mouse[0] <= 450 and 200 <= mouse[1] <= 250:
            return True
        if 550 <= mouse[0] <= 750 and 200 <= mouse[1] <= 250:
            return False
        if 250 <= mouse[0] <= 450 and 300 <= mouse[1] <= 350:
            return False
        if 550 <= mouse[0] <= 750 and 300 <= mouse[1] <= 350:
            return False
        else:
            return None
        
def level3_question3():     
    quizzes = "Different numbers can be made using the digits 1, 5, 6, 8"    
    quiz = quiz_font.render(quizzes, True, test)  
    quizRect = quiz.get_rect()
    quizRect.center = (position1)
    window.blit(quiz,quizRect)
    quizzes = "and a decimal point. How many possibilities are there if"                     
    quiz = quiz_font.render(quizzes, True, test)    
    quizRect = quiz.get_rect()
    quizRect.center = (position2)
    window.blit(quiz,quizRect) 
    quizzes = "each digit must be used exactly once and the decimal"                     
    quiz = quiz_font.render(quizzes, True, test)    
    quizRect = quiz.get_rect()
    quizRect.center = (position3)
    window.blit(quiz,quizRect)    
    quizzes = "point must lie between two digits?"                     
    quiz = quiz_font.render(quizzes, True, test)    
    quizRect = quiz.get_rect()
    quizRect.center = (position4)
    window.blit(quiz,quizRect)    
    sprite()
    pygame.draw.rect(window, test, pygame.Rect(250,200,200,50), 4,3) #screen, colour, position[x,y,width,height], fill/border, corners
    answer1 = answer_font.render ('A) 72', True, test)
    window.blit(answer1,(260,210))
    pygame.draw.rect(window, test, pygame.Rect(550,200,200,50), 4,3) #screen, colour, position[x,y,width,height], fill/border, corners
    answer2 = answer_font.render ('B) 146', True, test)
    window.blit(answer2,(560,210))
    pygame.draw.rect(window, test, pygame.Rect(250,300,200,50), 4,3) #screen, colour, position[x,y,width,height], fill/border, corners
    answer3 = answer_font.render ('C) 120', True, test)
    window.blit(answer3,(260,310))
    pygame.draw.rect(window, test, pygame.Rect(550,300,200,50), 4,3) #screen, colour, position[x,y,width,height], fill/border, corners
    answer4 = answer_font.render ('D) 96', True, test)
    window.blit(answer4,(560,310))

def level3_question3_answer():          #answer positions
    if event.type == MOUSEBUTTONDOWN:
        mouse = pygame.mouse.get_pos()
        if 250 <= mouse[0] <= 450 and 200 <= mouse[1] <= 250:
            return True
        if 550 <= mouse[0] <= 750 and 200 <= mouse[1] <= 250:
            return False
        if 250 <= mouse[0] <= 450 and 300 <= mouse[1] <= 350:
            return False
        if 550 <= mouse[0] <= 750 and 300 <= mouse[1] <= 350:
            return False
        else:
            return None
        
def level3_question4():     
    quizzes = "A bale of hay can be eaten by a horse in 2 days, by a"    
    quiz = quiz_font.render(quizzes, True, test)  
    quizRect = quiz.get_rect()
    quizRect.center = (position1)
    window.blit(quiz,quizRect)
    quizzes = "cow in 3 days and by a sheep in 12 days. A farmer"                     
    quiz = quiz_font.render(quizzes, True, test)    
    quizRect = quiz.get_rect()
    quizRect.center = (position2)
    window.blit(quiz,quizRect) 
    quizzes = "has 22 bales of hay and one horse, one cow and one"                     
    quiz = quiz_font.render(quizzes, True, test)    
    quizRect = quiz.get_rect()
    quizRect.center = (position3)
    window.blit(quiz,quizRect)    
    quizzes = "sheep to feed. How many days will his bales last?"                     
    quiz = quiz_font.render(quizzes, True, test)    
    quizRect = quiz.get_rect()
    quizRect.center = (position4)
    window.blit(quiz,quizRect)    
    sprite()
    pygame.draw.rect(window, test, pygame.Rect(250,200,200,50), 4,3) #screen, colour, position[x,y,width,height], fill/border, corners
    answer1 = answer_font.render ('A) 20', True, test)
    window.blit(answer1,(260,210))
    pygame.draw.rect(window, test, pygame.Rect(550,200,200,50), 4,3) #screen, colour, position[x,y,width,height], fill/border, corners
    answer2 = answer_font.render ('B) 22', True, test)
    window.blit(answer2,(560,210))
    pygame.draw.rect(window, test, pygame.Rect(250,300,200,50), 4,3) #screen, colour, position[x,y,width,height], fill/border, corners
    answer3 = answer_font.render ('C) 24', True, test)
    window.blit(answer3,(260,310))
    pygame.draw.rect(window, test, pygame.Rect(550,300,200,50), 4,3) #screen, colour, position[x,y,width,height], fill/border, corners
    answer4 = answer_font.render ('D) 26', True, test)
    window.blit(answer4,(560,310))

def level3_question4_answer():          #answer positions
    if event.type == MOUSEBUTTONDOWN:
        mouse = pygame.mouse.get_pos()
        if 250 <= mouse[0] <= 450 and 200 <= mouse[1] <= 250:
            return False
        if 550 <= mouse[0] <= 750 and 200 <= mouse[1] <= 250:
            return False
        if 250 <= mouse[0] <= 450 and 300 <= mouse[1] <= 350:
            return True
        if 550 <= mouse[0] <= 750 and 300 <= mouse[1] <= 350:
            return False
        else:
            return None

def level3_question5():     
    quizzes = "On my chicken farm where I have 24 pens, the pens"    
    quiz = quiz_font.render(quizzes, True, test)  
    quizRect = quiz.get_rect()
    quizRect.center = (position1)
    window.blit(quiz,quizRect)
    quizzes = "were a bit crowded. So I built 6 more pens, and"    
    quiz = quiz_font.render(quizzes, True, test)  
    quizRect = quiz.get_rect()
    quizRect.center = (position2)
    window.blit(quiz,quizRect)
    quizzes = "the number of chickens in each pen reduced by 6."    
    quiz = quiz_font.render(quizzes, True, test)  
    quizRect = quiz.get_rect()
    quizRect.center = (position3)
    window.blit(quiz,quizRect)
    quizzes = "How many chickens do I have?"    
    quiz = quiz_font.render(quizzes, True, test)  
    quizRect = quiz.get_rect()
    quizRect.center = (position4)
    window.blit(quiz,quizRect)
    sprite()
    pygame.draw.rect(window, test, pygame.Rect(250,200,200,50), 4,3) #screen, colour, position[x,y,width,height], fill/border, corners
    answer1 = answer_font.render ('A) 480', True, test)
    window.blit(answer1,(260,210))
    pygame.draw.rect(window, test, pygame.Rect(550,200,200,50), 4,3) #screen, colour, position[x,y,width,height], fill/border, corners
    answer2 = answer_font.render ('B) 720', True, test)
    window.blit(answer2,(560,210))
    pygame.draw.rect(window, test, pygame.Rect(250,300,200,50), 4,3) #screen, colour, position[x,y,width,height], fill/border, corners
    answer3 = answer_font.render ('C) 600', True, test)
    window.blit(answer3,(260,310))
    pygame.draw.rect(window, test, pygame.Rect(550,300,200,50), 4,3) #screen, colour, position[x,y,width,height], fill/border, corners
    answer4 = answer_font.render ('D) 840', True, test)
    window.blit(answer4,(560,310))

def level3_question5_answer():          #answer positions
    if event.type == MOUSEBUTTONDOWN:
        mouse = pygame.mouse.get_pos()
        if 250 <= mouse[0] <= 450 and 200 <= mouse[1] <= 250:
            return False
        if 550 <= mouse[0] <= 750 and 200 <= mouse[1] <= 250:
            return True
        if 250 <= mouse[0] <= 450 and 300 <= mouse[1] <= 350:
            return False
        if 550 <= mouse[0] <= 750 and 300 <= mouse[1] <= 350:
            return False
        else:
            return None

def level3_question6():   
    quizzes = "Kayla is 5 years old and Ryan is 13 years younger"    
    quiz = quiz_font.render(quizzes, True, test)  
    quizRect = quiz.get_rect()
    quizRect.center = (position1)
    window.blit(quiz,quizRect)
    quizzes = "than Cody. One year ago, Cody’s age was twice the"                     
    quiz = quiz_font.render(quizzes, True, test)    
    quizRect = quiz.get_rect()
    quizRect.center = (position2)
    window.blit(quiz,quizRect)
    quizzes = "sum of Kayla’s and Ryan’s age. Find the sum of the"                     
    quiz = quiz_font.render(quizzes, True, test)    
    quizRect = quiz.get_rect()
    quizRect.center = (position3)
    window.blit(quiz,quizRect)
    quizzes = "three children’s current ages."                     
    quiz = quiz_font.render(quizzes, True, test)    
    quizRect = quiz.get_rect()
    quizRect.center = (position4)
    window.blit(quiz,quizRect)  
    sprite()
    pygame.draw.rect(window, test, pygame.Rect(250,200,200,50), 4,3) #screen, colour, position[x,y,width,height], fill/border, corners
    answer1 = answer_font.render ('A) 20', True, test)
    window.blit(answer1,(260,210))
    pygame.draw.rect(window, test, pygame.Rect(550,200,200,50), 4,3) #screen, colour, position[x,y,width,height], fill/border, corners
    answer2 = answer_font.render ('B) 26', True, test)
    window.blit(answer2,(560,210))
    pygame.draw.rect(window, test, pygame.Rect(250,300,200,50), 4,3) #screen, colour, position[x,y,width,height], fill/border, corners
    answer3 = answer_font.render ('C) 30', True, test)
    window.blit(answer3,(260,310))
    pygame.draw.rect(window, test, pygame.Rect(550,300,200,50), 4,3) #screen, colour, position[x,y,width,height], fill/border, corners
    answer4 = answer_font.render ('D) 36', True, test)
    window.blit(answer4,(560,310))

def level3_question6_answer():          #answer positions
    if event.type == MOUSEBUTTONDOWN:
        mouse = pygame.mouse.get_pos()
        if 250 <= mouse[0] <= 450 and 200 <= mouse[1] <= 250:
            return False
        if 550 <= mouse[0] <= 750 and 200 <= mouse[1] <= 250:
            return False
        if 250 <= mouse[0] <= 450 and 300 <= mouse[1] <= 350:
            return True
        if 550 <= mouse[0] <= 750 and 300 <= mouse[1] <= 350:
            return False
        else:
            return None

def level3_question7():   
    quizzes = "Our school is organising a quiz night. They are expecting"    
    quiz = quiz_font.render(quizzes, True, test)  
    quizRect = quiz.get_rect()
    quizRect.center = (position1)
    window.blit(quiz,quizRect)
    quizzes = "from 25 to 35 people to come. The people will be arranged"                     
    quiz = quiz_font.render(quizzes, True, test)    
    quizRect = quiz.get_rect()
    quizRect.center = (position2)
    window.blit(quiz,quizRect)
    quizzes = "in teams of 6 to 8 people. What is the range of possible"                     
    quiz = quiz_font.render(quizzes, True, test)    
    quizRect = quiz.get_rect()
    quizRect.center = (position3)
    window.blit(quiz,quizRect)  
    quizzes = "numbers of teams to expect?"                     
    quiz = quiz_font.render(quizzes, True, test)    
    quizRect = quiz.get_rect()
    quizRect.center = (position4)
    window.blit(quiz,quizRect) 
    sprite()
    pygame.draw.rect(window, test, pygame.Rect(250,200,200,50), 4,3) #screen, colour, position[x,y,width,height], fill/border, corners
    answer1 = answer_font.render ('A) 4 to 5', True, test)
    window.blit(answer1,(260,210))
    pygame.draw.rect(window, test, pygame.Rect(550,200,200,50), 4,3) #screen, colour, position[x,y,width,height], fill/border, corners
    answer2 = answer_font.render ('B) 4 to 6', True, test)
    window.blit(answer2,(560,210))
    pygame.draw.rect(window, test, pygame.Rect(250,300,200,50), 4,3) #screen, colour, position[x,y,width,height], fill/border, corners
    answer3 = answer_font.render ('C) 3 to 5', True, test)
    window.blit(answer3,(260,310))
    pygame.draw.rect(window, test, pygame.Rect(550,300,200,50), 4,3) #screen, colour, position[x,y,width,height], fill/border, corners
    answer4 = answer_font.render ('D) 3 to 6', True, test)
    window.blit(answer4,(560,310))

def level3_question7_answer():          #answer positions
    if event.type == MOUSEBUTTONDOWN:
        mouse = pygame.mouse.get_pos()
        if 250 <= mouse[0] <= 450 and 200 <= mouse[1] <= 250:
            return True
        if 550 <= mouse[0] <= 750 and 200 <= mouse[1] <= 250:
            return False
        if 250 <= mouse[0] <= 450 and 300 <= mouse[1] <= 350:
            return False
        if 550 <= mouse[0] <= 750 and 300 <= mouse[1] <= 350:
            return False
        else:
            return None

def level3_question8():   
    quizzes = "It is 10 am now. What time will it be in 2021"    
    quiz = quiz_font.render(quizzes, True, test)  
    quizRect = quiz.get_rect()
    quizRect.center = (position1)
    window.blit(quiz,quizRect)
    quizzes = "hours time?"                     
    quiz = quiz_font.render(quizzes, True, test)    
    quizRect = quiz.get_rect()
    quizRect.center = (position2)
    window.blit(quiz,quizRect)
    sprite()
    pygame.draw.rect(window, test, pygame.Rect(250,200,200,50), 4,3) #screen, colour, position[x,y,width,height], fill/border, corners
    answer1 = answer_font.render ('A) 3pm', True, test)
    window.blit(answer1,(260,210))
    pygame.draw.rect(window, test, pygame.Rect(550,200,200,50), 4,3) #screen, colour, position[x,y,width,height], fill/border, corners
    answer2 = answer_font.render ('B) 1pm', True, test)
    window.blit(answer2,(560,210))
    pygame.draw.rect(window, test, pygame.Rect(250,300,200,50), 4,3) #screen, colour, position[x,y,width,height], fill/border, corners
    answer3 = answer_font.render ('C) 8am', True, test)
    window.blit(answer3,(260,310))
    pygame.draw.rect(window, test, pygame.Rect(550,300,200,50), 4,3) #screen, colour, position[x,y,width,height], fill/border, corners
    answer4 = answer_font.render ('D) 10am', True, test)
    window.blit(answer4,(560,310))

def level3_question8_answer():          #answer positions
    if event.type == MOUSEBUTTONDOWN:
        mouse = pygame.mouse.get_pos()
        if 250 <= mouse[0] <= 450 and 200 <= mouse[1] <= 250:
            return True
        if 550 <= mouse[0] <= 750 and 200 <= mouse[1] <= 250:
            return False
        if 250 <= mouse[0] <= 450 and 300 <= mouse[1] <= 350:
            return False
        if 550 <= mouse[0] <= 750 and 300 <= mouse[1] <= 350:
            return False
        else:
            return None

def level3_questions_method():         #generate random questions, no repeating questions
    if question == 1:
        level3_question1()
        if level3_question1_answer() == True:
            return True
        elif level3_question1_answer() == False:
            return False
    if question == 2:
        level3_question2()
        if level3_question2_answer() == True:
            return True
        elif level3_question2_answer() == False:
            return False
    if question == 3:
        level3_question3()
        if level3_question3_answer() == True:
            return True
        elif level3_question3_answer() == False:
            return False
    if question == 4:
        level3_question4()
        if level3_question4_answer() == True:
            return True
        elif level3_question4_answer() == False:
            return False
    if question == 5:
        level3_question5()
        if level3_question5_answer() == True:
            return True
        elif level3_question5_answer() == False:
            return False    
    if question == 6:
        level3_question6()
        if level3_question6_answer() == True:
            return True
        elif level3_question6_answer() == False:
            return False
    if question == 7:
        level3_question7()
        if level3_question7_answer() == True:
            return True
        elif level3_question7_answer() == False:
            return False
    if question == 8:
        level3_question8()
        if level3_question8_answer() == True:
            return True
        elif level3_question8_answer() == False:
            return False

def level3():
    level_font = pygame.font.Font('Style/minecraft_font.ttf',48)
    level_text = "Level 3"
    level = level_font.render(level_text, True, test)
    levelRect = level.get_rect()
    levelRect.center = (X//2,Y//2)
    if page_no == 11:
        window.blit(level,levelRect)
    if page_no == 12:
        level3_questions_method()

def sprite():
    font = pygame.font.Font('Style/minecraft_font.ttf',24)  #font, size
    if page_no != 13:
        text = f"{score +1}/5"
        text = font.render(text, True, test)  #text, smth, text colour, box colour
        textRect = text.get_rect()
        textRect.center = (810,40)
        window.blit (text,textRect)
    if life == 3:
        window.blit(happy,postion_sprite)
        if page_no != 13:
            window.blit(heart1,postion_heart1)
            window.blit(heart2,postion_heart2)
            window.blit(heart3,postion_heart3)
    if life == 2:
        window.blit(normal,postion_sprite)
        if page_no != 13:
            window.blit(heart1,postion_heart1)
            window.blit(heart2,postion_heart2)
    if life == 1:
        window.blit(dying,postion_sprite)
        if page_no != 13:
            window.blit(heart1,postion_heart1)
    if life == 0:
        window.blit(dead,postion_sprite)


numer_list = []         #generate random question after first one
all_questions = 0
a = 0
change = 1



while running:
    mouse = pygame.mouse.get_pos()      #stores mouse position
    window.blit(bg_img,(0,0))           #background image
    infopages()                             #change the page after first click
    level1()
    level2()
    level3()  
    if change == 1:
        numer_list.clear()
        all_questions = 0
        while all_questions < 7:
            question_no = random.randint(2,8)
            if question_no not in numer_list:
                numer_list.append(question_no)
                all_questions = all_questions + 1
        change = 0
        print (all_questions)
        print(numer_list)
    for event in pygame.event.get():  
        if page_no <= 5:                #stops page turning after instructions
            if event.type == MOUSEBUTTONUP: #if mouse clicked
                page_no = page_no + 1
        
        if page_no == 6:
            if score < 5:
                if level1_questions_method() == False:
                    question = numer_list[a]    #question no. = random number in list
                    a = a + 1
                    life = life - 1
                    if life == 0:
                        page_no = 99
                if level1_questions_method() == True:
                    question = numer_list[a]
                    a = a + 1
                    score = score + 1
            else:
                score = 0
                question = 1
                page_no = 7
                a = 0
        if 7 <= page_no <= 8:
            if event.type == MOUSEBUTTONUP: #if mouse clicked
                page_no = page_no + 1     

        if page_no == 9:
            if score < 5:
                if level2_questions_method() == False:
                    question = numer_list[a]
                    a = a + 1
                    life = life - 1
                    if life == 0:
                        page_no = 99
                if level2_questions_method() == True:
                    question = numer_list[a]
                    a = a + 1
                    score = score + 1
            else:
                score = 0
                question = 1
                page_no = page_no + 1
                a = 0
        if 10 <= page_no <= 11:
                if event.type == MOUSEBUTTONUP: #if mouse clicked
                    page_no = page_no + 1    

        if page_no == 12:
            if score < 5:
                if level3_questions_method() == False:
                    question = numer_list[a]
                    a = a + 1
                    life = life - 1
                    if life == 0:
                        page_no = 99
                if level3_questions_method() == True:
                    question = numer_list[a]
                    a = a + 1
                    score = score + 1
            else:
                score = 0
                question = 1
                page_no = page_no + 1 
                a = 0
        
        if page_no == 13:        
            if complete() == True:
                page_no = 4
                question = 1
                score = 0
                life = 3
                change = 1
            elif complete() == False:
                page_no = -1
                question = 1
                score = 0
                life = 3
                change = 1
       
        if life == 0:        
            if fail() == True:
                page_no = 4
                question = 1
                score = 0
                life = 3
                change = 1
                a = 0
            elif fail() == False:
                page_no = -1
                question = 1
                score = 0
                life = 3
                change = 1
                a = 0

        if event.type == MOUSEBUTTONUP: #if mouse clicked
            print(page_no, question, life, score,change)

        end()            
    
  
    
    pygame.display.update()
             
pygame.quit()
