"""Escreva um programa que calcule a soma de três variáveis e imprima
o resultado na tela"""
print("-=-"*10,"VAMOS SOMAR?","-=-"*10)

numero = 1
cont = 0
while numero > 0 or numero < 0:
    numero = int(input("Digite por favor um número[Zero encerra]: "))
    cont += numero
print(f"A soma dos números inseridos deu o resultado de: {cont}")    


