# >MENU INICIAL MODIFICADO
# >ANIMAÇÃO COM 3 PERSONAGENS
# >BOTÃO READY ACIONADO COM SPACEBAR
# >começo da implementação do modo BEST OF 3

# >simulação de loading reduzida
# MUSICA DESABILITADA

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

        self.naked_sprites = []
        self.naked_sprites.append(pygame.transform.scale2x(pygame.image.load('data/naked_idle_1.png')))     #[0]
        self.naked_sprites.append(pygame.transform.scale2x(pygame.image.load('data/naked_idle_2.png')))     #[1]
        self.naked_sprites.append(pygame.transform.scale2x(pygame.image.load('data/naked_paper.png')))      #[2]
        self.naked_sprites.append(pygame.transform.scale2x(pygame.image.load('data/naked_rock.png')))       #[3]
        self.naked_sprites.append(pygame.transform.scale2x(pygame.image.load('data/naked_sci.png')))        #[4]
        
        self.motoboy_sprites = []
        self.motoboy_sprites.append(pygame.transform.scale2x(pygame.image.load('data/moto_idle_1.png')))    #[0]
        self.motoboy_sprites.append(pygame.transform.scale2x(pygame.image.load('data/moto_idle_2.png')))    #[1]
        self.motoboy_sprites.append(pygame.transform.scale2x(pygame.image.load('data/moto_paper.png')))     #[2]
        self.motoboy_sprites.append(pygame.transform.scale2x(pygame.image.load('data/moto_rock.png')))      #[3]
        self.motoboy_sprites.append(pygame.transform.scale2x(pygame.image.load('data/moto_sci.png')))       #[4]

        self.funker_sprites = []
        self.funker_sprites.append(pygame.transform.scale2x(pygame.image.load('data/funker_idle_1.png')))   #[0]
        self.funker_sprites.append(pygame.transform.scale2x(pygame.image.load('data/funker_idle_2.png')))   #[1]
        self.funker_sprites.append(pygame.transform.scale2x(pygame.image.load('data/funker_paper.png')))    #[2]
        self.funker_sprites.append(pygame.transform.scale2x(pygame.image.load('data/funker_rock.png')))     #[3]
        self.funker_sprites.append(pygame.transform.scale2x(pygame.image.load('data/funker_sci.png')))      #[4]


        self.character.append(self.naked_sprites)       #[0]
        self.character.append(self.motoboy_sprites)     #[1]
        self.character.append(self.funker_sprites)      #[2]

        self.image = self.character[charSelection][int(self.current_sprite)]

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
        if choice != 0 and ready == True and gameOver == True:
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
        
        self.current_sprite = 0
        self.character = []
        
        self.naked_sprites = []
        self.naked_sprites.append(pygame.transform.flip(pygame.transform.scale2x(pygame.image.load('data/naked_idle_1.png')), True, False))   #[0]
        self.naked_sprites.append(pygame.transform.flip(pygame.transform.scale2x(pygame.image.load('data/naked_idle_2.png')), True, False))   #[1]
        self.naked_sprites.append(pygame.transform.flip(pygame.transform.scale2x(pygame.image.load('data/naked_paper.png')), True, False))    #[2]
        self.naked_sprites.append(pygame.transform.flip(pygame.transform.scale2x(pygame.image.load('data/naked_rock.png')), True, False))     #[3]
        self.naked_sprites.append(pygame.transform.flip(pygame.transform.scale2x(pygame.image.load('data/naked_sci.png')), True, False))      #[4]

        self.motoboy_sprites = []
        self.motoboy_sprites.append(pygame.transform.flip(pygame.transform.scale2x(pygame.image.load('data/moto_idle_1.png')), True, False))  #[0]
        self.motoboy_sprites.append(pygame.transform.flip(pygame.transform.scale2x(pygame.image.load('data/moto_idle_2.png')), True, False))  #[1]
        self.motoboy_sprites.append(pygame.transform.flip(pygame.transform.scale2x(pygame.image.load('data/moto_paper.png')), True, False))   #[2]
        self.motoboy_sprites.append(pygame.transform.flip(pygame.transform.scale2x(pygame.image.load('data/moto_rock.png')), True, False))    #[3]
        self.motoboy_sprites.append(pygame.transform.flip(pygame.transform.scale2x(pygame.image.load('data/moto_sci.png')), True, False))     #[4]

        self.funker_sprites = []
        self.funker_sprites.append(pygame.transform.flip(pygame.transform.scale2x(pygame.image.load('data/moto_idle_1.png')), True, False))  #[0]
        self.funker_sprites.append(pygame.transform.flip(pygame.transform.scale2x(pygame.image.load('data/moto_idle_2.png')), True, False))  #[1]
        self.funker_sprites.append(pygame.transform.flip(pygame.transform.scale2x(pygame.image.load('data/moto_paper.png')), True, False))   #[2]
        self.funker_sprites.append(pygame.transform.flip(pygame.transform.scale2x(pygame.image.load('data/moto_rock.png')), True, False))    #[3]
        self.funker_sprites.append(pygame.transform.flip(pygame.transform.scale2x(pygame.image.load('data/moto_sci.png')), True, False))     #[4]

        
        self.character.append(self.naked_sprites)       #[0]
        self.character.append(self.motoboy_sprites)     #[1]
        self.character.append(self.funker_sprites)      #[2]

        self.image = self.character[charSelection][int(self.current_sprite)]

        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x, pos_y]

    def update(self):
        global comp, ready, compSelection

        self.current_sprite += 0.2

        if ready == False:
            if self.current_sprite >= 2:
                self.current_sprite = 0
            self.image = self.character[compSelection][int(self.current_sprite)]
        if ready == True:
            if comp == 1:
                self.image = self.character[compSelection][2]
            if comp == 2:
                self.image = self.character[compSelection][3]
            if comp == 3:
                self.image = self.character[compSelection][4]


# main functions
def events():
    global menuSelection, gameOver, charSelection, inGame, choice, ready

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        elif event.type == pygame.KEYDOWN:

            if event.key == pygame.K_ESCAPE and 0 < menuSelection < 5:
                sys.exit()

            elif menuSelection == 100:
                if event.key == pygame.K_SPACE and ready == False:
                    ready = True
                elif event.key == pygame.K_SPACE and gameOver == True:
                    menuSelection = 1

            elif menuSelection == 200:
                if event.key == pygame.K_SPACE and ready == False:
                    ready = True
                elif event.key == pygame.K_SPACE and gameOver == True:
                    menuSelection = 1
                
            elif menuSelection < 5:
                if event.key == pygame.K_DOWN and inGame == False:
                    menuSelection += 1
                elif event.key == pygame.K_UP and inGame == False:
                    menuSelection -= 1
                elif event.key == pygame.K_RIGHT and inGame == False:
                    if charSelection >= 2:
                        charSelection = 2
                    else:
                        charSelection += 1
                elif event.key == pygame.K_LEFT and inGame == False:
                    if charSelection <= 0:
                        charSelection == 0
                    else:
                        charSelection -= 1
                elif event.key == pygame.K_RETURN:
                    menuSelection += 10

            
        elif event.type == pygame.MOUSEBUTTONDOWN:            
            if menuSelection < 10:
                if quickOn_button.rect.collidepoint(event.pos) or bestOn_button.rect.collidepoint(event.pos) or aboutOn_button.rect.collidepoint(event.pos) or exitOn_button.rect.collidepoint(event.pos):
                    menuSelection += 10
            elif menuSelection == 100 or menuSelection == 200:
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
            elif menuSelection == 300:
                if back_button.rect.collidepoint(event.pos):
                    menuSelection += 10

        elif event.type == pygame.MOUSEMOTION:
            if menuSelection < 10:
                if quickOff_button.rect.collidepoint(event.pos):
                    menuSelection = 1
                if bestOff_button.rect.collidepoint(event.pos):
                    menuSelection = 2
                if aboutOff_button.rect.collidepoint(event.pos):
                    menuSelection = 3
                if exitOff_button.rect.collidepoint(event.pos):
                    menuSelection = 4

        
def main_menu():
    global menuSelection, gameOver, charSelection, compSelection, inGame, font, choice, ready, comp, lock, yourScore, compScore
    global white, black, red, green, blue, yellow

    font = pygame.font.SysFont("Retro Computer", 20, False, False)

    # ---- start menu ----
    if menuSelection < 1:
        menuSelection = 1

    if menuSelection == 1:  # quick game
        music.set_volume(0.3)

        # variables need to reset here
        gameOver = False
        inGame = False
        ready = False
        comp = 0
        choice = 0
        yourScore = 0
        compScore = 0

        screen.blit(BACKGROUND, (0, 0))
        print_char()

        quickOn_button.render(screen)
        bestOff_button.render(screen)
        aboutOff_button.render(screen)
        exitOff_button.render(screen)
    
    if menuSelection == 2:  # best of 3
        screen.blit(BACKGROUND, (0, 0))
        print_char()

        quickOff_button.render(screen)
        bestOn_button.render(screen)
        aboutOff_button.render(screen)
        exitOff_button.render(screen)

    if menuSelection == 3:  # about
        screen.blit(BACKGROUND, (0, 0))
        print_char()

        quickOff_button.render(screen)
        bestOff_button.render(screen)
        aboutOn_button.render(screen)
        exitOff_button.render(screen)

    if menuSelection == 4:  # exit   
        screen.blit(BACKGROUND, (0, 0))
        print_char()

        quickOff_button.render(screen)
        bestOff_button.render(screen)
        aboutOff_button.render(screen)
        exitOn_button.render(screen)
    
    if menuSelection == 5:
        menuSelection = 4

    CHAR_SELECTION_GROUP.draw(screen)
    CHAR_SELECTION_GROUP.update()


    #   ---- bridges ----
    if menuSelection == 11:  # to quick game
        choice = 0
        lock = 0
        comp = randint(1, 3)
        compSelection = randint(0, 2)
        ready = False
        inGame = True
        menuSelection = 100

    if menuSelection == 12:  # to best of 3
        choice = 0
        lock = 0
        comp = randint(1, 3)
        compSelection = randint(0, 2)
        ready = False
        inGame = True
        menuSelection = 200

    if menuSelection == 13:  # to about
        menuSelection = 300

    if menuSelection == 14:  # to quit
        sys.exit()

    #   ---- game modes ----
    if menuSelection == 100:       # -- QUICK GAME --
        quick_game()

        PLAYER_GROUP.draw(screen)
        COMP_GROUP.draw(screen)
        PLAYER_GROUP.update()
        COMP_GROUP.update()

    if menuSelection == 200:       # -- BEST OF 3 --
        if gameOver == False:
            best_game()

            PLAYER_GROUP.draw(screen)
            COMP_GROUP.draw(screen)
            PLAYER_GROUP.update()
            COMP_GROUP.update()

    if menuSelection == 300:       # -- ABOUT --
        music.set_volume(0.1)
        
        screen.fill(black)

        font = pygame.font.SysFont("Retro Computer", 14, False, False)
        created = font.render("-- Created by Rodrigo Formigon, Heavy Games Co. --", True, white)
        version = font.render("-- Version 0.3.0 --", True, white)

        screen.blit(created, (155, 330))
        screen.blit(version, (318, 360))
        back_button.render(screen)   

    #   ---- callbacks ----
    if menuSelection == 310:  # back to main menu >about<
        menuSelection = 3
    

def loading_screen_init():
    screen.blit(LOADING, (0, 0))
    pygame.display.update()

    pygame.time.wait(500)
    #music.play(-1)
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
    global yourScore, compScore 
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
    global yourScore, compScore

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
    global yourScore, compScore
    
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


def best_game():
    global menuSelection, gameOver, yourScore, compScore, choice, ready, comp, lock, lastYourMove, lastCompMove
    global white, black, red, green, blue, yellow

    if yourScore < 2 and compScore < 2:
        best_round()

    elif yourScore == 2:
        gameOver = True

        screen.blit(INGAME, (0, 0))

        paper_button.render(screen)
        rock_button.render(screen)
        sci_button.render(screen)
        readyOn_button.render(screen)

        font = pygame.font.SysFont("Retro Computer", 16, False, False)

        you = font.render("YOU: ", True, white)
        screen.blit(you, (260, 200))
        screen.blit(pygame.transform.scale(lastYourMove, (40, 40)), (310, 188))

        computer = font.render(" :COMPUTER", True, white)
        screen.blit(computer, (492, 200))
        screen.blit(pygame.transform.scale(lastCompMove, (40, 40)), (450, 188))

        print_won()

        again = font.render('Press "space" to main menu', True, white)
        screen.blit(again, (249, 150))
        yourScore = 0
        compScore = 0


    elif compScore == 2:
        gameOver = True

        screen.blit(INGAME, (0, 0))

        paper_button.render(screen)
        rock_button.render(screen)
        sci_button.render(screen)
        readyOn_button.render(screen)

        font = pygame.font.SysFont("Retro Computer", 16, False, False)

        you = font.render("YOU: ", True, white)
        screen.blit(you, (260, 200))
        screen.blit(pygame.transform.scale(lastYourMove, (40, 40)), (310, 188))

        computer = font.render(" :COMPUTER", True, white)
        screen.blit(computer, (492, 200))
        screen.blit(pygame.transform.scale(lastCompMove, (40, 40)), (450, 188))

        print_lost()

        again = font.render('Press "space" to main menu', True, (white))
        screen.blit(again, (249, 150))
    

def best_round():
    global menuSelection, gameOver, yourScore, compScore, font, choice, ready, comp, lock, lastYourMove, lastCompMove
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
                if yourScore == 2 or compScore == 2:
                    quick_screen_true_ok(PAPER, PAPER)
                else:
                    best_screen_true_ok(PAPER, PAPER)
                print_draw()
                lastYourMove = PAPER
                lastCompMove = PAPER
                menuSelection = 12

        if comp == 2:  # comp chose ROCK
            quick_screen_true_notReady(PAPER)
            if ready == True:
                if yourScore == 2 or compScore == 2:
                    quick_screen_true_ok(PAPER, ROCK)
                else:
                    best_screen_true_ok(PAPER, ROCK)
                print_won()
                lastYourMove = PAPER
                lastCompMove = ROCK
                yourScore += 1
                menuSelection = 12

        if comp == 3:  # comp chose SCISSORS
            quick_screen_true_notReady(PAPER)
            if ready == True:
                if yourScore == 2 or compScore == 2:
                    quick_screen_true_ok(PAPER, SCISSORS)
                else:
                    best_screen_true_ok(PAPER, SCISSORS)
                print_lost()
                lastYourMove = PAPER
                lastCompMove = SCISSORS
                compScore += 1
                menuSelection = 12
        
    if choice == 2:  # you chose ROCK
        lock = choice

        if comp == 1:  # comp chose PAPER
            quick_screen_true_notReady(ROCK)
            if ready == True:
                if yourScore == 2 or compScore == 2:
                    quick_screen_true_ok(ROCK, PAPER)
                else:
                    best_screen_true_ok(ROCK, PAPER)
                print_lost()
                lastYourMove = ROCK
                lastCompMove = PAPER
                compScore += 1
                menuSelection = 12

        if comp == 2:  # comp chose ROCK
            quick_screen_true_notReady(ROCK)
            if ready == True:
                if yourScore == 2 or compScore == 2:
                    quick_screen_true_ok(ROCK, ROCK)
                else:
                    best_screen_true_ok(ROCK, ROCK)
                print_draw()
                lastYourMove = ROCK
                lastCompMove = ROCK
                menuSelection = 12

        if comp == 3:  # comp chose SCISSORS
            quick_screen_true_notReady(ROCK)
            if ready == True:
                if yourScore == 2 or compScore == 2:
                    quick_screen_true_ok(ROCK, SCISSORS)
                else:
                    best_screen_true_ok(ROCK, SCISSORS)
                print_won()
                lastYourMove = ROCK
                lastCompMove = SCISSORS
                yourScore += 1
                menuSelection = 12

    if choice == 3:  # you chose SCISSORS
        lock = choice

        if comp == 1:  # comp chose PAPER
            quick_screen_true_notReady(SCISSORS)
            if ready == True:
                if yourScore == 2 or compScore == 2:
                    quick_screen_true_ok(SCISSORS, PAPER)
                else:
                    best_screen_true_ok(SCISSORS, PAPER)
                print_won()
                lastYourMove = SCISSORS
                lastCompMove = PAPER
                yourScore += 1
                menuSelection = 12

        if comp == 2:  # comp chose ROCK
            quick_screen_true_notReady(SCISSORS)
            if ready == True:
                if yourScore == 2 or compScore == 2:
                    quick_screen_true_ok(SCISSORS, ROCK)
                else:
                    best_screen_true_ok(SCISSORS, ROCK)
                print_lost()
                lastYourMove = SCISSORS
                lastCompMove = ROCK
                compScore += 1
                menuSelection = 12

        if comp == 3:  # comp chose SCISSORS
            quick_screen_true_notReady(SCISSORS)
            if ready == True:
                if yourScore == 2 or compScore == 2:
                    quick_screen_true_ok(SCISSORS, SCISSORS)
                else:
                    best_screen_true_ok(SCISSORS, SCISSORS)
                print_draw()
                lastYourMove = SCISSORS
                lastCompMove = SCISSORS
                menuSelection = 12
        
        
def best_screen_true_ok(yourMove, compMove):
    global yourScore, compScore
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


def print_char():
    global charSelection    
    font = pygame.font.SysFont("Retro Computer", 14, False, False)

    right = font.render(">", True, white)
    left = font.render("<", True, white)

    if charSelection == 0:
        NAKED = font.render("NAKEDMAN", True, white)
        screen.blit(NAKED, (166,370))
        screen.blit(right, (270 ,350))

    elif charSelection == 1:
        MOTOBOY = font.render("MOTOBOY", True, white)
        screen.blit(MOTOBOY, (173,370))
        screen.blit(right, (270 ,350))
        screen.blit(left, (150 ,350))
    else:
        FUNKER = font.render("FUNKER", True, white)
        screen.blit(FUNKER, (178,370))
        screen.blit(left, (150 ,350))

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
inGame = False
ready = False
yourScore = 0
compScore = 0
comp = 0
lock = 0
choice = 0
lastYourMove = 0
lastCompMove = 0

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

QUICK = [
    pygame.image.load('data/quick_off.png').convert_alpha(),
    pygame.image.load('data/quick_on.png').convert_alpha()
]

BEST = [
    pygame.image.load('data/best_off.png').convert_alpha(),
    pygame.image.load('data/best_on.png').convert_alpha()
]

ABOUT = [
    pygame.image.load('data/about_off.png').convert_alpha(),
    pygame.image.load('data/about_on.png').convert_alpha()
]

EXIT = [
    pygame.image.load('data/exit_off.png').convert_alpha(),
    pygame.image.load('data/exit_on.png').convert_alpha()
]

BACK = pygame.image.load('data/back_on.png')


# buttons:
quickOff_button = Button(QUICK[0], (305, 300))
quickOn_button = Button(QUICK[1], (305, 300))

bestOff_button = Button(BEST[0], (305, 325))
bestOn_button = Button(BEST[1], (305, 325))

aboutOff_button = Button(ABOUT[0], (305,350))
aboutOn_button = Button(ABOUT[1], (305, 350))

exitOff_button = Button(EXIT[0], (305, 375))
exitOn_button = Button(EXIT[1], (305, 375))

back_button = Button(BACK, (305, 420))


paper_button = Button(PAPER, (120, 440))    # 1
rock_button = Button(ROCK, (350, 450))      # 2
sci_button = Button(SCISSORS, (580, 440))   # 3

readyOff_button = Button(pygame.transform.scale(READY[0], (70, 30)), (366, 400))
readyOn_button = Button(pygame.transform.scale(READY[1], (70, 30)), (366, 400))


# sounds
music = pygame.mixer.Sound('data/music.wav')
buttonSound = pygame.mixer.Sound('data/click.wav')


# sprites:
CHAR_SELECTION_GROUP = pygame.sprite.Group()
char_selection = Player(178, 262)
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
    print(menuSelection)
    #print(yourScore, compScore)


    events()

    pygame.display.update()

pygame.quit()
sys.exit()
