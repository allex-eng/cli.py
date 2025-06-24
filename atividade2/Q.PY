for num in range(1, 1000000):
    if num % 2 == 0 or num % 5 == 0:
        soma_potencias = 0
        for d in str(num):
            soma_potencias += int(d) ** 5
        if soma_potencias == num:
            print(f'os valores: {num} ')
