try:
    a1 = float(input('Digite o valor do primeiro termo : '))
    q = float(input('Digite o valor da razão : '))
    n = int(input('Digite o número de termos: '))

    if n <= 0:
        print("Erro: o número de termos deve ser maior que zero.")
    else:
        
        if a1 == 0:
            print("A P.G. é singular .")
        elif q == 1:
            print("A P.G. é constante.")
        elif q == 0 and a1 != 0:
            print("A P.G. é estacionária.")
        elif q < 0:
            print("A P.G. é oscilante (alternada).")
        elif q > 1 or (0 < q < 1 and a1 < 0):
            print("A P.G. é crescente.")
        elif (0 < q < 1 and a1 > 0) or (q > 1 and a1 < 0):
            print("A P.G. é decrescente.")
        else:
            print("Classificação.")

    an = a1 * (q ** (n - 1))
    print(f"O {n}º termo da P.G. é {an}")

    if q == 1:
     soma = a1 * n
    else:
     soma = a1 * ((q ** n - 1) / (q - 1))
    print(f"Soma dos {n} primeiros termos da P.G.: {soma}")  
except ValueError:
  print("Erro: você deve digitar apenas números válidos ")


       