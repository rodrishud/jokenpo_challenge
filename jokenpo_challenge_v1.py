import pygame
from random import randint


class Button:
    def __init__(self, image, position):
        self.image = image
        self.rect = image.get_rect(topleft=position)

    def render(self, screen):
        screen.blit(self.image, self.rect)


def events():
    global menu_selection, choice, ready, game_over
    global paper_button, rock_button, sci_button, buttonSound

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                if menu_selection == 200:
                    menu_selection = 200
                else:
                    menu_selection += 1
            if event.key == pygame.K_UP:
                if menu_selection == 200:
                    menu_selection = 200
                else:    
                    menu_selection -= 1
            if event.key == pygame.K_RETURN:
                menu_selection += 10
            if event.key == pygame.K_ESCAPE and 0 < menu_selection < 5:
                pygame.quit()
            if event.key == pygame.K_SPACE and menu_selection == 100 and game_over == True:
                menu_selection = 1
    
        if event.type == pygame.MOUSEBUTTONDOWN:
            if paper_button.rect.collidepoint(event.pos):
                if ready == False:
                    buttonSound.play()
                choice = 1
            if rock_button.rect.collidepoint(event.pos):
                if ready == False:
                    buttonSound.play()
                choice = 2
            if sci_button.rect.collidepoint(event.pos):
                if ready == False:
                    buttonSound.play()
                choice = 3
            if choice != 0:
                if readyOff_button.rect.collidepoint(event.pos):
                    ready = True


def selection():
    global menu_selection, font, choice, ready, comp, game_over, lock, start
    global white, black, red, green, blue, yellow

    font = pygame.font.SysFont("Retro Computer", 20, False, False)

#   ---- main menu ----

    if menu_selection < 1:
        menu_selection = 1

    if menu_selection == 1:     #quick game
        # variables need to reset here
        ready = False
        game_over = False
        comp = 0
        choice = 0

        screen.blit(BACKGROUND, (0, 0))

        quick_game = font.render("> Quick Game <", True, white)
        screen.blit(quick_game, ((SCREEN_WIDTH/2)-105, (SCREEN_HEIGHT/2)))

        about = font.render("About", True, white)
        screen.blit(about, ((SCREEN_WIDTH/2)-47, (SCREEN_HEIGHT/2)+30))

        exit = font.render("Exit", True, white)
        screen.blit(exit, ((SCREEN_WIDTH/2)-40, (SCREEN_HEIGHT/2)+60))

    if menu_selection == 2:     #about
        
        screen.blit(BACKGROUND, (0, 0))

        quick_game = font.render("Quick Game", True, white)
        screen.blit(quick_game, ((SCREEN_WIDTH/2)-87, (SCREEN_HEIGHT/2)))

        about = font.render("> About <", True, white)
        screen.blit(about, ((SCREEN_WIDTH/2)-65, (SCREEN_HEIGHT/2)+30))

        exit = font.render("Exit", True, white)
        screen.blit(exit, ((SCREEN_WIDTH/2)-40, (SCREEN_HEIGHT/2)+60))

    if menu_selection == 3:     #exit
        
        screen.blit(BACKGROUND, (0, 0))

        quick_game = font.render("Quick Game", True, white)
        screen.blit(quick_game, ((SCREEN_WIDTH/2)-87, (SCREEN_HEIGHT/2)))

        about = font.render("About", True, white)
        screen.blit(about, ((SCREEN_WIDTH/2)-47, (SCREEN_HEIGHT/2)+30))

        exit = font.render("> Exit <", True, white)
        screen.blit(exit, ((SCREEN_WIDTH/2)-58, (SCREEN_HEIGHT/2)+60))

    if menu_selection == 4:
       menu_selection = 3
 
 
#   ---- bridges ----
    if menu_selection == 11:        #to quick game
        choice = 0
        lock = 0
        comp = randint(1, 3)
        menu_selection = 100

    if menu_selection == 12:        #to about
        menu_selection = 200
    
    if menu_selection == 13:        #to quit
        pygame.quit()


#   ---- game modes ----
    if menu_selection == 100:       # -- QUICK GAME -- 
        quick_screen_false()

        if ready == True:
                if lock != choice:
                    choice = lock

        if choice == 1:         #you chose PAPER
            lock = choice
            
            if comp == 1:       # comp chose PAPER
                quick_screen_true_noChoice(PAPER)
                if ready == True:
                    quick_screen_true_ok(PAPER, PAPER)
                    print_draw("DRAW", yellow)
            
            if comp == 2:       #comp chose ROCK
                quick_screen_true_noChoice(PAPER)
                if ready == True:
                    quick_screen_true_ok(PAPER, ROCK)
                    print_won("YOU WON!", green)
           
            if comp == 3:       #comp chose SCISSORS
                quick_screen_true_noChoice(PAPER)
                if ready == True:
                    quick_screen_true_ok(PAPER, SCISSORS)
                    print_lost("YOU LOST!", red)
                    
            game_over = True
                
        if choice == 2:         #you chose ROCK
            lock = choice
            
            if comp == 1:       #comp chose PAPER
                quick_screen_true_noChoice(ROCK)
                if ready == True:
                    quick_screen_true_ok(ROCK, PAPER)
                    print_lost("YOU LOST!", red)

            if comp == 2:       #comp chose ROCK
                quick_screen_true_noChoice(ROCK)
                if ready == True:
                    quick_screen_true_ok(ROCK, ROCK)
                    print_draw('DRAW', yellow)     
           
            if comp == 3:       #comp chose SCISSORS
                quick_screen_true_noChoice(ROCK)
                if ready == True:
                    quick_screen_true_ok(ROCK, SCISSORS)
                    print_won('YOU WON!', green)
            
            game_over = True

        if choice == 3:         #you chose SCISSORS
            lock = choice
            
            if comp == 1:       #comp chose PAPER
                quick_screen_true_noChoice(SCISSORS)
                if ready == True:
                    quick_screen_true_ok(SCISSORS, PAPER)
                    print_won("YOU WON!", green)

            if comp == 2:       #comp chose ROCK
                quick_screen_true_noChoice(SCISSORS)
                if ready == True:
                    quick_screen_true_ok(SCISSORS, ROCK)
                    print_lost("YOU LOST!", red)

            if comp == 3:       #comp chose SCISSORS
                quick_screen_true_noChoice(SCISSORS)
                if ready == True:
                    quick_screen_true_ok(SCISSORS, SCISSORS)
                    print_draw("DRAW", yellow)

            game_over = True
              
    if menu_selection == 200:       # -- ABOUT --

        screen.fill(black)

        font = pygame.font.SysFont("Retro Computer", 14, False, False)
        created = font.render("-- Created by Rodrigo Formigon, Heavy Games --", True, (white))
        version = font.render("-- Version 1.0 --", True, (white))
        
        font = pygame.font.SysFont("Retro Computer", 20, False, False)
        back = font.render("> back <", True, (white))

        screen.blit(created, (160, (SCREEN_HEIGHT/2)+30))
        screen.blit(version, ((SCREEN_WIDTH/2)-70, (SCREEN_HEIGHT/2)+60))
        screen.blit(back, ((SCREEN_WIDTH/2)-45, (SCREEN_HEIGHT/2)+120))


#   ---- callbacks ----
    if menu_selection == 210:       #back to main menu >about<
        menu_selection = 2



def loading_screen_init():
    screen.blit(LOADING, (0,0))
    pygame.display.update()

    pygame.time.wait(800)
    pygame.mixer.music.play(-1)
    pygame.time.wait(800)


def quick_screen_false():
    screen.blit(INGAME, (0, 0))
    font = pygame.font.SysFont("Retro Computer", 16, False, False)

    paper_button.render(screen)
    rock_button.render(screen)
    sci_button.render(screen)
    readyOff_button.render(screen)

    you = font.render("YOU: ___", True, (white))
    screen.blit(you, ((SCREEN_WIDTH/2)-140, SCREEN_HEIGHT-400))

    computer = font.render("___ :COMPUTER", True, (white))
    screen.blit(computer, ((SCREEN_WIDTH/2)+50, SCREEN_HEIGHT-400))

def quick_screen_true_noChoice(choice):
    screen.blit(INGAME, (0, 0))
    font = pygame.font.SysFont("Retro Computer", 16, False, False)

    paper_button.render(screen)
    rock_button.render(screen)
    sci_button.render(screen)

    readyOff_button.render(screen)

    you = font.render("YOU: ", True, (white))
    screen.blit(you, ((SCREEN_WIDTH/2)-140, SCREEN_HEIGHT-400))
    screen.blit(pygame.transform.scale(choice, (40,40)), (310, 188))

    computer = font.render("___ :COMPUTER", True, (white))
    screen.blit(computer, ((SCREEN_WIDTH/2)+50, SCREEN_HEIGHT-400))

def quick_screen_true_ok(yourMove, compMove):
    screen.blit(INGAME, (0, 0))

    paper_button.render(screen)
    rock_button.render(screen)
    sci_button.render(screen)
    readyOn_button.render(screen)

    font = pygame.font.SysFont("Retro Computer", 16, False, False)

    you = font.render("YOU: ", True, (white))
    screen.blit(you, ((SCREEN_WIDTH/2)-140, SCREEN_HEIGHT-400))
    screen.blit(pygame.transform.scale(yourMove, (40,40)), (310, 188))

    computer = font.render(" :COMPUTER", True, (white))
    screen.blit(computer, ((SCREEN_WIDTH/2)+92, SCREEN_HEIGHT-400))
    screen.blit(pygame.transform.scale(compMove, (40,40)), (450, 188))
    
    again = font.render('Press "space" to main menu', True, (white))
    screen.blit(again, (249,150))

def print_won(result, color):
    font = pygame.font.SysFont("Retro Computer", 40, False, False)
    youWon = font.render(result, True, color)
    screen.blit(youWon, (290, 80))

def print_lost(result, color):
    font = pygame.font.SysFont("Retro Computer", 40, False, False)
    youLost = font.render(result, True, color)
    screen.blit(youLost, (272, 80))

def print_draw(result, color):
    font = pygame.font.SysFont("Retro Computer", 40, False, False)
    draw = font.render(result, True, color)
    screen.blit(draw, (333, 80))


#variaveis
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 30

paper_x = 120
paper_y = 390

rock_x = 350
rock_y = 400

sci_x = 580
sci_y = 390

menu_selection = 1
game_over = False
ready = False
comp = 0
lock = 0
choice = 0

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
yellow = (255,255,0)



pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('JOKENPO CHALLENGE')

font = pygame.font.SysFont("Retro Computer", 20, False, False)


#images
BACKGROUND = pygame.image.load('images/background.png')
INGAME = pygame.image.load('images/ingame.png')
LOADING = pygame.image.load('images/loading.png')

PAPER = pygame.image.load('images/paper.png').convert_alpha()
ROCK = pygame.image.load('images/rock.png').convert_alpha()
SCISSORS = pygame.image.load('images/scissors.png').convert_alpha()

READY = [
    pygame.image.load('images/ready1.png').convert_alpha(), 
    pygame.image.load('images/ready2.png').convert_alpha()
]


#sounds
buttonSound = pygame.mixer.Sound('sounds/click.wav')

macintoshPlus = pygame.mixer.music.load('sounds/macintosh_plus_trapmix.mp3')


#buttons:
paper_button = Button(PAPER, (paper_x, paper_y))    #1
rock_button = Button(ROCK, (rock_x, rock_y))        #2
sci_button = Button(SCISSORS, (sci_x, sci_y))       #3

readyOff_button = Button(pygame.transform.scale(READY[0], (70,30)), (366, 350))
readyOn_button = Button(pygame.transform.scale(READY[1], (70,30)), (366, 350))


# MAIN ------------------------------------------------------------------------------        
loading_screen_init()

while True:
    clock.tick(FPS)
    
    events()
    selection()

    if menu_selection == 200:
        pygame.mixer.music.set_volume(0.1)
    else:
        pygame.mixer.music.set_volume(0.3)
        
    pygame.display.update()

pygame.quit()
