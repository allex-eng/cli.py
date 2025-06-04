a1 = int(input('Digite o valor do primeiro termo: '))
r = int(input('Digite o valor da razão: '))
n = int(input('Digite o número de termos: '))

if r == 0:
    print('A P.A. é constante')
else:
    if r > 0:
        print('A P.A. é crescente')
    else:
        print('A P.A. é decrescente')

    for i in range(1, n + 1):
        termo = a1 + (i - 1) * r
        if i == n:
            print(f"O {n}º termo da P.A. é {termo}")


