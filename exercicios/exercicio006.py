"""Escreva um código para determinar se a pessoa deve pagar
imposto, considere que a pessoa deve pagar se receber mais que 1200
de salário"""

print("-=-"*10,"VERIFICADOR DE IMPOSTO","-=-"*10)

salario_pessoa = float(input("Digite por favor seu salário atual: "))

if salario_pessoa >= 1200:
    print("O você deverá pagar imposto!")
else:
    print("Não a necessidade de pagamento.")
print("Obrigado e volte sempre!")    