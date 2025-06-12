# # Solicita a mensagem ao usuário
mensagem = input("Digite a mensagem a ser cifrada: ")

# Solicita o deslocamento e converte para inteiro
deslocamento_str = input("Digite o valor do deslocamento (inteiro): ")
deslocamento = int(deslocamento_str)

# Inicializa a variável que vai armazenar a mensagem cifrada
mensagem_cifrada = ""

# Para cada caractere na mensagem original
for caractere in mensagem:
    codigo_original = ord(caractere)                  # Obtém o código Unicode do caractere
    codigo_cifrado = codigo_original + deslocamento   # Aplica o deslocamento
    caractere_cifrado = chr(codigo_cifrado)           # Converte de volta para caractere
    mensagem_cifrada += caractere_cifrado             # Adiciona à mensagem cifrada

# Exibe a mensagem cifrada
print("\nMensagem cifrada:")
print(mensagem_cifrada)

# Se quiser imprimir o código cifrado do último caractere (opcional)
print("Código cifrado do último caractere:", codigo_cifrado)
