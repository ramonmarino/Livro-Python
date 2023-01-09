"""Escreva um programa de média escolar em que a média do aluno
deverá ser 7 para ser aprovado, caso fique entre 5 e 7 estará de recuperação e 
abaixo de 5 estará reprovado, considere que só tem 3 matérias"""

print("-=-"*10,"PROGRAMA DE MÉDIA","-=-"*10)

materia1 = float(input("Digite por favor a primeira nota: "))
materia2 = float(input("Digite por favor a segunda nota: "))
materia3 = float(input("Digite por favor a terceira nota: "))


media_final = (materia1 + materia2 + materia3)/3

if media_final >= 7:
    print(f"O aluno passou de ano!,tá cagado a sua nota: {media_final:.0f}")
elif media_final > 5 and media_final < 7:
    print(f"Sinto muito está de reforço, sua nota: {media_final:.0f}")
else:
    print(f"Você precisa estudar mais, reprovado sua nota: {media_final:.0f}")
lista_notas =[materia1,materia2,materia3]
lista_notas.append(10)
print(f"As notas do aluno: {lista_notas}")
print()
 