A = int(input())
B = int(input())
C = int(input())

soma = A - (B + C)

if (soma < B):
    print(B)
elif (soma < C):
    print(C)
else:
    print(soma)