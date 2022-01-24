from random import randint
from sre_parse import parse_template 
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0,2)
print('O computador escolheu {}'.format(itens[computador]))
print(''' Suas opções:
[ 0 ] Pedra 
[ 1 ] Papel 
[ 2 ] Tesoura ''')
jogador = int(input('Qual a sua jogada?: '))
print('JO KEN PO!!!')
print('Computador jogou {}'.format(itens[computador]))
print('Jogador jogou {}'.format(itens[jogador]))


if computador == 0:
    if jogador == 0:
        print('Empatou.')
    elif jogador == 1:
        print('O Jogador ganhou.')
    elif jogador == 2:
        print('O computador ganhou.')
    else:
        print('JOGADA INVÁLIDA')

elif computador == 1:
    if jogador == 0:
        print('O computador ganhou.')
    elif jogador == 1:
        print('Empatou')
    elif jogador == 2:
        print('O jogador ganhou.')
    else:
        print('JOGADA INVÁLIDA')

elif computador == 2:
    if jogador == 0:
        print('O Jogador ganhou.')
    elif jogador == 1:
        print('O computador ganhou.')
    elif jogador == 2:
        print('Empatou.')
    else:
        print('JOGADA INVÁLIDA')
