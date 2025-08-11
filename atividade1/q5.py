try:
    # Solicita ao usuário o tempo de estacionamento em horas e minutos
    t_hora = int(input('Digite a hora(s) que o carro ficou estacionado: '))
    t_min = int(input('Digite o minuto(s) que o carro ficou estacionado: '))
   
    # Validação do tempo em minutos, garantindo que não ultrapasse 59 minutos
    if t_min < 0 or t_min >= 60:
        print('ERRO: minutos inválidos. Por favor, digite um valor entre 0 e 59.')
    else:
        # Converte o tempo total para horas, considerando os minutos como fração
        t_total = t_hora + t_min / 60

        # Verifica o tempo total de estacionamento e calcula o valor a pagar baseado nesse tempo
        if t_total > 12:   # Se o carro ficou mais de 12 horas, o valor fixo será 30 reais
            valor = 30
        else:
            if t_total <= 2:  # Se o tempo for menor ou igual a 2 horas, o valor é calculado a 8 reais por hora
                valor = t_total * 8
            elif t_total <= 4:  # Se o tempo for entre 2 e 4 horas, as 2 primeiras horas custam 8 reais e o restante custa 5 reais por hora
                valor = 2 * 8 + (t_total - 2) * 5
            else:  # Se o tempo for superior a 4 horas, as 2 primeiras horas custam 8 reais, as próximas 2 custam 5 reais, e o restante custa 3 reais por hora
                valor = 2 * 8 + 2 * 5 + (t_total - 4) * 3

        # Imprime o valor a pagar com 2 casas decimais
        print(f"Valor a pagar: R$ {valor:.2f}")

except ValueError:  # Trata o erro caso o usuário digite algo que não seja um número inteiro válido
    print('ERRO: digite um número inteiro válido para horas e minutos.')