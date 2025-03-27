A = int(input())
M = int(input())

B = 0

if (A > M):
    B = M - (A - M)
elif (A == M):
    B = A
else:
    B = (M - A) + M
print(B)