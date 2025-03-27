N = int(input())

soma = 0

for i in range(0, N):
    nota = int(input())
    soma = soma + nota

media = soma/N

if media >= 60:
    print("APROVADO!")

elif media < 60 and media >= 30:
    print("RECUPERACAO!")

else:
    print("REPROVADO!")