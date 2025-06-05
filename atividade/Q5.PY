try:
    # a) Solicite o valor inicial e a razão da P.A.
    a1 = int(input("Digite o valor inicial da P.A.: "))
    r = int(input("Digite a razão da P.A.: "))

    # b) Solicite a quantidade de elementos e exiba os valores da P.A.
    qtd = int(input("Digite a quantidade de termos da P.A.: "))

    if qtd <= 0:
        print("Erro: a quantidade de termos deve ser maior que zero.")
    else:
        print("Valores da P.A.:")
        for i in range(qtd):
            termo = a1 + i * r
            print(f"Termo {i + 1}: {termo}")

        # c) Classificação da P.A.
        if r == 0:
            print("\nA P.A. é constante.")
        elif r > 0:
            print("\nA P.A. é crescente.")
        else:
            print("\nA P.A. é decrescente.")

        # d) Soma dos elementos da P.A.
        soma = (qtd * (2 * a1 + (qtd - 1) * r)) // 2  # fórmula: S = n/2 * (2a + (n - 1)r)
        print(f"\nSoma dos {qtd} primeiros termos da P.A.: {soma}")

        # e) Valor de um termo qualquer (posição n)
        posicao = int(input("\nDigite a posição (n) de um termo da P.A. que deseja ver: "))
        if posicao <= 0:
            print("Erro: a posição deve ser um número positivo.")
        else:
            enesimo = a1 + (posicao - 1) * r
            print(f"O termo na posição {posicao} da P.A. é: {enesimo}")

except ValueError:
    print("Erro: por favor, digite apenas números inteiros válidos.")
