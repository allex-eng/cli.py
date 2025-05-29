

import sys

numero = None

try:
    numero = int(input('Digite um numero para calcular seu fatorial: '))

except ValueError: 
    sys.exit('ERRO: Digite um número inteiro positivo')

except Exception as exc:
    sys.exit(f'ERRO: {exc}')

else:
    if numero < 0:
        print('Não existe fatorial.')
    elif numero < 2:
        print(f'Fatorial de {numero} = 1')

    else:
        resultado = numero
        contador = numero
        
        while contador > 1:
            resultado *= (numero - 1)
            contador -= 1
        
        print(f'Fatorial de {numero} = {resultado}')