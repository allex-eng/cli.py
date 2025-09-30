ip ='192.168.1.10'
cidr = 24
intip = int.from_bytes(bytes([int(x) for x in ip.split('.')]), 'big')
mark = 0xFFFFFFFF >> (32 - cidr) << (32 - cidr)
p_rede = intip & mark
redes = '.'.join([str(x) for x in p_rede.to_bytes(4)])
intpri_host = p_rede | 0x00000001
prime_host = '.'.join([str(x) for x in intpri_host.to_bytes(4)])
ip_broadcast = p_rede | 0x00000001
striprime_host = '.'.join([str(x) for x in ip_broadcast.to_bytes(4)])
intip_brodacast = p_rede | (~mark & 0xFFFFFFFF)
strip_brodacast = '.'.join([str(x) for x in intip_brodacast.to_bytes(4)])
ipul_brod = intip_brodacast & 0xFFFFFFFF
strul_brod = '.'.join([str(x) for x in ipul_brod.to_bytes(4)])
strip_mark = '.'.join([str(x) for x in mark.to_bytes(4)])
inthost = 2 ** (32 - cidr) - 2

# ----------------------------------------------------------------------
# EXIBIÇÃO DOS RESULTADOS
# Imprime os resultados de forma organizada, mostrando tanto a representação
# decimal pontilhada quanto a representação binária de 32 bits para cada valor.

# Dados de Entrada
print('\nRESULTADOS OBTIDOS (os IPs estão no formato IPv4):\n')
# `:>15` alinha a string à direita em um espaço de 15 caracteres.
# `:032b` formata o inteiro como um número binário de 32 bits, com zeros à esquerda.
print(f'O Endereço é (IPv4).........................: {ip:>15} -> {intip:032b}')
print(f'O IP da Máscara para o CIDR /{cidr:<2} é...........: {strip_mark:>15} -> {mark:032b}\n')
# Resultados dos Cálculos
print(f'O Endereço da Rede é (IPv4).................: {redes:>15} -> {p_rede:032b}')
print(f'O Endereço do 1º Host da Rede é (IPv4)......: {prime_host:>15} -> {intpri_host:032b}')
print(f'O Endereço do Broadcast da Rede é (IPv4)....: {strip_brodacast:>15} -> {intip_brodacast:032b}')
print(f'O Endereço do Último Host da Rede é (IPv4)..: {strul_brod:>15} -> {ipul_brod:032b}')
print(f'A Quantidade de Hosts Válidos na Rede é.....: {inthost:>15}\n')
