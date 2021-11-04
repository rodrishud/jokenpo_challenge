import emoji
import random
from time import sleep

#START
comp = 0
you = 0

while True:
    print('\033[4;31m{:=^40}\033[m'.format(' JOKENPÔ CHALLENGE '))
    print('[1] MELHOR DE 1         [2] MELHOR DE 3')
    mode = int(input('\033[1mENTER MODE: \033[m'))

    while mode != 1 and mode != 2:
        print('\033[1;31mMODO INVÁLIDO\033[m')
        print()
        mode = int(input('\033[1mENTER MODE: \033[m'))
    print()

    choice = ' '

    # MELHOR DE 1
    x = 0
    if mode == 1:
        while x not in (1, 2, 3):
            print(emoji.emojize('\033[1;37m[1] PEDRA\033[m :fist:  ', use_aliases=True), end='')
            print(emoji.emojize('\033[1;30m[2] PAPEL\033[m :hand:  ', use_aliases=True), end='')
            print(emoji.emojize('\033[1;33m[3] TESOURA\033[m :v:', use_aliases=True))

            x = int(input('\033[1;36mCHOOSE YOUR WEAPON: \033[m'))

        y = int(random.randint(1, 3))
        print()
        print('\033[1;32mJO \033[m', end='')
        sleep(0.5)
        print('\033[1;32mKEN \033[m', end='')
        sleep(0.5)
        print('\033[1;32mPO!\033[m')
        sleep(0.5)

        if y == 1 and x == 1:
            print(emoji.emojize('Você escolheu \033[1;37m[1] PEDRA\033[m :fist:', use_aliases=True))
            print(emoji.emojize('O computador escolheu \033[1;37m[1] PEDRA\033[m :fist:', use_aliases=True))
            print('\033[1;35m{:=^20}\033[m'.format(' EMPATE! '))
        else:
            if y == 2 and x == 2:
                print(emoji.emojize('Você escolheu \033[1;30m[2] PAPEL\033[m :hand:', use_aliases=True))
                print(emoji.emojize('O computador escolheu \033[1;30m[2] PAPEL\033[m :hand:', use_aliases=True))
                print('\033[1;35m{:=^20}\033[m'.format(' EMPATE! '))
            elif y == 3 and x == 3:
                print(emoji.emojize('Você escolheu \033[1;33m[3] TESOURA\033[m :v:', use_aliases=True))
                print(emoji.emojize('O computador escolheu \033[1;33m[3] TESOURA\033[m :v:', use_aliases=True))
                print('\033[1;35m{:=^20}\033[m'.format(' EMPATE! '))

            elif y == 1 and x == 2:
                print(emoji.emojize('Você escolheu \033[1;30m[2] PAPEL\033[m :hand:', use_aliases=True))
                print(emoji.emojize('O computador escolheu \033[1;37m[1] PEDRA\033[m :fist:', use_aliases=True))
                print('\033[1;36m{:=^20}\033[m'.format(' VOCÊ GANHOU! '))

            elif y == 2 and x == 3:
                print(emoji.emojize('Você escolheu \033[1;33m[3] TESOURA\033[m :v:', use_aliases=True))
                print(emoji.emojize('O computador escolheu \033[1;30m[2] PAPEL\033[m :hand:', use_aliases=True))
                print('\033[1;36m{:=^20}\033[m'.format(' VOCÊ GANHOU! '))

            elif y == 3 and x == 1:
                print(emoji.emojize('Você escolheu \033[1;37m[1] PEDRA\033[m :fist:', use_aliases=True))
                print(emoji.emojize('O computador escolheu \033[1;33m[3] TESOURA\033[m :v:', use_aliases=True))
                print('\033[1;36m{:=^20}\033[m'.format(' VOCÊ GANHOU! '))

            elif y == 1 and x == 3:
                print(emoji.emojize('Você escolheu \033[1;33m[3] TESOURA\033[m :v:', use_aliases=True))
                print(emoji.emojize('O computador escolheu \033[1;37m[1] PEDRA\033[m :fist:',
                                    use_aliases=True))
                print('\033[1;31m{:=^20}\033[m'.format(' VOCÊ PERDEU! '))

            elif y == 2 and x == 1:
                print(emoji.emojize('Você escolheu \033[1;37m[1] PEDRA\033[m :fist:', use_aliases=True))
                print(emoji.emojize('O computador escolheu \033[1;30m[2] PAPEL\033[m :hand:', use_aliases=True))
                print('\033[1;31m{:=^20}\033[m'.format(' VOCÊ PERDEU! '))

            elif y == 3 and x == 2:
                print(emoji.emojize('Você escolheu \033[1;30m[2] PAPEL\033[m :hand:',
                                    use_aliases=True))
                print(emoji.emojize('O computador escolheu \033[1;33m[3] TESOURA\033[m :v:',
                                    use_aliases=True))
                print('\033[1;31m{:=^20}\033[m'.format(' VOCÊ PERDEU! '))

            else:
                print('\033[1;30;41mOPÇÃO INVÁLIDA!\033[m')

        while choice not in 'SN':
            choice = str(input('\033[1;32mJOGAR NOVAMENTE? [S/N] \033[m')).upper().strip()[0]
        if choice == 'N':
            break
        print()


# MELHOR DE 3
    x = 0
    if mode == 2:
        while x not in (1, 2, 3):
            while you < 2 and comp < 2:
                print(emoji.emojize('\033[1;37m[1] PEDRA\033[m :fist:  ', use_aliases=True), end='')
                print(emoji.emojize('\033[1;30m[2] PAPEL\033[m :hand:  ', use_aliases=True), end='')
                print(emoji.emojize('\033[1;33m[3] TESOURA\033[m :v:', use_aliases=True))

                x = int(input('\033[1;36mCHOOSE YOUR WEAPON: \033[m'))

                y = int(random.randint(1, 3))
                print()
                print('\033[1;32mJO \033[m', end='')
                sleep(0.5)
                print('\033[1;32mKEN \033[m', end='')
                sleep(0.5)
                print('\033[1;32mPO!\033[m')
                sleep(0.5)

                if y == 1 and x == 1:
                    print(emoji.emojize('Você escolheu \033[1;37m[1] PEDRA\033[m :fist:', use_aliases=True))
                    print(emoji.emojize('O computador escolheu \033[1;37m[1] PEDRA\033[m :fist:', use_aliases=True))
                    print('\033[1;35m{:=^20}\033[m'.format(' EMPATE! '))
                    print()
                else:
                    if y == 2 and x == 2:
                        print(emoji.emojize('Você escolheu \033[1;30m[2] PAPEL\033[m :hand:', use_aliases=True))
                        print(emoji.emojize('O computador escolheu \033[1;30m[2] PAPEL\033[m :hand:', use_aliases=True))
                        print('\033[1;35m{:=^20}\033[m'.format(' EMPATE! '))
                        print()
                    elif y == 3 and x == 3:
                        print(emoji.emojize('Você escolheu \033[1;33m[3] TESOURA\033[m :v:', use_aliases=True))
                        print(emoji.emojize('O computador escolheu \033[1;33m[3] TESOURA\033[m :v:', use_aliases=True))
                        print('\033[1;35m{:=^20}\033[m'.format(' EMPATE! '))
                        print()

                    elif y == 1 and x == 2:
                        print(emoji.emojize('Você escolheu \033[1;30m[2] PAPEL\033[m :hand:', use_aliases=True))
                        print(emoji.emojize('O computador escolheu \033[1;37m[1] PEDRA\033[m :fist:', use_aliases=True))
                        print('\033[1;36m{:=^20}\033[m'.format(' VOCÊ GANHOU! '))
                        you += 1
                        print('\033[1;34mVOCÊ {}\033[m  x  \033[1;31m{} COMPUTADOR\033[m'.format(you, comp))
                        print()

                    elif y == 2 and x == 3:
                        print(emoji.emojize('Você escolheu \033[1;33m[3] TESOURA\033[m :v:', use_aliases=True))
                        print(emoji.emojize('O computador escolheu \033[1;30m[2] PAPEL\033[m :hand:', use_aliases=True))
                        print('\033[1;36m{:=^20}\033[m'.format(' VOCÊ GANHOU! '))
                        you += 1
                        print('\033[1;34mVOCÊ {}\033[m  x  \033[1;31m{} COMPUTADOR\033[m'.format(you, comp))
                        print()

                    elif y == 3 and x == 1:
                        print(emoji.emojize('Você escolheu \033[1;37m[1] PEDRA\033[m :fist:', use_aliases=True))
                        print(emoji.emojize('O computador escolheu \033[1;33m[3] TESOURA\033[m :v:', use_aliases=True))
                        print('\033[1;36m{:=^20}\033[m'.format(' VOCÊ GANHOU! '))
                        you += 1
                        print('\033[1;34mVOCÊ {}\033[m  x  \033[1;31m{} COMPUTADOR\033[m'.format(you, comp))
                        print()

                    elif y == 1 and x == 3:
                        print(emoji.emojize('Você escolheu \033[1;33m[3] TESOURA\033[m :v:', use_aliases=True))
                        print(emoji.emojize('O computador escolheu \033[1;37m[1] PEDRA\033[m :fist:',
                                            use_aliases=True))
                        print('\033[1;31m{:=^20}\033[m'.format(' VOCÊ PERDEU! '))
                        comp += 1
                        print('\033[1;34mVOCÊ {}\033[m  x  \033[1;31m{} COMPUTADOR\033[m'.format(you, comp))
                        print()

                    elif y == 2 and x == 1:
                        print(emoji.emojize('Você escolheu \033[1;37m[1] PEDRA\033[m :fist:', use_aliases=True))
                        print(emoji.emojize('O computador escolheu \033[1;30m[2] PAPEL\033[m :hand:', use_aliases=True))
                        print('\033[1;31m{:=^20}\033[m'.format(' VOCÊ PERDEU! '))
                        comp += 1
                        print('\033[1;34mVOCÊ {}\033[m  x  \033[1;31m{} COMPUTADOR\033[m'.format(you, comp))
                        print()

                    elif y == 3 and x == 2:
                        print(emoji.emojize('Você escolheu \033[1;30m[2] PAPEL\033[m :hand:',
                                            use_aliases=True))
                        print(emoji.emojize('O computador escolheu \033[1;33m[3] TESOURA\033[m :v:',
                                            use_aliases=True))
                        print('\033[1;31m{:=^20}\033[m'.format(' VOCÊ PERDEU! '))
                        comp += 1
                        print('\033[1;34mVOCÊ {}\033[m  x  \033[1;31m{} COMPUTADOR\033[m'.format(you, comp))
                        print()

                    else:
                        print('\033[1;30;41mOPÇÃO INVÁLIDA!\033[m')
                        print()

        if you == 2:
            print('\033[1;33mVOCÊ VENCEU\033[m')
        else:
            print('\033[1;31mO COMPUTADOR VENCEU\033[m')

        while choice not in 'SN':
            choice = str(input('\033[1;32mJOGAR NOVAMENTE? [S/N] \033[m')).upper().strip()[0]
        if choice == 'N':
            break
        print()
