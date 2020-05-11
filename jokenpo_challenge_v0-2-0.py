# >MOUSEMOTION IMPLEMENTADO
# >BACK_BUTTON IMPLEMENTADO EM ABOUT
# >SELEÇÃO DE PERSONAGENS IMPLEMENTADA
# >ANIMAÇÃO COM 2 PERSONAGENS
# >simulação de loading reduzida

import os, sys

dirpath = os.getcwd()
sys.path.append(dirpath)

if getattr(sys, "frozen", False):
    os.chdir(sys._MEIPASS)

## ---------------------------------------


import pygame
from random import randint


# classes:
class Button:
    def __init__(self, image, position):
        self.image = image
        self.rect = image.get_rect(topleft=position)

    def render(self, screen):
        screen.blit(self.image, self.rect)


class Player(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        
        global charSelection

        self.current_sprite = 0

        self.character = []

        self.char1 = []
        self.char1.append(pygame.transform.scale2x(pygame.image.load('data/char1idle1.png')))     #[0]
        self.char1.append(pygame.transform.scale2x(pygame.image.load('data/char1idle2.png')))     #[1]
        self.char1.append(pygame.transform.scale2x(pygame.image.load('data/char1paper.png')))     #[2]
        self.char1.append(pygame.transform.scale2x(pygame.image.load('data/char1rock.png')))      #[3]
        self.char1.append(pygame.transform.scale2x(pygame.image.load('data/char1sci.png')))       #[4]
        
        self.motoboy_sprites = []
        self.motoboy_sprites.append(pygame.transform.scale2x(pygame.image.load('data/moto_idle_1.png')))     #[0]
        self.motoboy_sprites.append(pygame.transform.scale2x(pygame.image.load('data/moto_idle_2.png')))     #[1]
        self.motoboy_sprites.append(pygame.transform.scale2x(pygame.image.load('data/moto_paper.png')))      #[2]
        self.motoboy_sprites.append(pygame.transform.scale2x(pygame.image.load('data/moto_rock.png')))       #[3]
        self.motoboy_sprites.append(pygame.transform.scale2x(pygame.image.load('data/moto_sci.png')))        #[4]



        self.character.append(self.char1)               #[0]
        self.character.append(self.motoboy_sprites)     #[1]

        self.image = self.character[charSelection][self.current_sprite]

        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x, pos_y]

    def update(self):
        global choice, ready, charSelection

        atual = charSelection
        self.current_sprite += 0.2

        if choice == 0 or ready == False:
            if self.current_sprite >= 2:
                self.current_sprite = 0
            self.image = self.character[charSelection][int(self.current_sprite)]
        if choice != 0 and ready == True:
            if choice == 1:
                self.image = self.character[charSelection][2]
            if choice == 2:
                self.image = self.character[charSelection][3]
            if choice == 3:
                self.image = self.character[charSelection][4]

        elif charSelection != atual:
            current_sprite = 0


class Computer(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.sprites = []
        self.sprites.append(pygame.transform.flip(pygame.transform.scale2x(pygame.image.load('data/char1idle1.png')), True, False))
        self.sprites.append(pygame.transform.flip(pygame.transform.scale2x(pygame.image.load('data/char1idle2.png')), True, False))
        self.sprites.append(pygame.transform.flip(pygame.transform.scale2x(pygame.image.load('data/char1paper.png')), True, False))
        self.sprites.append(pygame.transform.flip(pygame.transform.scale2x(pygame.image.load('data/char1rock.png')), True, False))
        self.sprites.append(pygame.transform.flip(pygame.transform.scale2x(pygame.image.load('data/char1sci.png')), True, False))
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]

        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x, pos_y]

    def update(self):
        global comp, ready

        self.current_sprite += 0.2

        if ready == False:
            if self.current_sprite >= 2:
                self.current_sprite = 0
            self.image = self.sprites[int(self.current_sprite)]
        if ready == True:
            if comp == 1:
                self.image = self.sprites[2]
            if comp == 2:
                self.image = self.sprites[3]
            if comp == 3:
                self.image = self.sprites[4]


# main functions
def events():
    global menuSelection, gameOver, charSelection, choice, ready
    global paper_button, rock_button, sci_button, back_button, buttonSound

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                if menuSelection == 200:
                    menuSelection = 200
                else:
                    menuSelection += 1
            elif event.key == pygame.K_UP:
                if menuSelection == 200:
                    menuSelection = 200
                else:
                    menuSelection -= 1
            elif event.key == pygame.K_RETURN:
                menuSelection += 10
            elif event.key == pygame.K_ESCAPE and 0 < menuSelection < 5:
                sys.exit()
            elif event.key == pygame.K_SPACE and menuSelection == 100 and gameOver == True:
                menuSelection = 1
            
            elif menuSelection < 5:
                if event.key == pygame.K_RIGHT:
                    if charSelection >= 1:
                        charSelection = 1
                    else:
                        charSelection += 1
                elif event.key == pygame.K_LEFT:
                    if charSelection <= 0:
                        charSelection == 0
                    else:
                        charSelection -= 1


            
        elif event.type == pygame.MOUSEBUTTONDOWN:            
            if menuSelection < 10:
                if quick2_button.rect.collidepoint(event.pos) or about2_button.rect.collidepoint(event.pos) or exit2_button.rect.collidepoint(event.pos):
                    menuSelection += 10
            elif menuSelection == 100:
                if ready == False:
                    if paper_button.rect.collidepoint(event.pos):
                        buttonSound.play()
                        choice = 1
                    elif rock_button.rect.collidepoint(event.pos):
                        buttonSound.play()
                        choice = 2
                    elif sci_button.rect.collidepoint(event.pos):
                        buttonSound.play()
                        choice = 3
                    elif readyOff_button.rect.collidepoint(event.pos):
                        if choice != 0:
                            ready = True
            elif menuSelection == 200:
                if back_button.rect.collidepoint(event.pos):
                    menuSelection += 10

        elif event.type == pygame.MOUSEMOTION:
            if menuSelection < 10:
                if quick1_button.rect.collidepoint(event.pos):
                    menuSelection = 1
                if about1_button.rect.collidepoint(event.pos):
                    menuSelection = 2
                if exit1_button.rect.collidepoint(event.pos):
                    menuSelection = 3

        
def main_menu():
    global menuSelection, gameOver, font, choice, ready, comp, lock
    global white, black, red, green, blue, yellow

    font = pygame.font.SysFont("Retro Computer", 20, False, False)

    # ---- main menu ----
    if menuSelection < 1:
        menuSelection = 1

    if menuSelection == 1:  # quick game
        music.set_volume(0.3)

        # variables need to reset here
        charSelection = 0
        gameOver = False
        ready = False
        comp = 0
        choice = 0

        screen.blit(BACKGROUND, (0, 0))
        quick2_button.render(screen)
        about1_button.render(screen)
        exit1_button.render(screen)
        

    if menuSelection == 2:  # about
        screen.blit(BACKGROUND, (0, 0))
        quick1_button.render(screen)
        about2_button.render(screen)
        exit1_button.render(screen)
        pygame.display.update()

    if menuSelection == 3:  # exit   
        screen.blit(BACKGROUND, (0, 0))
        quick1_button.render(screen)
        about1_button.render(screen)
        exit2_button.render(screen)
    
    if menuSelection == 4:
        menuSelection = 3
    
    CHAR_SELECTION_GROUP.draw(screen)
    CHAR_SELECTION_GROUP.update()


    #   ---- bridges ----
    if menuSelection == 11:  # to quick game
        choice = 0
        lock = 0
        comp = randint(1, 3)
        ready = False
        menuSelection = 100

    if menuSelection == 12:  # to about
        menuSelection = 200

    if menuSelection == 13:  # to quit
        sys.exit()

    #   ---- game modes ----
    if menuSelection == 100:       # -- QUICK GAME --
        quick_game()

        PLAYER_GROUP.draw(screen)
        COMP_GROUP.draw(screen)
        PLAYER_GROUP.update()
        COMP_GROUP.update()
        
    if menuSelection == 200:       # -- ABOUT --
        music.set_volume(0.1)
        
        screen.fill(black)

        font = pygame.font.SysFont("Retro Computer", 14, False, False)
        created = font.render("-- Created by Rodrigo Formigon, Heavy Games --", True, white)
        version = font.render("-- Version 0.2.0 --", True, white)

        screen.blit(created, (160, 330))
        screen.blit(version, (320, 360))
        back_button.render(screen)   

    #   ---- callbacks ----
    if menuSelection == 210:  # back to main menu >about<
        menuSelection = 2
    

def loading_screen_init():
    screen.blit(LOADING, (0, 0))
    pygame.display.update()

    pygame.time.wait(500)
    music.play(-1)
    music.set_volume(0.3)

   
def quick_game():
    global menuSelection, gameOver, font, choice, ready, comp, lock
    global white, black, red, green, blue, yellow
    
    quick_screen_false()
    
    if ready == True:
        if lock != choice:
            choice = lock

    if choice == 1:  # you chose PAPER
        lock = choice

        if comp == 1:       # comp chose PAPER
            quick_screen_true_notReady(PAPER)
            if ready == True:
                quick_screen_true_ok(PAPER, PAPER)
                print_draw()
                gameOver = True

        if comp == 2:  # comp chose ROCK
            quick_screen_true_notReady(PAPER)
            if ready == True:
                quick_screen_true_ok(PAPER, ROCK)
                print_won()
                gameOver = True

        if comp == 3:  # comp chose SCISSORS
            quick_screen_true_notReady(PAPER)
            if ready == True:
                quick_screen_true_ok(PAPER, SCISSORS)
                print_lost()
                gameOver = True

    if choice == 2:  # you chose ROCK
        lock = choice

        if comp == 1:  # comp chose PAPER
            quick_screen_true_notReady(ROCK)
            if ready == True:
                quick_screen_true_ok(ROCK, PAPER)
                print_lost()
                gameOver = True
        if comp == 2:  # comp chose ROCK
            quick_screen_true_notReady(ROCK)
            if ready == True:
                quick_screen_true_ok(ROCK, ROCK)
                print_draw()
                gameOver = True
        if comp == 3:  # comp chose SCISSORS
            quick_screen_true_notReady(ROCK)
            if ready == True:
                quick_screen_true_ok(ROCK, SCISSORS)
                print_won()
                gameOver = True

    if choice == 3:  # you chose SCISSORS
        lock = choice

        if comp == 1:  # comp chose PAPER
            quick_screen_true_notReady(SCISSORS)
            if ready == True:
                quick_screen_true_ok(SCISSORS, PAPER)
                print_won()
                gameOver = True
        if comp == 2:  # comp chose ROCK
            quick_screen_true_notReady(SCISSORS)
            if ready == True:
                quick_screen_true_ok(SCISSORS, ROCK)
                print_lost()
                gameOver = True
        if comp == 3:  # comp chose SCISSORS
            quick_screen_true_notReady(SCISSORS)
            if ready == True:
                quick_screen_true_ok(SCISSORS, SCISSORS)
                print_draw()
                gameOver = True
    

def quick_screen_false():    
    screen.blit(INGAME, (0, 0))

    font = pygame.font.SysFont("Retro Computer", 16, False, False)

    paper_button.render(screen)
    rock_button.render(screen)
    sci_button.render(screen)
    readyOff_button.render(screen)

    you = font.render("YOU: ___", True, (white))
    screen.blit(you, (260, 200))

    computer = font.render("___ :COMPUTER", True, (white))
    screen.blit(computer, (450, 200))

def quick_screen_true_notReady(yourMove):
    screen.blit(INGAME, (0, 0))
    font = pygame.font.SysFont("Retro Computer", 16, False, False)

    paper_button.render(screen)
    rock_button.render(screen)
    sci_button.render(screen)

    readyOff_button.render(screen)

    you = font.render("YOU: ", True, (white))
    screen.blit(you, (260, 200))
    screen.blit(pygame.transform.scale(yourMove, (40, 40)), (310, 188))

    computer = font.render("___ :COMPUTER", True, (white))
    screen.blit(computer, (450, 200))

def quick_screen_true_ok(yourMove, compMove):
    screen.blit(INGAME, (0, 0))

    paper_button.render(screen)
    rock_button.render(screen)
    sci_button.render(screen)
    readyOn_button.render(screen)

    font = pygame.font.SysFont("Retro Computer", 16, False, False)

    you = font.render("YOU: ", True, (white))
    screen.blit(you, (260, 200))
    screen.blit(pygame.transform.scale(yourMove, (40, 40)), (310, 188))

    computer = font.render(" :COMPUTER", True, (white))
    screen.blit(computer, (492, 200))
    screen.blit(pygame.transform.scale(compMove, (40, 40)), (450, 188))

    again = font.render('Press "space" to main menu', True, (white))
    screen.blit(again, (249, 150))


def print_won():
    font = pygame.font.SysFont("Retro Computer", 40, False, False)
    youWon = font.render("YOU WON!", True, green)
    screen.blit(youWon, (290, 80))

def print_lost():
    font = pygame.font.SysFont("Retro Computer", 40, False, False)
    youLost = font.render("YOU LOST!", True, red)
    screen.blit(youLost, (272, 80))

def print_draw():
    font = pygame.font.SysFont("Retro Computer", 40, False, False)
    draw = font.render("DRAW", True, yellow)
    screen.blit(draw, (333, 80))


# variaveis
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 30

menuSelection = 1
gameOver = False
charSelection = 0
ready = False
comp = 0
lock = 0
choice = 0

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)

os.environ['SDL_VIDEO_CENTERED'] = '1'

pygame.init()
pygame.mixer.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('JOKENPO CHALLENGE')

font = pygame.font.SysFont("Retro Computer", 20, False, False)


# images
BACKGROUND = pygame.image.load('data/background.png')
INGAME = pygame.image.load('data/ingame.png')
LOADING = pygame.image.load('data/loading.png')

PAPER = pygame.image.load('data/paper.png').convert_alpha()
ROCK = pygame.image.load('data/rock.png').convert_alpha()
SCISSORS = pygame.image.load('data/scissors.png').convert_alpha()

READY = [
    pygame.image.load('data/ready1.png').convert_alpha(),
    pygame.image.load('data/ready2.png').convert_alpha()
]

QUICK1 = font.render("Quick Game", True, white)
QUICK2 = font.render("> Quick Game <", True, white)

ABOUT1 = font.render("About", True, white)
ABOUT2 = font.render("> About <", True, white)

EXIT1 = font.render("Exit", True, white)
EXIT2 = font.render("> Exit <", True, white)

BACK = font.render("> back <", True, white)



# sounds
music = pygame.mixer.Sound('data/music.wav')
buttonSound = pygame.mixer.Sound('data/click.wav')

# buttons:
quick1_button = Button(QUICK1, (313, 300))
quick2_button = Button(QUICK2, (295, 300))
about1_button = Button(ABOUT1, (353,330))
about2_button = Button(ABOUT2, (335, 330))
exit1_button = Button(EXIT1, (362, 360))
exit2_button = Button(EXIT2, (344, 360))
back_button = Button(BACK, (355, 420))

paper_button = Button(PAPER, (120, 440))    # 1
rock_button = Button(ROCK, (350, 450))      # 2
sci_button = Button(SCISSORS, (580, 440))   # 3

readyOff_button = Button(pygame.transform.scale(READY[0], (70, 30)), (366, 400))
readyOn_button = Button(pygame.transform.scale(READY[1], (70, 30)), (366, 400))


# sprites:
CHAR_SELECTION_GROUP = pygame.sprite.Group()
char_selection = Player(200, 260)
CHAR_SELECTION_GROUP.add(char_selection)

PLAYER_GROUP = pygame.sprite.Group()
player = Player(260, 260)
PLAYER_GROUP.add(player)

COMP_GROUP = pygame.sprite.Group()
computer = Computer(458, 260)
COMP_GROUP.add(computer)



# MAIN ------------------------------------------------------------------------------
loading_screen_init()

while True:
    clock.tick(FPS)

    main_menu()
    
    events()

    pygame.display.update()

pygame.quit()
sys.exit()
