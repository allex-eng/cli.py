try:
    a1 = int(input('Digite o valor do primeiro termo: '))
    r = int(input('Digite o valor da razão: '))
    n = int(input('Digite o número de termos: '))

    if n <= 0:
        print("Só valores positivos!")
    elif r == 0:
        print('A P.A. é constante')
        soma = a1 * n
    else:
        if r > 0:
            print('A P.A. é crescente')
        else:
            print('A P.A. é decrescente')

        for i in range(1, n + 1):
            termo = a1 + (i - 1) * r
            if i == n:
                print(f"O {n}º termo da P.A. é {termo}")

        soma = (a1 + termo) * n // 2
        print(f'A soma dos {n} termos é {soma}')

except ValueError:
    print("Erro: digite um número inteiro válido.")
