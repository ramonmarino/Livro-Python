print("=="*10,"CALCULADORA","=="*10)
numero1 = int(input("Digite por favor um número: "))
numero2 = int(input("Digite por favor o segundo número: "))
operacao = int(input("Digite a operação desejada: [1-somar/2-subtrair/3-vezes]: "))

if operacao == 1:
     resultado = numero1 + numero2
     print(f"A SOMA DOS NÚMEROS {numero1} e {numero2} FOI: {resultado:.2f}")
elif operacao == 2:
     resultado = numero1 - numero2 
     print(f"A SUBTRAÇÃO DE {numero1} e {numero2} deu: {resultado:.2f}")
elif operacao == 3:
    resultado = numero1 * numero2
    print(f"O VALOR DA MULTIPLICAÇÃO DE {numero1} E {numero2} FOI: {resultado:.2f}")         