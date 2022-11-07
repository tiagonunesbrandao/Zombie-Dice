# Aluno: Tiago Nunes Brandão.
# Matricula: 1112022202371
# Curso: Análise e Desenvolvimento de Sistemas.
# Prototipo do Zombie Dice FINAL, 8a Semana. Criado a partir do pseudocódigo do orientador.
# Professor: Galbas Milleo
# Feito em 25/09/2022

from random import randint
from time import sleep

#FUNCOES

#Cabecalho, apresentação do aluno

def inicio():
    print("\nALUNO: Tiago Nunes Brandão \nCURSO: Análise e Desenvolvimento de Sistemas\n")
    sleep(0.4)
    print("=" * 32)
    print("\033[1;35mZombie Dice (Protótipo Semana 8)\nSeja bem vindo ao Zombie Dice!\033[m")
    print("=" * 32)
    sleep(0.4)

#Definir Dados

def pegar_dado_Verde():
    return ('C', 'P', 'C', 'T', 'P', 'C')


def pegar_dado_Amarelo():
    return ('T', 'P', 'C', 'T', 'P', 'C')


def pegar_dado_Vermelho():
    return ('T', 'P', 'T', 'C', 'P', 'T')

#Colocando Dados no Copo

def init_dados_Copo(copo):

    for i in range(6):  # dados verdes no copo
        copo.append(pegar_dado_Verde())
    for i in range(4):  # dados amarelos no copo
        copo.append(pegar_dado_Amarelo())
    for i in range(3):  # dados vermelhos no copo
        copo.append(pegar_dado_Vermelho())
    return copo

#Para pegar os dados no copo

def pegar_dados_Copo(copo):
    if len(copo) != 0:
        num_Dados = (len(copo) - 1)
        index = randint(0, num_Dados)
        dado = copo[index]
        del (copo[index])
        return dado, copo
    else:
        print("--- COPO VAZIO ---")
        sleep(1.5)
        return -1, copo

#Rolar dos Dados e mostrar faces sorteadas

def lancar_Dado(dado):
    if dado == ('C', 'P', 'C', 'T', 'P', 'C'):
        print("\033[1;32mDado VERDE\033[m, com face sorteada: ",end="")
        sleep(1)
    elif dado == ('T', 'P', 'C', 'T', 'P', 'C'):
        print("\033[1;33mDado AMARELO\033[m, com face sorteada: ",end="")
        sleep(1)
    elif dado == ('T', 'P', 'T', 'C', 'P', 'T'):
        print("\033[1;31mDado VERMELHO\033[m, com face sorteada: ",end="")
        sleep(1)

    face_Dado = randint(0, 5)
    if dado[face_Dado] == "C":
        print("\033[1;7mCérebro - VOCÊ COMEU UM CÉREBRO!!!\033[m")
        sleep(0.3)
        return 'C'
    elif dado[face_Dado] == "T":
        print("\033[1;7mTiro - VOCÊ LEVOU UM TIRO!!!\033[m")
        sleep(0.3)
        return 'T'
    else:
        print("\033[1;7mPassos - SUA VÍTIMA ESCAPOU!!!\033[m")
        sleep(0.3)
        return "P"


#Mostrar jogador da rodada

def mostrar_Player():

    print("\033[1;35m======================\033[m")
    print(f"\033[1;34mVez do jogador {nome}\033[m")
    print("\033[1;35m======================\033[m")
    sleep(1.3)

#Mostrar Dados no Copo

def mostrar_dados_Copo(copo):
    list_Dado = []
    for dado in copo:
        if dado == ("C", "P", "C", "T", "P", "C"):
            list_Dado.append("Verde")
        elif dado == ("T", "P", "C", "T", "P", "C"):
            list_Dado.append("Amarelo")
        else:
            list_Dado.append("Vermelho")
    print(f'COPO: {list_Dado}')
    sleep(1.5)

#Mostrar dados que pegou

def mostrar_Dado(dado):
    if dado == ("C", "P", "C", "T", "P", "C"):
        print("Pegou o dado \033[1;32mVERDE\033[m")
        sleep(0.5)
    elif dado == ("T", "P", "C", "T", "P", "C"):
        print("Pegou o dado \033[1;33mAMARELO\033[m")
        sleep(0.5)
    else:
        print("Pegou o dado \033[1;31mVERMELHO\033[m")
        sleep(0.5)

#Verificando pontuacao

def verificar_Score(primeiro, segundo, terceiro):
    tiro = 0
    cerebro = 0
    passos = 0
    if primeiro == "C":
        cerebro += 1
    elif primeiro == "T":
        tiro += 1
    else:
        passos += 1
    if segundo == "C":
        cerebro += 1
    elif segundo == "T":
        tiro += 1
    else:
        passos += 1
    if terceiro == "C":
        cerebro += 1
    elif terceiro == "T":
        tiro += 1
    else:
        passos += 1
    return (cerebro, tiro, passos)

#COMECO DO APLICATIVO

inicio()

copo = []
copo = init_dados_Copo(copo)
list_Players = []
Jogs = []
num_Players = 0

# INFORME NUMERO DE JOGADORES

while num_Players < 2:
    try:
        num_Players = int(input("\n\033[1mPara começar, informe o número de jogadores (pelo menos 2 jogadores): \033[m"))
        if num_Players < 2:
            print("\033[1mATENÇÃO!!\033[m Você precisa de pelo menos 2 jogadores!!\n")
            sleep(1)
    except ValueError:
        print ("\033[1mPor favor, digite apenas números :)\n\033[m")

# COLOCAR NOME DOS JOGADORES

for ind in range(num_Players):
    nome = str(input(f"\033[1mEscreva o nome do jogador {str(ind + 1)}: \033[m"))
    cerebro = 0
    tiro = 0
    passos = 0
    player = [ind, nome, cerebro, tiro, passos]
    Jogs.append(nome)
    list_Players.append(player)


print(f"\n\033[1;35mBOA SORTE {Jogs}!\nE QUE VENCA O MELHOR!\n\n---------- INICIANDO O JOGO ----------\n\033[m")
sleep(0.8)

play = True
while (play):
    for player in list_Players:
        cod = player[0]
        nome = player[1]
        mostrar_Player()
        print("\n\033[4;34mO copo está com todos os 13 dados!\033[m\n")
        mostrar_dados_Copo(copo)
        turno = True
        block_Dado1 = True
        block_Dado2 = True
        block_Dado3 = True

        primeiro_Dado = -1
        segundo_Dado = -1
        terceiro_Dado = -1

        while (turno):
            play_Game = str(input("Pronto para jogar? (S/N): ")).upper()
            sleep(1)
            if play_Game == "S":
                pass
            else:
                turno = False
                play = False
                break

            print("\n\033[4;34mPegue os 3 dados no copo...\033[m\n")
            sleep(0.8)
            if block_Dado1:
                primeiro_Dado, copo = pegar_dados_Copo(copo)
            mostrar_Dado(primeiro_Dado)

            if block_Dado2:
                segundo_Dado, copo = pegar_dados_Copo(copo)
            mostrar_Dado(segundo_Dado)

            if block_Dado3:
                terceiro_Dado, copo = pegar_dados_Copo(copo)
            mostrar_Dado(terceiro_Dado)

            print("\n\033[4;34mMostrar Dados Restantes no Copo:\033[m\n")
            mostrar_dados_Copo(copo)
            input("\n\033[1;34mAgora, aperte ENTER para rolar os dados e jogar sua sorte!\033[m")
            sleep(1.2)

            one = " "
            two = " "
            three = " "

            if primeiro_Dado != -1:
                one = lancar_Dado(primeiro_Dado)
            if segundo_Dado != -1:
                two = lancar_Dado(segundo_Dado)
            if terceiro_Dado != -1:
                three = lancar_Dado(terceiro_Dado)
            # Para os dados com face "passos"
            block_Dado1 = True
            block_Dado2 = True
            block_Dado3 = True

            cerebro, tiro, passos = verificar_Score(one, two, three)

#Verificar se a vitima escapou
            if passos > 0:
                if one == "P":
                    block_Dado1 = False
                if two == "P":
                    block_Dado2 = False
                if three == "P":
                    block_Dado3 = False

            list_Players[cod][2] = player[2] + cerebro
            list_Players[cod][3] = player[3] + tiro
            list_Players[cod][4] = player[4] + passos

            print(f"\n\033[1mPlayer: {list_Players[cod][1]}")
            print(f"Cerebro: {str(list_Players[cod][2])}")
            print(f"Tiro: {str(list_Players[cod][3])}")
            print(f"Passos: {str(list_Players[cod][4])}\033[m")

#Verificar se tomou 3 tiros
            if list_Players[player[0]][3] >=3:
                print("\033[1;30;41mJÁ ERA! TOMOU 3 TIROS E PERDEU TODOS OS CÉREBROS COMIDOS!!! HA-HA-HA!!!\033[m\n")
                list_Players[player[0]][2] = 0
                list_Players[player[0]][3] = 0
                list_Players[player[0]][4] = 0
                copo_Reset = []
                copo = init_dados_Copo(copo_Reset)
                print("\033[4;34mRetornando os dados para o copo...\033[m")
                sleep(2)
                mostrar_dados_Copo(copo)

                turno = False

#Verificar vencedor (se comeu 13 cerebros ou mais)
            if list_Players[player[0]][2] >= 13:
                print("\033[1;30;42mVOCÊ COMEU CÉREBROS PRA CARAMBA E VENCEU O JOGO!!! PARABÉNS!\033[m")
                print("""\033[1;30;42m(Agora toma aqui seu Omeprazol)\033[m\n""")
                copo_Reset = []
                copo = init_dados_Copo(copo_Reset)
                print("\033[4;34mRetornando os dados para o copo...\033[m")
                sleep(2)
                mostrar_dados_Copo(copo)
                play = False
                turno = False

            if turno:
                continue_Turno = str(input("Você deseja continuar? (S/N): ")).upper()

            if continue_Turno == "S":
                continue
            else:
                print("\n\033[4;34mPróximo Jogador!\033[m\n")
                sleep(2)
                list_Players[player[0]][3] = 0
                copo_Reset = []
                copo = init_dados_Copo(copo_Reset)
                turno = False
