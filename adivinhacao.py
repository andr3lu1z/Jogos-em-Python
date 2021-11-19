import random
print("********************************")
print("Bem-vindo ao Jogo de Advinhação!")
print("********************************")

numero_secreto = random.randrange(1, 101)
total_tentativas = 0
pontos = 1000

print("Qual o nível de dificuldade?")
print("(1) Fácil, (2) Médio ou (3) Difícil")

nivel = int(input("Escolha o nível: "))

if (nivel == 1):
    total_tentativas = 20
elif(nivel == 2):
    total_tentativas = 10
else:
    total_tentativas = 5

for rodada in range (1, total_tentativas + 1):
    print("Tentativas {} de {}".format(rodada, total_tentativas))

    chute_str = input("Digite o seu número: ")
    print("Você digitou " , chute_str)
    chute = int(chute_str)

    if(chute < 1 or chute > 100):
        print("Número não permitido! Digite um número entre 1 e 100!")
        continue

    acertou = numero_secreto == chute
    maior   = chute > numero_secreto
    menor   = chute < numero_secreto

    if (acertou):
        print("PARABÉNS!!! Você acertou e marcou {} pontos".format(pontos))
        break
    else:
        if(maior):
            print("você errou! Seu palpite foi maior que o número secreto.")
        elif(menor):
            print("você errou! Seu palpite foi menor que o número secreto.")
        pontos_perdidos = abs(numero_secreto - chute)
        pontos = pontos - pontos_perdidos

    print("FIM DE JOGO")
