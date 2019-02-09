#menu de escolha de modo de jogo
def menu():
    parar = False
    while parar != True:
        print("Bem-vindo ao jogo do NIM! Escolha:")
        print("")
        print("1 - para jogar uma partida isolada")
        print("2 - para jogar um campeonato")
        resposta = int(input())
        #verifica a resposta do usuário
        if resposta == 1:
            print("Voce escolheu partida isolada")
            parar = True
            #executa a função de partida isolada
            partida_isolada()
        elif resposta == 2:
            print("Voce escolheu campeonato")
            parar = True
            #executa a função de campeonato
            campeonato()
        else: 
            print("Escolha uma das opcoes acima")

def partida_isolada():
    resultado = partida()
    if resultado == 1:
        print("Voce venceu!")
    else:
        print("O computador venceu!")

def campeonato():
    rodada_final = int(input("Deseja quantas rodadas? "))
    rodada = 1
    usuario = 0
    computador = 0
    while rodada <= rodada_final:
        print("**** Rodada {} ****".format(rodada))
        print("")
        resultado = partida()
        if resultado == 1:
            print("Voce venceu!")
            usuario = usuario + 1
        if resultado == 0:
            print("O computador venceu!")
            computador = computador + 1
        rodada = rodada + 1
    print("**** Final do campeonato! ****")
    print("")
    print("Placar: Você {} x {} Computador ".format(usuario, computador))


def partida():
    n = int(input("Quantas peças? "))
    m = int(input("Limite de peças por jogada? "))
    jogada = 0
    usuario_ultimo = False
    #condição que define quem irá começar o jogo
    if n % (m + 1) == 0:
        print("Voce começa!")
        print("")
        vez_do_computador = False
    else: 
        print("O computador começa!")
        print("")
        vez_do_computador = True

    #loop até as peças acabarem
    while n > 0:
        if vez_do_computador:
            jogada = computador_escolhe_jogada(n, m)
            vez_do_computador = False
            usuario_ultimo = False
            print("O computador tirou {} peça(s) do tabuleiro.".format(jogada))
            n = n - jogada  
            if n == 1:
                print("Resta uma peça no tabuleiro.")
                print("")
            else:
                print("Restam {} peças no tabuleiro.".format(n))
                print("")
        else:
            jogada = usuario_escolhe_jogada(n, m)
            vez_do_computador = True
            usuario_ultimo = True
            print("Voce tirou {} peça(s) do tabuleiro.". format(jogada))
            n = n - jogada  
            if n == 1:
                print("Resta uma peça no tabuleiro.")
                print("")
            else:
                print("Restam {} peças no tabuleiro.".format(n))
                print("")

    #resultado da rodada
    if usuario_ultimo:
        return 1
    else:
        return 0

def usuario_escolhe_jogada(n, m):
    print("Sua vez!")
    print("")
    terminar = False
    while terminar == False:
        jogada = int(input("Quantas peças você vai tirar? "))
        print("")
        terminar = True
        if jogada > n or jogada > m or jogada < 1:
            terminar = False
            print("Oops! Jogada inválida! Tente de novo.")
            print("")
    return jogada

def computador_escolhe_jogada(n, m):
    print("Vez do computador!")
    print("")
    if n <= m:
        return n
    resto = n % (m + 1)
    if resto != 0:
        return resto
    else:
        return m 

menu()
