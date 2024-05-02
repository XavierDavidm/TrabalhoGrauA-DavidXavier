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
def tabuleiro(posJogador,jogadorVivo,Nomejogador,paralizado,jogadorFormado,filhosJogador,jogadorCasado,jogadorFamoso,jogadorDivorciado,dinheiro):
    #casas com roleta
    if posJogador==1 or posJogador==3 or posJogador==10 or posJogador==17:
        print('você caiu na roleta! gire para ver sua sorte!')
        (posJogador,paralizado)=roleta(posJogador,Nomejogador,paralizado)
    #casas com caveira
    elif posJogador==2 or posJogador==8 or posJogador==18:
        jogadorVivo=morte(jogadorVivo,Nomejogador)
    #casas do desafio matemático
    elif posJogador==4 or posJogador==11 or posJogador==19:
        print('desafio matematico!!')
        desafioMatematico()
    #casa da faculdade
    elif posJogador==5:
        print(Nomejogador,'entrou na faculdade')
        jogadorFormado=formatura(Nomejogador,jogadorFormado)
    #casas de filho
    elif posJogador==6 or posJogador==9 or posJogador==13:
        filhosJogador=filho(Nomejogador,filhosJogador)
    #casas do casamento
    elif posJogador==7:
        jogadorCasado=casamento(Nomejogador)
    #casa da fama
    elif posJogador==15:
        jogadorFamoso=famoso(Nomejogador)
    #casa do divorcio
    elif posJogador==12:
        jogadorDivorciado=divorcio(Nomejogador,jogadorCasado,jogador1Divorciado)
    #casa da loteria
    elif posJogador==14:
        dinheiro=loteria(Nomejogador)
    #casa do novo amor
    elif posJogador==16:
        if jogadorCasado==True:
            print(Nomejogador,'já é casado')
        else:
            jogadorCasado=True
            jogadorDivorciado=False
            print(Nomejogador,'encontrou um novo amor na sua vida!')
    #maquina do tempo
    elif posJogador==20:
        reset(Nomejogador)
    return(posJogador,jogadorVivo,Nomejogador,paralizado,jogadorFormado,filhosJogador,jogadorCasado,jogadorFamoso,jogadorDivorciado,dinheiro)


def estatisticas(dupla,posJogador2,jogador2Vivo,nomeJ2,paralizado2,jogador2Formado,filhosJogador2,jogador2Casado,jogador2Famoso,jogador2Divorciado,dinheiro2,posJogador1,jogador1Vivo,nomeJ1,paralizado1,jogador1Formado,filhosJogador1,jogador1Casado,jogador1Famoso,jogador1Divorciado,dinheiro1):
    print('')
    print('estaticas de fim de jogo:')
    print('')
    print('estatisicas',nomeJ1)
    if jogador1Formado==False:
        print(nomeJ1,'não é formado')
    else:
        print(nomeJ1,'é formado em',jogador1Formado)
    print(nomeJ1,'teve',filhosJogador1,'filhos durante sua vida')
    if jogador1Casado==False:
        print(nomeJ1,'não se casou')
    else:
        print(nomeJ1,'é casado')
    if jogador1Divorciado==True:
        print(nomeJ1,'se divorciou')
    else:
        print(nomeJ1,'não se divorciou')
    if jogador1Famoso==True:
        print(nomeJ1,'é famoso')
    else:
        print(nomeJ1,'não foi famoso')
    if dinheiro1 == 0:
        print(nomeJ1,'nunca ganhou na loteria')
    else:
        print(nomeJ1,'ganhou',dinheiro1,'na loteria')

    if dupla==True:
        print('')
        print('estatisicas',nomeJ2)
        if jogador2Formado==False:
            print(nomeJ2,'não é formado')
        else:
            print(nomeJ2,'é formado em',jogador2Formado)
        print(nomeJ2,'deve',filhosJogador2,'durante sua vida')
        if jogador2Casado==False:
            print(nomeJ2,'não se casou')
        else:
            print(nomeJ2,'é casado')
        if jogador2Divorciado==True:
            print(nomeJ2,'se divorciou')
        else:
            print(nomeJ2,'não se divorciou')
        if jogador2Famoso==True:
            print(nomeJ2,'é famoso')
        else:
            print(nomeJ2,'não foi famoso')
        if dinheiro2 == 0:
            print(nomeJ2,'nunca ganhou na loteria')
        else:
            print(nomeJ2,'ganhou',dinheiro2,'na loteria')

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
   # if n == 0:
        #fact=1
    #else:
       # fact= n * factorial(n-1)
    print(120)

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
def filho(Nomejogador,filhosJogador):
    roll=random.randint(1,6)
    if roll==5:
        filhosJogador=filhosJogador+2
        print('Parabéns,',Nomejogador,'você teve gêmeos!')
    else:
        filhosJogador=filhosJogador+1
        print('Parabéns,',Nomejogador,'você teve um filho!')
    return filhosJogador

#casamento
def casamento(Nomejogador):
    print('parabéns,',Nomejogador,'você acaba de se casar!')
    jogadorCasado=True
    return jogadorCasado

#famoso
def famoso(Nomejogador):
    print(Nomejogador,'agora é famoso')
    jogadorFamoso=True
    return jogadorFamoso

#divórcio
def divorcio(Nomejogador,jogadorCasado,jogadorDivorciado):
    if jogadorCasado==False:
        print(Nomejogador,'não é casado, nada acontece')
    else:
        print(Nomejogador,'infelizmente se divorciou')
        jogadorCasado=False
        jogadorDivorciado=True
    return jogadorCasado,jogadorDivorciado

#loteria
def loteria(NomeJogador):
    roll=random.randint(1,6)
    if roll==1:
        print(NomeJogador,'ganhou 2,50 reais na loteria')
        dinheiro='2,50'
    if roll==2:
        print(NomeJogador,'ganhou 5.000,00 reais na loteria')
        dinheiro='5.000,00'
    if roll==3:
        print(NomeJogador,'ganhou 50.000,00 reais na loteria')
        dinheiro='50.000,00'
    if roll==4:
        print(NomeJogador,'ganhou 500.000,00 reais na loteria')
        dinheiro='500.000,00'
    if roll==5:
        print(NomeJogador,'ganhou 5.000.000,00 reais na loteria')
        dinheiro='5.000.000,00'
    if roll==6:
        print(NomeJogador,'ganhou 100.000.000,00 na loteria')
        dinheiro='100.000.000,00'
    return dinheiro

#maquina do tempo
def reset(Nomejogador):
    posJogador = 0
    filhosJogador = 0
    jogadorCasado = False
    jogadorDivorciado = False
    jogadorFormado = False
    jogadorFamoso = False
    jogadorVivo = True
    paralizado=False
    dinheiro=0
    print(Nomejogador,'encontrou uma maquina do tempo!!!, agora ele voutou ao inicio sem NADA!')
    return(posJogador,filhosJogador,jogadorCasado,jogadorDivorciado,jogadorFormado,jogadorFamoso,jogadorVivo,paralizado,dinheiro)

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
dinheiro1=0

#jogador 2
posJogador2 = 0
filhosJogador2 = 0
jogador2Casado = False
jogador2Divorciado = False
jogador2Formado = False
jogador2Famoso = False
jogador2Vivo = True
paralizado2=False
dinheiro2=0

#observação 'paralizado' é uma variavel que verifica se o jogador perdeu seu turno(util na função roleta)

#extra
dupla=False
lobby=0
nomeJ1=0
nomeJ2=0
fim=False
cont=0
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

while fim!=True:
    #movimento dos jogares e simulação do tabuleiro(contém validação de vida e paralisado)
    #observação 02 a linha contendo a funçao tabuleiro abaixo é extremamente longa pois nela são inseridas e retiradas todas as variaveis de cada player
    #jogador1

    cont=cont+1
    print('#####   TURNO',cont,'  #####')

    if jogador1Vivo==True and paralizado1!=True:
        posJogador1=dado(posJogador1)
        print(nomeJ1,'caiu na casa',posJogador1)
        posJogador1,jogador1Vivo,nomeJ1,paralizado1,jogador1Formado,filhosJogador1,jogador1Casado,jogador1Famoso,jogador1Divorciado,dinheiro1=tabuleiro(posJogador1,jogador1Vivo,nomeJ1,paralizado1,jogador1Formado,filhosJogador1,jogador1Casado,jogador1Famoso,jogador1Divorciado,dinheiro1)
    elif jogador1Vivo==True and paralizado1==True:
        print(nomeJ1,'perdeu seu turno')  
        paralizado1=False    
    else:
        print(nomeJ1,'está morto')
    print('')

    #jogador2 (se tiver)
    if dupla==True and jogador2Vivo==True and paralizado2==False:
        posJogador2=dado(posJogador2)
        print(nomeJ2,'caiu na casa',posJogador2)
        posJogador2,jogador2Vivo,nomeJ2,paralizado2,jogador2Formado,filhosJogador2,jogador2Casado,jogador2Famoso,jogador2Divorciado,dinheiro2=tabuleiro(posJogador2,jogador2Vivo,nomeJ2,paralizado2,jogador2Formado,filhosJogador2,jogador2Casado,jogador2Famoso,jogador2Divorciado,dinheiro2)
    elif dupla==True and jogador2Vivo==True and paralizado2==True:
        print(nomeJ2,'perdeu seu turno')  
        paralizado2=False   
    elif dupla==True and jogador2Vivo==False:
        print(nomeJ2,'está morto')
    print('')

    #comemoração(validação vem depois)
    if posJogador1==21:
        print(nomeJ1,'Teve uma vida longa e próspera!') 
    if posJogador2==21:
        print(nomeJ2,'Teve uma vida longa e próspera!') 

    #validação de fim de jogo(condições: se um chegar primeiro,todos estiverem mortos(dupla))
    if posJogador1==21 and posJogador2==21:
        print('ambos os jogadores chegaram vivos juntos ao final do tabuleiro') #fiz essa pra caso venha aquele 00001% de chance
        fim=True
    elif posJogador1==21:
        print(nomeJ1,'chegou ao fim do tabuleiro!')
        fim=True
    elif posJogador2==21:
        print(nomeJ2,'chegou ao fim do tabuleiro!')
        fim=True
    elif jogador1Vivo==False and dupla==False:
        print(nomeJ1,'GAME OVER!, infelizmente você morreu o jogo acabou, estatisticas abaixo:')
        fim=True
    elif jogador1Vivo==False and dupla==True and jogador2Vivo==False:
        print('GAME OVER!, infelizmente os jogadores estão mortos, o jogo acabou, estatisticas abaixo:')
        fim=True
    else:
        fim=False
    if fim==True:
        estatisticas(dupla,posJogador2,jogador2Vivo,nomeJ2,paralizado2,jogador2Formado,filhosJogador2,jogador2Casado,jogador2Famoso,jogador2Divorciado,dinheiro2,posJogador1,jogador1Vivo,nomeJ1,paralizado1,jogador1Formado,filhosJogador1,jogador1Casado,jogador1Famoso,jogador1Divorciado,dinheiro1)
###observaçâo: para não ficar poluida a tela decidi que aparecerá uma lista com todas as conquistas dos jogadores apenas no fim
#mas a cada ação é mostrado o que aconteceu no turno, ex Você é famoso agora.

    if fim==False:
        input('aperte qualquer tecla para passar de turno')
        print('')
#para melhor visualização dos turnos será sempre nescessario apertar qualquer tecla para continuar.

