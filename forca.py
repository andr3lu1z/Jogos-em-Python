def jogar():
    print("********************************")
    print("***Bem-vindo ao Jogo da Forca!**")
    print("********************************")

    palavra_secreta = "banana"
    letras_acertadas = ["_", "_", "_", "_", "_", "_"]


    enforcou = False
    acertou = False

    while (not acertou and not enforcou):
        chute = input("Qual letra? ")
        chute = chute.strip()

        index = 0
        for letra in palavra_secreta:
            if (chute.upper() == letra.upper()):
                letras_acertadas[index] = letra
            index = index + 1
        print(letras_acertadas)

    print("FIM DE JOGO")

if(__name__ == "__main__"):
    jogar()