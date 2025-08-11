try:
    # Solicita ao usuário os coeficientes da equação do 2º grau e converte para float.
    a = float(input("Digite o valor de a: "))
    b = float(input("Digite o valor de b: "))
    c = float(input("Digite o valor de c: "))

    # Se 'a' for zero, não é uma equação do 2º grau.
    if a == 0:
        print("Não é uma equação do 2º grau.")
    else:
        # Calcula o delta usado a fórmula de Bhaskara.
        delta = b**2 - 4*a*c
        print(f"Delta = {delta:.0f}")  # Mostra o delta sem casas decimais.

        # Se delta < 0, não existem raízes reais.
        if delta < 0:
            print("A equação não possui raízes reais.")

        # Se delta == 0, existe uma raiz real (ou duas iguais).
        elif delta == 0:
            x = -b / (2*a)
            print(f"A equação possui uma raiz real(ou duas iguais): x = {x:.1f}")

        # Se delta > 0, existem duas raízes reais e diferentes.
        else:
            raiz_delta = delta ** 0.5  # Calcula a raiz quadrada de delta.
            x1 = (-b + raiz_delta) / (2*a)  # Primeira raiz.
            x2 = (-b - raiz_delta) / (2*a)  # Segunda raiz.
            print(f"A equação possui duas raízes reais distintas: x1 = {x1:.1f}, x2 = {x2:.1f}")

# Trata erro se o usuário digitar algo que não seja número.
except ValueError:
    print("Erro: Por favor, digite apenas números válidos.")

# Trata erro de divisão por zero (pouco provável aqui, mas seguro).
except ZeroDivisionError:
    print("Erro: Divisão por zero.")

# Trata qualquer outro erro inesperado que possa ocorrer.
except Exception as e:
    print(f"Ocorreu um erro inesperado: {e}")