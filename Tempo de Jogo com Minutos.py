HoraI, MinutoI, HoraF, MinutoF = input().split()

HoraI = int(HoraI)
MinutoI = int(MinutoI)
HoraF = int(HoraF)
MinutoF = int(MinutoF)

TotalI = (HoraI * 60) + MinutoI
TotalF = (HoraF * 60) + MinutoF

Res = TotalF - TotalI

if Res < 0:
    Res = Res + 1440

ResH = Res // 24
ResM = Res % 24

if Res > 1 and Res <= 1440:
    print(f"O JOGO DUROU {ResH} HORA(S) E {ResM} MINUTO(S)")