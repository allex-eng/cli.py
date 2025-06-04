try:
    a = int(input('Digite um valor: '))
    b = int(input('Digite outro valor: '))

    if a <= 0 or b <= 0:
        print('Valor não permitido.')
    else:
        for _ in range(100):
            if b == 0:
                break
            divisão = a % b
            a = b
            b = divisão

        print(f'O MDC é {a}')

except ValueError:
    print("Erro: você deve digitar apenas números inteiros.")


