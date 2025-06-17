try:
    massa = float(input('Digite a massa radioativa em (g): '))
    
    if massa <= 0:
        print('Esse valor não é possível. A massa deve ser maior que zero.')
    
    else:
        divisoes = 0
        while massa >= 0.05:
            massa = massa / 2
            divisoes += 1
            print(f'A massa é: {massa:.5f} g')
        
        print(f'Total de divisões até a massa ficar menor que 0.05 g: {divisoes}')

except ValueError:
    print("Erro: você deve digitar apenas números válidos.")
