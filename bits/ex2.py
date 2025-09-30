ip ='192.168.1.10'
cidr = 24
intip = int.from_bytes(bytes([int(x) for x in ip.split('.')]), 'big')
mark = 0xFFFFFFFF >> (32 - cidr) << (32 - cidr)
p_rede = intip & mark
redes = '.'.join([str(x) for x in p_rede.to_bytes(4)])
intpri_host = p_rede | 0x00000001
prime_host = '.'.join([str(x) for x in intpri_host.to_bytes(4)])

# 4 - CÁLCULO DO ENDEREÇO DE BROADCAST
# O endereço de broadcast é o último endereço da sub-rede. Ele é usado
# para enviar dados para todos os dispositivos na mesma sub-rede.
# É calculado preenchendo a porção de host do endereço de rede com bits '1'.

# `~intMascara` inverte todos os bits da máscara, criando uma "máscara invertida"
# (wildcard mask) que isola a porção de host (ex: 00000000.00000000.00000000.11111111).
# A operação "OU" (OR) com esta máscara invertida liga todos os bits de host
# do endereço de rede.
#
#   Rede.....: 11000000.10101000.00000001.00000000
#   Mascara..: 00000000.00000000.00000000.11111111
#   -------------------------------------------------
ip_broadcast = p_rede | 0x00000001
striprime_host = '.'.join([str(x) for x in ip_broadcast.to_bytes(4)])
# ----------------------------------------------------------------------
# 4 - CÁLCULO DO ENDEREÇO DE BROADCAST
# O endereço de broadcast é o último endereço da sub-rede. Ele é usado
# para enviar dados para todos os dispositivos na mesma sub-rede.
# É calculado preenchendo a porção de host do endereço de rede com bits '1'.

# `~intMascara` inverte todos os bits da máscara, criando uma "máscara invertida"
# (wildcard mask) que isola a porção de host (ex: 00000000.00000000.00000000.11111111).
# A operação "OU" (OR) com esta máscara invertida liga todos os bits de host
# do endereço de rede.
#
#   Rede.....: 11000000.10101000.00000001.00000000
#   Mascara..: 00000000.00000000.00000000.11111111
#   -------------------------------------------------
#   Broadcast: 11000000.10101000.00000001.11111111 (192.168.1.255)
intip_brodacast = p_rede | (~mark & 0xFFFFFFFF) # '& 0xFFFFFFFF' garante que o número seja de 32 bits
strip_brodacast = '.'.join([str(x) for x in intip_brodacast.to_bytes(4)])