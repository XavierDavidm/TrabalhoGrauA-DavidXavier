#import
import random

#funções principais

#dado para mover jogadores
def dado(posJogador):
    posJogador=posJogador+random.randint(1,6)
    if posJogador>21:
        posJogador=21
    return(posJogador)

#uma grande função contendo todas as 'casas' do tabuleiro,verifica a posição e status do jogador para executar as outras funções
def tabuleiro(posJogador,jogadorVivo,Nomejogador,paralizado):
    #casas com roleta
    if posJogador==1 or posJogador==3 or posJogador==10 or posJogador==17:
        print('você caiu na roleta! gire para ver sua sorte!')
        (posJogador,paralizado)=roleta(posJogador,Nomejogador,paralizado)

    #casas com caveira
    if posJogador==2 or posJogador==8 or posJogador==18:
        jogadorVivo=morte(jogadorVivo,Nomejogador)

    return (posJogador,jogadorVivo,Nomejogador,paralizado)






#Regras das casas

#roleta
def roleta(posJogador,Nomejogador,paralizado):
    roll=random.randint(1,6)
    if roll==1:
        print(Nomejogador,'tirou 1 na roleta, avance uma casa!')
        posJogador=posJogador+1
        print(Nomejogador,'agora está na casa',posJogador)
        paralizado=False
    elif roll==3:
        print(Nomejogador,'tirou 3 na roleta, volte uma casa!')
        posJogador=posJogador-1
        print(Nomejogador,'agora está na casa',posJogador)
        paralizado=False
    elif roll==6:
        print(Nomejogador,'tirou 6 na roleta, Você perdeu seu proximo turno!')
        paralizado=True
    else:
        print(Nomejogador,'tirou',roll,'no dado, nada acontece!')
        paralizado=False
    print('')
    return posJogador,paralizado

#morte
def morte(jogadorVivo,Nomejogador):
    print(Nomejogador,'Morreu!')
    #chamar função das estatisticas
    jogadorVivo=False
    print('')
    return jogadorVivo

#desafio matemático





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
paralizado1=False

#jogador 2
posJogador2 = 0
filhosJogador2 = 0
jogador2Casado = False
jogador2Divorciado = False
jogador2Formado = False
jogador2Famoso = False
jogador2Vivo = True
paralizado2=False

#observação 'paralizado' é uma variavel que verifica se o jogador perdeu seu turno(util na função roleta)

#extra
dupla=False
lobby=0
nomeJ1=0
nomeJ2=0
fim=False

#lobby determina se é 1 ou 2 jogadores, para então começar o jogo(contém validação de entrada) e nomes dos jogadores

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

while fim!=True: #or (jogador1Vivo!=True and jogador2Vivo!=True):
    #movimento dos jogares e simulação do tabuleiro(contém validação de vida e paralisado)

    #jogador1
    if jogador1Vivo==True and paralizado1!=True:
        posJogador1=dado(posJogador1)
        print(nomeJ1,'caiu na casa',posJogador1)
        posJogador1,jogador1Vivo,nomeJ1,paralizado1=tabuleiro(posJogador1,jogador1Vivo,nomeJ1,paralizado1)
    elif jogador1Vivo==True and paralizado1==True:
        print(nomeJ1,'perdeu seu turno')     
    else:
        print(nomeJ1,'está morto')

    #jogador2 (se tiver)
    if dupla==True and jogador2Vivo==True and paralizado2==False:
        posJogador2=dado(posJogador2)
        print(nomeJ2,'caiu na casa',posJogador2)
        posJogador2,jogador2Vivo,nomeJ2,paralizado2 = tabuleiro(posJogador2,jogador2Vivo,nomeJ2,paralizado2)
    elif dupla==True and jogador2Vivo==True and paralizado2==True:
        print(nomeJ2,'perdeu seu turno')     
    elif dupla==True and jogador2Vivo==False:
        print(nomeJ2,'está morto')

    input('aperte qualquer tecla para passar de turno')
#para melhor visualização dos turnos setá sempre nescessario apertar qualquer tecla para continuar.



    