import socket
import os
from PIL import Image

HOST_IP_SERVER = '192.168.56.1'
HOST_PORT = 50000
BUFFER_SIZE = 4096
CODE_PAGE = 'utf-8'

sockServer = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sockServer.bind((HOST_IP_SERVER, HOST_PORT))

print("\nServidor iniciado...\n")

try:
    while True:
        # Recebe nome do arquivo
        data, cliente = sockServer.recvfrom(1024)
        nomeArquivo = data.decode(CODE_PAGE)
        print(f"Cliente pediu: {nomeArquivo}")

        if not os.path.isfile(nomeArquivo):
            sockServer.sendto("ERRO: Arquivo não encontrado.".encode(CODE_PAGE), cliente)
            print("Arquivo não encontrado.")
            continue

        # ---------- ⬇️ MOSTRA A IMAGEM NO SERVIDOR ⬇️ ----------
        try:
            img = Image.open(nomeArquivo)
            img.show()  # Abre a imagem na tela
            print("Imagem aberta no servidor.")
        except Exception as e:
            print("Erro ao abrir imagem:", e)
        # ---------------------------------------------------------

        # Envia tamanho do arquivo
        tamanho = os.path.getsize(nomeArquivo)
        sockServer.sendto(str(tamanho).encode(CODE_PAGE), cliente)

        # Envia o arquivo
        with open(nomeArquivo, "rb") as f:
            while True:
                bloco = f.read(BUFFER_SIZE)
                if not bloco:
                    break
                sockServer.sendto(bloco, cliente)

        print("Envio concluído.\n")

except KeyboardInterrupt:
    print("Servidor encerrado.")
finally:
    sockServer.close()
