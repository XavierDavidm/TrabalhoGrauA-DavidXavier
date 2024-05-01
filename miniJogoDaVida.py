#import
import random









#funções
#dado para mover jogadores
def dado(posJogador):
    posJogador=posJogador+random.randint(1,6)
    if posJogador>21:
        posJogador=21
    return(posJogador)

#uma grande função contendo todas as 'casas' do tabuleiro,verifica a posição do jogador para executar as outras funções
def tabuleiro(posJogador):
    #casas com roleta
    if posJogador==1 or posJogador==3 or posJogador==10 or posJogador==17:
        print('você caiu na roleta! gire para ver sua sorte!')
    
    #casas com caveira
    if posJogador==2 or posJogador==8 or posJogador==18:
        print('')


#Regras das casas
def morte(jogadorvivo):
    print('o jogador morreu')
    jogadorvivo=False
    return jogadorvivo







#main
#variaveis iniciais:

#jogador 1
posJogador1 = 0
filhosJogador1 = 0
jogador1Casado = False
jogador1Divorciado = False
jogador1Formado = False
jogador1Famoso = False
jogador1Vivo = True

#jogador 2
posJogador2 = 0
filhosJogador2 = 0
jogador2Casado = False
jogador2Divorciado = False
jogador2Formado = False
jogador2Famoso = False
jogador2Vivo = True

#extra
dupla=False
lobby=0
nomeJ1=0
nomeJ2=0
#lobby determina se é 1 ou 2 jogadores, para então começar o jogo(contém validação de entrada)
while lobby !=1 and lobby !=2:
    lobby=int(input('digite o número de jogadores que vão jogar(1/2): '))
    if lobby==1:
        print('jogo solo')
        nomeJ1=input('digite seu nome jogador 1: ')
        print(nomeJ1,'iniciou sua jornada!')
        print('')
        dupla=False
        jogador2Vivo=False
    elif lobby==2:
        print('jogo em dupla')
        nomeJ1=input('digite seu nome jogador 1: ')
        nomeJ2=input('digite seu nome jogador 2: ')
        print(nomeJ1,'iniciou sua jornada!')
        print(nomeJ2,'iniciou sua jornada!')
        print('')
        dupla=True
    else:
        print('ERRO! por favor digite o número de jogadores entre 1 e 2')

#jogo principal
#-o jogo só acaba quando um jogador alcançar a posição 21 ou todos estiverem mortos.

while (posJogador1!=21 and posJogador2!=21) or (jogador1Vivo==False and jogador2Vivo==False):
    #movimento dos jogares
    if jogador1Vivo==True:
        posJogador1=dado(posJogador1)
        print('o jogador 1 está na casa',posJogador1)


    if dupla==True and jogador2Vivo==True:
        posJogador2=dado(posJogador2)
        print('o jogador 2 está na casa',posJogador2)

