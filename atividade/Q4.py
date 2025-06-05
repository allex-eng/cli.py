try:
    # a) Solicita valor inicial e razão da P.G.
    a1 = float(input("Digite o valor inicial da P.G.: "))
    q = float(input("Digite a razão da P.G.: "))

    # b) Solicita quantidade de termos e exibe os valores
    qtd = int(input("Digite a quantidade de termos da P.G.: "))

    if qtd <= 0:
        print("Erro: a quantidade de termos deve ser maior que zero.")
    else:
        print("\nValores da P.G.:")
        for i in range(qtd):
            termo = a1 * (q ** i)
            print(f"Termo {i + 1}: {termo}")

        # c) Classificação da P.G.
        if a1 == 0:
            print("A P.G. é singular (todos os termos são zero).")
        elif q == 1:
            print("A P.G. é constante.")
        elif q == 0:
            print("A P.G. é estacionária (após o primeiro termo, todos são zero).")
        elif q < 0:
            print("A P.G. é oscilante (alternada entre positivo e negativo).")
        elif (q > 1 and a1 > 0) or (0 < q < 1 and a1 < 0):
            print("A P.G. é crescente.")
        elif (0 < q < 1 and a1 > 0) or (q > 1 and a1 < 0):
            print("A P.G. é decrescente.")
        else:
            print("Classificação indefinida.")

        # d) Soma dos termos da P.G.
        print()
        if q == 1:
            soma = a1 * qtd
        else:
            soma = a1 * ((q ** qtd - 1) / (q - 1))
        print(f"Soma dos {qtd} primeiros termos da P.G.: {soma}")

        # e) Solicita a posição de um termo da P.G.
        pos = int(input("\nDigite a posição (n) de um termo da P.G. que deseja ver: "))
        if pos <= 0:
            print("Erro: a posição deve ser um número positivo.")
        else:
            enesimo = a1 * (q ** (pos - 1))
            print(f"O termo na posição {pos} da P.G. é: {enesimo}")

except ValueError:
    print("Erro: por favor, digite apenas números válidos.")
