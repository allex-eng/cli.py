import socket

# ---------------------------------------------------
HOST_IP_SERVER = '10.25.1.9'
HOST_PORT      = 50000
TUPLA_SERVER   = (HOST_IP_SERVER, HOST_PORT)

BUFFER_SIZE    = 4096
CODE_PAGE      = 'utf-8'
# ---------------------------------------------------

sockClient = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print("\nCliente iniciado.")
print("Digite o nome do arquivo para baixar.")
print("Digite MENSAGEM para ir ao modo de mensagens.")
print("Digite SAIR para fechar.\n")


while True:

    opcao = input("Arquivo / MENSAGEM / SAIR: ").strip()

    if opcao.lower() == "sair":
        break

    # ----------------------------------------------------
    #  MODO: BAIXAR ARQUIVO
    # ----------------------------------------------------
    if opcao.lower() != "mensagem":
        nomeArquivo = opcao

        # Envia o nome do arquivo
        sockClient.sendto(nomeArquivo.encode(CODE_PAGE), TUPLA_SERVER)

        # Recebe tamanho ou erro
        data, _ = sockClient.recvfrom(1024)
        resposta = data.decode(CODE_PAGE)

        if resposta.startswith("ERRO"):
            print(resposta)
            continue

        tamanho = int(resposta)
        print(f"Tamanho do arquivo: {tamanho} bytes")
        print("Baixando...")

        recebido = 0
        with open("baixado_" + nomeArquivo, "wb") as f:
            while recebido < tamanho:
                bloco, _ = sockClient.recvfrom(BUFFER_SIZE)
                f.write(bloco)
                recebido += len(bloco)

        print("Download concluído!\n")
        continue

    # ----------------------------------------------------
    #  MODO: MENSAGENS (modelo tamanho + mensagem)
    # ----------------------------------------------------
    print("\nModo de mensagens ativado.")
    print("Digite VOLTAR para voltar ao modo arquivo.")
    print("Digite SAIR para encerrar.\n")

    while True:
        msg = input("Mensagem: ")

        if msg.lower().strip() == "sair":
            sockClient.close()
            print("Cliente encerrado.")
            exit()

        if msg.lower().strip() == "voltar":
            print("\nVoltando ao modo arquivo...\n")
            break

        # Envia tamanho da mensagem
        bytesTamanho = str(len(msg)).encode(CODE_PAGE)
        sockClient.sendto(bytesTamanho, TUPLA_SERVER)

        # Envia mensagem
        sockClient.sendto(msg.encode(CODE_PAGE), TUPLA_SERVER)

        # Recebe tamanho da resposta
        bytesResp, tuplaOrigem = sockClient.recvfrom(BUFFER_SIZE)
        tamResp = int(bytesResp.decode(CODE_PAGE))
        if tamResp > BUFFER_SIZE: BUFFER_SIZE = tamResp

        # Recebe mensagem
        bytesResp, tuplaOrigem = sockClient.recvfrom(BUFFER_SIZE)
        resposta = bytesResp.decode(CODE_PAGE)

        host = socket.gethostbyaddr(tuplaOrigem[0])[0].split('.')[0].upper()
        print(f"{tuplaOrigem} -> {host}: {resposta}\n")


sockClient.close()
print("Cliente encerrado.")
