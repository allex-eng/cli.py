try:
    n = int(input("Digite a quantidade de termos da sequência de Fibonacci: "))

    if n <= 0:
        print("digite um número inteiro positivo.")
    else:
        a, b = 1, 1
        print("Sequência de Fibonacci:")

        if n == 1:
            print(a)
        else:
            print(a)
            print(b)
            for _ in range(n - 2):
                a, b = b, a + b
                print(b)

except ValueError:
    print("Erro: você deve digitar um número válido.")