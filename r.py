try:
    base = int(input("Digite a base (número inteiro): "))
    expoente = int(input("Digite o expoente (número inteiro não-negativo): "))

    if expoente < 0:
        print("Erro: O expoente deve ser um número inteiro não-negativo.")
    else:
        resultado = 1
        contador = 0

        while contador < expoente:
            resultado *= base
            contador += 1

        print("Resultado:", resultado)

except ValueError:
    print("Erro: Você deve digitar apenas números inteiros.")
