import random

def jogar():
    mostra_mensagem_abertura()
    palavra_secreta = carrega_palavra_secreta()

    letras_acertadas = inicia_letras_acertadas(palavra_secreta)
    print(letras_acertadas)

    enforcou = False
    acertou = False
    tentativa = 0

    while(not enforcou and not acertou):

        chute = chama_chute()

        if(chute in palavra_secreta):
           mostra_chute_correto(chute, letras_acertadas, palavra_secreta)
        else:
            tentativa += 1

        enforcou = tentativa == 6
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)

    if (acertou):
        mostra_mensagem_vencedor()
    else:
       mostra_mensagem_perdedor()
    print("FIM DE JOGO")

def mostra_mensagem_vencedor():
    print("Você ganhou!!")

def mostra_mensagem_perdedor():
    print("Você perdeu!")

def chama_chute():
    input("Qual letra?")
    chute = chute.strip().upper()
    return chute

def inicia_letras_acertadas(palavra):
    ["_" for letra in palavra]

def mostra_mensagem_abertura():
    print("********************************")
    print("***Bem-vindo ao Jogo da Forca!**")
    print("********************************")

def mostra_chute_correto():
    index = 0
    for letra in palavra_secreta:
        if (chute == letra):
            letras_acertadas[index] = letra
        index += 1

def carrega_palavra_secreta():
    arquivo = open("palavras.txt", "r")
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()

    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()
    return palavra_secreta


if(__name__ == "__main__"):
    jogar()