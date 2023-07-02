import os
import sys
import pygame
from pygame import MOUSEBUTTONDOWN,MOUSEBUTTONUP,QUIT
import random
import pickle
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

def end(): #end program if window closed
    global running
    if event.type == QUIT:
        running = False

def infopages(): #formatting for first few pages and instructions
    startfont = pygame.font.Font('Style/minecraft_font.ttf',16)  #font, size
    start = startfont.render('New Game', True, test)  #text, smth, text colour, box colour
    continuing = startfont.render('Continue Game', True, test)  #text, smth, text colour, box colour
    infofont = pygame.font.Font('Style/minecraft_font.ttf',32)
    instructions = "You have 3 lives"
    info = infofont.render(instructions, True, test)
    infoRect = info.get_rect()
    infoRect.center = (X//2,Y//2)
    if page_no == -1:
        pygame.draw.rect(window, test, pygame.Rect(400,212,200,40), 3,3) #screen, colour, position[x,y,width,height], fill/border, corners
        window.blit(start,(458,220))
        window.blit(text, textRect)         #Text/title
        if os.path.exists("variables.pkl"):
            pygame.draw.rect(window, test, pygame.Rect(400,300,200,40), 3,3) #screen, colour, position[x,y,width,height], fill/border, corners
            window.blit(continuing,(432,308))
            window.blit(text, textRect)         #Text/title

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

def fail(): #screen when you fail
    font = pygame.font.Font('Style/minecraft_font.ttf',40)  #font, size
    text = font.render('Your pet died!', True, test)  #text, smth, text colour, box colour
    textRect = text.get_rect()
    textRect.center = (X//2,Y//3)

    pygame.draw.rect(window, test, pygame.Rect(170,250,200,50), 4,3) #screen, colour, position[x,y,width,height], fill/border, corners
    answer1 = answer_font.render ('Try Again', True, test)
    window.blit(answer1,(215,260))
    pygame.draw.rect(window, test, pygame.Rect(395,250,200,50), 4,3) #screen, colour, position[x,y,width,height], fill/border, corners
    answer2 = answer_font.render ('Main Menu', True, test)
    window.blit(answer2,(440,260))
    pygame.draw.rect(window, test, pygame.Rect(620,250,200,50), 4,3) #screen, colour, position[x,y,width,height], fill/border, corners
    answer3 = answer_font.render ('Quit', True, test)
    window.blit(answer3,(700,260))

    window.blit(text,textRect)
    sprite()
    if life == 0: 
        if event.type == MOUSEBUTTONDOWN:   #each button returns/does different things
            mouse = pygame.mouse.get_pos()
            if 170 <= mouse[0] <= 370 and 250 <= mouse[1] <= 300:
                return True
            if 395 <= mouse[0] <= 595 and 250 <= mouse[1] <= 300:
                return False
            if 620 <= mouse[0] <= 820 and 250 <= mouse[1] <= 300:
                save_variable_values()  
                pygame.quit()
                sys.exit()

def complete(): #screen when you complete it, similar formatting as fail screen
    congrats_font = pygame.font.Font('Style/minecraft_font.ttf',40)  #font, size
    text = congrats_font.render('Congratulations!', True, test)  #text, smth, text colour, box colour
    textRect = text.get_rect()
    textRect.center = (X//2,Y//4)

    pygame.draw.rect(window, test, pygame.Rect(170,250,200,50), 4,3) #screen, colour, position[x,y,width,height], fill/border, corners
    answer1 = answer_font.render ('Play Again', True, test)
    window.blit(answer1,(210,260))
    pygame.draw.rect(window, test, pygame.Rect(395,250,200,50), 4,3) #screen, colour, position[x,y,width,height], fill/border, corners
    answer2 = answer_font.render ('Main Menu', True, test)
    window.blit(answer2,(440,260))
    pygame.draw.rect(window, test, pygame.Rect(620,250,200,50), 4,3) #screen, colour, position[x,y,width,height], fill/border, corners
    answer3 = answer_font.render ('Quit', True, test)
    window.blit(answer3,(700,260))

    window.blit(text,textRect)
    sprite()
    if page_no == 13:
        if event.type == MOUSEBUTTONDOWN:
            mouse = pygame.mouse.get_pos()
            if 170 <= mouse[0] <= 370 and 250 <= mouse[1] <= 300:
                return True
            if 395 <= mouse[0] <= 595 and 250 <= mouse[1] <= 300:
                return False
            if 620 <= mouse[0] <= 820 and 250 <= mouse[1] <= 300:
                save_variable_values()  
                pygame.quit()
                sys.exit()

#formating for each question
#each question has same formatting just different questions and answers
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

def level1_questions_method(run = True):          #if answer is correct then return true else false
    if run:   
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

def level1():   #display level screen and run the method for the questions
    level_font = pygame.font.Font('Style/minecraft_font.ttf',48)
    level_text = "Level 1"
    level = level_font.render(level_text, True, test)
    levelRect = level.get_rect()
    levelRect.center = (X//2,Y//2)
    if page_no == 5:
        window.blit(level,levelRect)
    if page_no == 6:
        level1_questions_method(run = True)


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

def level2_questions_method(run = True):          #same as other ones
    if run:
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

def level2(): #same as other ones
    level_font = pygame.font.Font('Style/minecraft_font.ttf',48)
    level_text = "Level 2"
    level = level_font.render(level_text, True, test)
    levelRect = level.get_rect()
    levelRect.center = (X//2,Y//2)
    if page_no == 8:
        window.blit(level,levelRect)
    if page_no == 9:
        level2_questions_method(run = True)


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

def level3_questions_method(run = True):          #same as other ones
    if run:
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

def level3(): #same as other ones
    level_font = pygame.font.Font('Style/minecraft_font.ttf',48)
    level_text = "Level 3"
    level = level_font.render(level_text, True, test)
    levelRect = level.get_rect()
    levelRect.center = (X//2,Y//2)
    if page_no == 11:
        window.blit(level,levelRect)
    if page_no == 12:
        level3_questions_method(run = True)

def sprite(): #posiitioning for hearts, sprite and score
    font = pygame.font.Font('Style/minecraft_font.ttf',24)  #font, size
    if page_no != 13 and page_no != 99: #don't display score on death and completion screens
        if page_no == 6:   
            text = f"Level 1 :  {score +1}/5"
        if page_no == 9:
            text = f"Level 2 :  {score +1}/5"
        if page_no == 12:
            text = f"Level 3 :  {score +1}/5"
        text = font.render(text, True, test)  #text, smth, text colour, box colour
        textRect = text.get_rect()
        textRect.center = (730,40)
        window.blit (text,textRect)
    if page_no !=13:
        if sprite_no == 1:  #sprite for first question
            window.blit(normal,postion_sprite)
        if sprite_no == 2:  #if correct then sprite is happy
            window.blit(happy,postion_sprite)
        if sprite_no == 3:  #if wrong sprite is dying
            window.blit(dying,postion_sprite)   
    else:
        window.blit(happy,postion_sprite)

    if life == 3:   #displaying amount of hearts depending on life left
        if page_no != 13:
            window.blit(heart1,postion_heart1)
            window.blit(heart2,postion_heart2)
            window.blit(heart3,postion_heart3)
    if life == 2:
        if page_no != 13:
            window.blit(heart1,postion_heart1)
            window.blit(heart2,postion_heart2)
    if life == 1:
        if page_no != 13:
            window.blit(heart1,postion_heart1)
    if life == 0:   #if died then pet dies
        window.blit(dead,postion_sprite)

def save_variable_values():
    """Save the values of variables to a file."""
    with open("variables.pkl", "wb") as f:
        pickle.dump([page_no, question, life, score, numer_list, all_questions, a, change, sprite_no], f)

def read_variable_values():
    """Read the values of variables from a file."""
    global variables
    with open("variables.pkl", "rb") as f:
        variables = pickle.load(f)





page_no = -1     #page number
question = 1    #starting question --> ends up being randomised for late questions

life = 3        #amount of lives
score = 0       #questions to complete --> 1/5 means first question to complete

numer_list = []     #randomised question list
all_questions = 0   #amount of numbers is numer_list
a = 0               #position in numer_list
change = 1          #variable for running randomised list once

sprite_no = 1       #costume for sprite, changes depending on right or wrong answer

#if os.path.exists("variables.pkl"): #if a file has been created use it if not use starting numbers



running = True  #loop variable
while running:
    mouse = pygame.mouse.get_pos()      #stores mouse position
    window.blit(bg_img,(0,0))           #background image

    if change == 1:     #generates a random list once until player dies or plays again
        numer_list.clear()
        all_questions = 0
        while all_questions < 7:
            question_no = random.randint(2,8)
            if question_no not in numer_list:   #makes it so the list does not contain repeating questions
                numer_list.append(question_no)
                all_questions = all_questions + 1
        change = 0 #stops generating list
    for event in pygame.event.get():  
        if page_no == -1:
            if event.type == MOUSEBUTTONUP:
                if 400 <= mouse[0] <= 600 and 212 <= mouse[1] <= 252:
                    page_no = page_no + 1
                if os.path.exists("variables.pkl"):
                    if 400 <= mouse[0] <= 600 and 300 <= mouse[1] <= 340:
                        read_variable_values()
                        page_no = variables[0] #400,330,200,40
                        question = variables[1]
                        life = variables[2]
                        score = variables[3]
                        numer_list = variables[4]
                        all_questions = variables[5]
                        a = variables[6]
                        change = variables[7]
                        sprite_no = variables[8]

        if 0 <= page_no <= 5:                #stops page turning after instructions
            if event.type == MOUSEBUTTONUP: #if mouse clicked
                page_no = page_no + 1
        
        if page_no == 6:    #level 1 question page
            if score < 5:   #loop until player pass
                if level1_questions_method() == False:  #answer is wrong
                    question = numer_list[a]    #question no. = random number in list
                    a = a + 1
                    life = life - 1
                    sprite_no = 3
                    if life == 0:
                        page_no = 99
                if level1_questions_method() == True:   #answer is correct
                    question = numer_list[a]
                    a = a + 1
                    score = score + 1
                    sprite_no = 2
            else:   #reset variables and change pages
                score = 0
                question = 1
                page_no = 7
                a = 0
                sprite_no = 1
        if 7 <= page_no <= 8:   #continue to next page (level 2 and questions)
            if event.type == MOUSEBUTTONUP: #if mouse clicked
                page_no = page_no + 1     

        if page_no == 9:    #level 2 questions same structure as level 1
            if score < 5:
                if level2_questions_method() == False:
                    question = numer_list[a]
                    a = a + 1
                    life = life - 1
                    sprite_no = 3
                    if life == 0:
                        page_no = 99
                if level2_questions_method() == True:
                    question = numer_list[a]
                    a = a + 1
                    score = score + 1
                    sprite_no = 2
            else:
                score = 0
                question = 1
                page_no = page_no + 1
                a = 0
                sprite_no = 1
        if 10 <= page_no <= 11:
                if event.type == MOUSEBUTTONUP: #if mouse clicked
                    page_no = page_no + 1    

        if page_no == 12:   #level 3
            if score < 5:
                if level3_questions_method() == False:
                    question = numer_list[a]
                    a = a + 1
                    life = life - 1
                    sprite_no = 3
                    if life == 0:
                        page_no = 99
                if level3_questions_method() == True:
                    question = numer_list[a]
                    a = a + 1
                    score = score + 1
                    sprite_no = 2
            else:
                score = 0
                question = 1
                page_no = page_no + 1 
                a = 0
        
        if page_no == 13:   #completion page      
            if complete() == True:  #reset variables and change page back to level 1
                page_no = 4
                question = 1
                score = 0
                life = 3
                change = 1  #generates another question list
                sprite_no = 1
            elif complete() == False:   #same thing but page goes to title page
                page_no = -1
                question = 1
                score = 0
                life = 3
                change = 1
                sprite_no = 1
            if os.path.exists("variables.pkl"):
                os.remove("variables.pkl")
        if life == 0:       #player failed
            if fail() == True:  #reset all variables and go straight to lvl 1
                page_no = 4
                question = 1
                score = 0
                life = 3
                change = 1
                a = 0
                sprite_no = 1
            elif fail() == False: #reset variable and go to home page
                page_no = -1
                question = 1
                score = 0
                life = 3
                change = 1
                a = 0
                sprite_no = 1
            if os.path.exists("variables.pkl"):
                os.remove("variables.pkl")
        if event.type == MOUSEBUTTONUP: #if mouse clicked
            print(page_no, question, life, score,change)
        end()            
    
    infopages()                             #change the page after first click
    level1()
    level2()
    level3()  

    pygame.display.update()
save_variable_values()  #save data before closing      
pygame.quit()
sys.exit()
