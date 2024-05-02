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

    #casas do desafio matemático
    if posJogador==4 or posJogador==11 or posJogador==19:
        desafioMatematico()

    #casa da faculdade
    if posJogador==5:
        jogadorFormado=formatura(Nomejogador,jogadorFormado)







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
#funções matematicas
def Primos(n):
    print("Números primos de 1 a 100:", end=" ")
    for num in range(1,n+1):
        if num > 1:
            primo = True
            for i in range(2, int(num/2) + 1):
                if (num % i) == 0:
                    primo = False                   
            if primo:
                print(num, end=" ")

def somatorio(ini,fim):
    soma = 0
    for i in range(ini,fim):
        soma += i
    print('a soma de todos os números do intervalo de ',ini,'até',fim,'é',soma)

def fibo(n):
    a, b = 0, 1
    for _ in range(10):
        print(a,end=" ")
        a, b = b, a + b

def circulo(r):
    area=3.14*r**2
    print('é',area)

def factorial(n):
    if n == 0:
        fact= 1
    else:
        fact= n * factorial(n-1)
    print(fact)

def div(n,m):
    count = 0
    num = 1
    while count < 5:
        if num % n == 0 and num % m == 0:
            print(num,end=" ")
            count += 1
        num += 1

#desafio matemático
def desafioMatematico():
    sort=random.randint(1,6)
    if sort==1:
        Primos(100)
        print('todos os números primos de 1 a 100')
    elif sort==2:
        somatorio(1,10)
        print('soma de todos os números 1 a 10')
    elif sort==3:
        fibo(10)
        print('série de fibonacci os 10 primeiro números')
    elif sort==4:
        print('area circulo com raio de 2,5')
        circulo(2.5)
    elif sort==5:
        print('factorial de 5 é:')
        factorial(5)
    elif sort==6:
        print('os primeiro 5 números divisiveis por 2 e 5 são')
        div(2,5)

#formatura
def formatura(Nomejogador,jogadorFormado):
    roll=random.randint(1,6)
    if roll==1:
        print(Nomejogador,'se formou em Administração')
        jogadorFormado='administracao'
    elif roll==2:
        print(Nomejogador,'se formou em Educação fisica')
        jogadorFormado='educacao fisica'
    elif roll==3:
        print(Nomejogador,'se formou em história')
        jogadorFormado='historia'
    elif roll==4:
        print(Nomejogador,'se formou em Engenharia')
        jogadorFormado='engenharia'
    elif roll==5:
        print(Nomejogador,'se formou em Análise e desenvolvimento de sistemas')
        jogadorFormado='analise e desenvolvimento de sistemas'
    elif roll==6:
        print(Nomejogador,'se formou em médicina')
        jogadorFormado='medicina'
    return(jogadorFormado)
#filho


#casamento



#famoso



#divórcio



#loteria



#novo amor(casar2 só que não pode ter divorciado nem casado )



#maquina do tempo



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
    print('')

    #jogador2 (se tiver)
    if dupla==True and jogador2Vivo==True and paralizado2==False:
        posJogador2=dado(posJogador2)
        print(nomeJ2,'caiu na casa',posJogador2)
        posJogador2,jogador2Vivo,nomeJ2,paralizado2 = tabuleiro(posJogador2,jogador2Vivo,nomeJ2,paralizado2)
    elif dupla==True and jogador2Vivo==True and paralizado2==True:
        print(nomeJ2,'perdeu seu turno')     
    elif dupla==True and jogador2Vivo==False:
        print(nomeJ2,'está morto')
    print('')

    input('aperte qualquer tecla para passar de turno')
#para melhor visualização dos turnos setá sempre nescessario apertar qualquer tecla para continuar.



    