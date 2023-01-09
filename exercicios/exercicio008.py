"""Escreva um programa  que pergunte a distância que passageiro irá viajar em km,Clacule o preço da passagem, cobrando 0,50 por km para viagens abaixo de 200km e 0,45 para longas distâncias"""

print("=="*10,"PROGRAMA CALCULO DE VIAGEM","=="*10)

dis = float(input("Digite por favor a distância da viagem em km: "))

if dis <= 200:
    passagem = 0.50*dis
    print(f"O valor da passagem foi: R$ {passagem:.2f}")
elif dis > 200:
    passagem = 0.45*dis
    print(f"O valor da passagem ficou em: R$ {passagem:.2f}")

