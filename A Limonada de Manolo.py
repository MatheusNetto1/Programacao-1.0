N, C = input().split()
N = int(N)
C = int(C)

soma = 0

for i in range(N):
    if (C - i < 1):
        soma += 1
    else:
        soma += (C - i)
print(soma)
