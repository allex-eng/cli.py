import sys  

try:
    # Solicita ao usuário que digite um número inteiro.
    numero = int(input('Digite um número positivo de até 4 dígitos: '))

    # Verifica se o número está fora do intervalo permitido (0 a 9999).
    if numero < 0 or numero > 9999:
        # Encerra o programa imediatamente com uma mensagem de erro.
        sys.exit('ERRO: Digite um número positivo e com até 4 dígitos.')

    # Extrai o dígito dos milhares (divisão inteira por 1000).
    mil = numero // 1000
    numero %= 1000  # Atualiza o número removendo o dígito dos milhares.

    # Extrai o dígito das centenas.
    cent = numero // 100
    numero %= 100  # Atualiza o número removendo o dígito das centenas.

    # Extrai o dígito das dezenas.
    dez = numero // 10
    numero %= 10  # Atualiza o número removendo o dígito das dezenas.

    # O que sobra agora é a unidade.
    uni = numero

    # Soma todos os dígitos.
    soma = mil + cent + dez + uni

   
    print(f'Soma dos dígitos: {mil} + {cent} + {dez} + {uni} = {soma}')

# Captura o erro se o usuário digitar algo que não pode ser convertido em inteiro.
except ValueError:
    print('ERRO: Informe um valor inteiro.')
