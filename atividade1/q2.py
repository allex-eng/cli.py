try:
    valor = float(input('Digite o valor do saque: R$ '))
    saque = round(valor * 100)   # Converte o valor de reais para centavos (multiplicando por 100 e arredondando

    if saque <= 0:  # Converte o valor de reais para centavos (multiplicando por 100 e arredondando)
        print('ERRO: o valor deve ser positivo.')
    else:  # Calcula as cédulas e atualiza o valor do saque restante
        ced_100 = saque // 10000
        saque = saque % 10000

        ced_50 = saque // 5000
        saque = saque % 5000

        ced_20 = saque // 2000
        saque = saque % 2000

        ced_10 = saque // 1000
        saque = saque % 1000

        ced_5 = saque // 500
        saque = saque % 500

        ced_2 = saque // 200
        saque = saque % 200

        moe_1R = saque // 100
        saque = saque % 100

        moe_50 = saque // 50
        saque = saque % 50

        moe_25 = saque // 25
        saque = saque % 25

        moe_10 = saque // 10
        saque = saque % 10

        moe_5 = saque // 5
        saque = saque % 5

        moe_1 = saque // 1
        saque = saque % 1

    # Imprimindo as quantidades necessárias de cédulas e moedas
    print(f'Notas de R$100 necessárias: {ced_100:.0f}')
    print(f'Notas de R$50 necessárias: {ced_50:.0f}')
    print(f'Notas de R$20 necessárias: {ced_20:.0f}')
    print(f'Notas de R$10 necessárias: {ced_10:.0f}')
    print(f'Notas de R$5 necessárias: {ced_5:.0f}')
    print(f'Notas de R$2 necessárias: {ced_2:.0f}')
    print(f'Moedas de R$1 necessárias: {moe_1R:.0f}')
    print(f'Moedas de 50 centavos necessárias: {moe_50:.0f}')
    print(f'Moedas de 25 centavos necessárias: {moe_25:.0f}')
    print(f'Moedas de 10 centavos necessárias: {moe_10:.0f}')
    print(f'Moedas de 5 centavos necessárias: {moe_5:.0f}')
    print(f'Moedas de 1 centavo necessária: {moe_1:.0f}')
except ValueError: # Caso o usuário digite algo que não seja um número válido
    print('ERRO: informe um número válido.')