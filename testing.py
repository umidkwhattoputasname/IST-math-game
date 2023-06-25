import pygame
import os
pygame.init()

WIDTH, HEIGHT = 900, 500                                    #Defining window size
WIN = pygame.display.set_mode((WIDTH, HEIGHT))              #Hey, lets start a game with this size and height
pygame.display.set_caption("Ta-math-gotchi game!!")         #Naming our game

TAMAGOTCHI_RIGHTANSWER = pygame.image.load('Images/Tamagotchihappy.png')
TAMAGOTCHI = pygame.image.load('Images/Tamagotchi.png')
TAMAGOTCHI_WRONGANSWER = pygame.image.load(os.path.join('Images', 'Tamagotchihurt.png'))
TAMAGOTCHI_DEAD = pygame.image.load(os.path.join('Images', 'Tamagotchided.png'))

def draw_window():
    WIN.fill((255,255,255))                               #white bg 
    WIN.blit(TAMAGOTCHI, (200,150))
    pygame.display.update()                               #update   

FPS = 60                                                        #Frames per second

def main():                                                 #Mainframe here
    clock = pygame.time.Clock()
    run = True                                              #keeps the game running until we tell it to stop
    while run:                                              #while the game is on do the following

        clock.tick(FPS)                                     #capping the frame rate at 60 per second
        draw_window()
        for event in pygame.event.get ():                   
            if event.type == pygame.QUIT:                   #check if user quit game
                run = False                                 #if user quit program, stop run
    
   

    

if __name__ == "__main__":                                  #buffer
    main()

pygame.quit()



