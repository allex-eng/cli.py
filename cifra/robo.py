x = 0
y = 0

print("Controles do robô:")
print("w = norte, s = sul, a = oeste, d = leste")
print("Digite 'fim' para encerrar antes de 10 comandos.")

for i in range(10):  # limita a 10 comandos
    comando = input("Digite um comando: ").lower()

    if comando == 'fim':
        print("Movimentação encerrada pelo usuário.")
        break
    elif comando == 'w':
        y += 1
    elif comando == 's':
        y -= 1
    elif comando == 'a':
        x -= 1
    elif comando == 'd':
        x += 1
    else:
        # Aqui, comandos inválidos são simplesmente ignorados
        # não faz nada e segue para o próximo loop
        pass  

    print(f"Posição atual do robô: ({x}, {y})")

else:
    print("Número máximo de comandos atingido.")

print("Programa finalizado.")
