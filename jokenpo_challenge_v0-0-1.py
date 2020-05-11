import emoji
import random
from time import sleep

print('\033[4;31m{:=^40}\033[m'.format(' JOKENPÔ CHALLENGE '))
print(emoji.emojize('\033[1;37m[1] PEDRA\033[m :fist:', use_aliases=True))
print(emoji.emojize('\033[1;30m[2] PAPEL\033[m :hand:', use_aliases=True))
print(emoji.emojize('\033[1;33m[3] TESOURA\033[m :v:', use_aliases=True))

y = int(random.randint(1, 3))
x = int(input('\033[1;36mCHOOSE YOUR WEAPON: \033[m'))
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
    else:
        if y == 3 and x == 3:
            print(emoji.emojize('Você escolheu \033[1;33m[3] TESOURA\033[m :v:', use_aliases=True))
            print(emoji.emojize('O computador escolheu \033[1;33m[3] TESOURA\033[m :v:', use_aliases=True))
            print('\033[1;35m{:=^20}\033[m'.format(' EMPATE! '))

        else:
            if y == 1 and x == 2:
                print(emoji.emojize('Você escolheu \033[1;30m[2] PAPEL\033[m :hand:', use_aliases=True))
                print(emoji.emojize('O computador escolheu \033[1;37m[1] PEDRA\033[m :fist:', use_aliases=True))
                print('\033[1;36m{:=^20}\033[m'.format(' VOCÊ GANHOU! '))
            else:
                if y == 2 and x == 3:
                    print(emoji.emojize('Você escolheu \033[1;33m[3] TESOURA\033[m :v:', use_aliases=True))
                    print(emoji.emojize('O computador escolheu \033[1;30m[2] PAPEL\033[m :hand:', use_aliases=True))
                    print('\033[1;36m{:=^20}\033[m'.format(' VOCÊ GANHOU! '))
                else:
                    if y == 3 and x == 1:
                        print(emoji.emojize('Você escolheu \033[1;37m[1] PEDRA\033[m :fist:', use_aliases=True))
                        print(emoji.emojize('O computador escolheu \033[1;33m[3] TESOURA\033[m :v:', use_aliases=True))
                        print('\033[1;36m{:=^20}\033[m'.format(' VOCÊ GANHOU! '))
                    else:
                        if y == 1 and x == 3:
                            print(emoji.emojize('Você escolheu \033[1;33m[3] TESOURA\033[m :v:', use_aliases=True))
                            print(emoji.emojize('O computador escolheu \033[1;37m[1] PEDRA\033[m :fist:',
                                                use_aliases=True))
                            print('\033[1;31m{:=^20}\033[m'.format(' VOCÊ PERDEU! '))
                        else:
                            if y == 2 and x == 1:
                                print(emoji.emojize('Você escolheu \033[1;37m[1] PEDRA\033[m :fist:', use_aliases=True))
                                print(emoji.emojize('O computador escolheu \033[1;30m[2] PAPEL\033[m :hand:', use_aliases=True))
                                print('\033[1;31m{:=^20}\033[m'.format(' VOCÊ PERDEU! '))
                            else:
                                if y == 3 and x == 2:
                                    print(emoji.emojize('Você escolheu \033[1;30m[2] PAPEL\033[m :hand:',
                                                        use_aliases=True))
                                    print(emoji.emojize('O computador escolheu \033[1;33m[3] TESOURA\033[m :v:',
                                                        use_aliases=True))
                                    print('\033[1;31m{:=^20}\033[m'.format(' VOCÊ PERDEU! '))
                                else:
                                    print('\033[1;30;41mOPÇÃO INVÁLIDA!\033[m')