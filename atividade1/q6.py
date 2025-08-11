import math  # Importa o módulo math para usar funções matemáticas, como cosseno e conversão para graus.

try:
    # Solicita ao usuário os valores dos três lados do triângulo e converte para float.
    lado_A = float(input('Digite o lado A: '))
    lado_B = float(input('Digite o lado B: '))
    lado_C = float(input('Digite o lado C: '))

    # Verifica se algum dos lados é menor ou igual a zero.
    if lado_A <= 0 or lado_B <= 0 or lado_C <= 0:
        print("Todos os lados devem ser maiores que zero.")
   
    # Verifica a condição de existência de um triângulo (a soma de dois lados deve ser maior que o terceiro).
    elif lado_A + lado_B > lado_C and lado_A + lado_C > lado_B and lado_B + lado_C > lado_A:
        print('Os lados formam um triângulo.')

        # Calcula o ângulo A usando a Lei dos Cossenos e converte o resultado de radianos para graus.
        ang_A = round(math.degrees(math.acos((lado_B**2 + lado_C**2 - lado_A**2) / (2 * lado_B * lado_C))), 2)

        # Calcula o ângulo B.
        ang_B = round(math.degrees(math.acos((lado_A**2 + lado_C**2 - lado_B**2) / (2 * lado_A * lado_C))), 2)

        # O ângulo C é calculado como 180° menos a soma dos outros dois (soma dos ângulos internos de um triângulo).
        ang_C = round(180 - (ang_A + ang_B), 2)

        # Verifica se os ângulos calculados são válidos (maiores que 0).
        if ang_A <= 0 or ang_B <= 0 or ang_C <= 0:
            print("Ângulos inválidos calculados.")
        else:
            # Mostra os ângulos calculados.
            print(f"Ângulos do triângulo: A = {ang_A}, B = {ang_B}, C = {ang_C}")

            # Classificação do triângulo com base nos ângulos:
            print("Classificação quanto aos ângulos:")
            if ang_A == 90 or ang_B == 90 or ang_C == 90:
                print('O Triângulo é Retângulo.')  # Um dos ângulos é 90°.
            elif ang_A > 90 or ang_B > 90 or ang_C > 90:
                print('O Triângulo é Obtusângulo.')  # Um dos ângulos é maior que 90°.
            else:
                print('O Triângulo é Acutângulo.')  # Todos os ângulos são menores que 90°.

            # Classificação do triângulo com base nos lados:
            print("Classificação quanto aos lados:")
            if lado_A == lado_B == lado_C:
                print('O Triângulo é Equilátero.')  # Todos os lados são iguais.
            elif lado_A == lado_B or lado_A == lado_C or lado_B == lado_C:
                print('O Triângulo é Isósceles.')  # Dois lados são iguais.
            else:
                print('O Triângulo é Escaleno.')  # Todos os lados são diferentes.
    else:
        # Se as condições do  triangular não forem validas.
        print('Não é um triângulo.')

# Tratamento de erro para entradas que não podem ser convertidas para float.
except ValueError:
    print("Entrada inválida: digite apenas números reais.")

# Tratamento  para qualquer erros inesperados.
except Exception as e:
    print(f"Ocorreu um erro inesperado: {e}")