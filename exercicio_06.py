#A padaria Hotpão vende uma certa quantidade de pães franceses e uma quantidade de broas a
# cada dia. Cada pãozinho custa R$ 0,12 e a broa custa R$ 1,50. Ao final do dia, o dono quer saber
# quanto arrecadou com a venda dos pães e broas (juntos), e quanto deve guardar numa conta de
# poupança (10% do total arrecadado). Você foi contratado para fazer os cálculos para o dono. Com
# base nestes fatos, faça um algoritmo para ler as quantidades de pães e de broas, e depois calcular
# os dados solicitados. 


paes_vendidos = int(input("Quantidade de pães vendidos no dia:"))

broas_vendidas = int(input("Quantidade de broas vendidas no dia"))

lucro_paes = paes_vendidos * 0.12
print("lucro com pães:", lucro_paes)
lucro_broas = broas_vendidas * 1.50
print("lucro com broas:", lucro_broas)

total_vendido = lucro_paes + lucro_broas
print("total vendido:", total_vendido)

poupar = total_vendido * (10/100)

print("O valor a ser guardado na poupança é: ", poupar)