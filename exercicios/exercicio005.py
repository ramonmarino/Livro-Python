'''Escreva um programa que e um aumento para um salário qualquer...'''

print("-=-"*10,"SEU SALÁRIO É MINHA DESGRAÇA","-=-"*10)

salario_atual = float(input("Digite por favor seu salário atual:"))
qtd_aumento = int(input("Digite por favor a porcetagem de aumento: "))

print(f"O aumento foi de {qtd_aumento}%")
print(f"Portanto o novo salário é:R${(salario_atual+(salario_atual*qtd_aumento)/100)}")