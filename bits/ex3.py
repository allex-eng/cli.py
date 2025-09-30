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
# ----------------------------------------------------------------------
# 5 - CÁLCULO DO ÚLTIMO HOST VÁLIDO
# O último endereço que pode ser atribuído a um dispositivo é o
# endereço de broadcast - 1.

# A operação "E" (AND) com `0xFFFFFFFE` (que é ...11111110 em binário)
# simplesmente desliga o último bit do endereço de broadcast.
#   Broadcast: ...11111111
#   AND      : ...11111110
#   -----------------
#   Resultado: ...11111110
ipul_brod = intip_brodacast & 0xFFFFFFFF
strul_brod = '.'.join([str(x) for x in ipul_brod.to_bytes(4)])
# ----------------------------------------------------------------------
# 6 - CONVERSÃO DA MÁSCARA PARA DECIMAL
# Converte o inteiro da máscara de sub-rede de volta para o formato de
# string 'A.B.C.D' para fácil visualização (ex: 255.255.255.0).
strip_mark = '.'.join([str(x) for x in mark.to_bytes(4)])
# ----------------------------------------------------------------------
# 7 - CÁLCULO DO NÚMERO DE HOSTS VÁLIDOS
# A quantidade de hosts disponíveis em uma sub-rede é calculada pela
# fórmula 2^n - 2, onde 'n' é o número de bits de host.
# O '- 2' é porque o primeiro endereço (rede) e o último (broadcast)
# são reservados e não podem ser usados por dispositivos.

# (32 - intCIDR) calcula o número de bits de host (n).
# 2 ** n calcula o total de endereços na sub-rede.
inthost = 2 ** (32 - cidr) - 2