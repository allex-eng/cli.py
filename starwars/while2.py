import sys

numero = None

try:
    numero = int(input('Digite um numero para calcular se é primo: '))

except ValueError: 
    sys.exit('ERRO: Digite um número inteiro positivo.')

except Exception as exc:
    sys.exit(f'ERRO: {exc}')

else:
    divisores = 1
    contDivisor = 0 # poderia tambem ja iniciar com 2
    while divisores <= numero:
        if (numero % divisores) == 0:
            contDivisor += 1
        divisores += 1

    if contDivisor == 2:
        print(f'{numero} é primo.')
    else:
        print(f'{numero} não é primo')