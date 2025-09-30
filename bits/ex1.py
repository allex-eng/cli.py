ip ='192.168.1.10'
cidr = 24
intip = int.from_bytes(bytes([int(x) for x in ip.split('.')]), 'big')
mark = 0xFFFFFFFF >> (32 - cidr) << (32 - cidr)

# 2 - CÁLCULO DO ENDEREÇO DE REDE
# O endereço de rede é o primeiro endereço de uma sub-rede e é obtido
# aplicando a operação "E" (AND) bit a bit entre o endereço IP e a
# máscara de sub-rede. Esta operação zera a porção de host do IP.

# Operação AND bit a bit:
#   IP.....: 11000000.10101000.00000001.00001010  (192.168.1.10)
#   Máscara: 11111111.11111111.11111111.00000000  (255.255.255.0)
#   -------------------------------------------------------------
#   Rede...: 11000000.10101000.00000001.00000000  (192.168.1.0)
p_rede = intip & mark
# Converte o inteiro do endereço de rede de volta para o formato de string 'A.B.C.D'.
# `intIPRede.to_bytes(4)` -> Converte o inteiro em 4 bytes.
# `'.'.join(...)` -> Une os bytes convertidos em string com pontos.
redes = '.'.join([str(x) for x in p_rede.to_bytes(4)])

# ----------------------------------------------------------------------
# 3 - CÁLCULO DO PRIMEIRO HOST VÁLIDO
# O primeiro endereço que pode ser atribuído a um dispositivo na rede é o
# endereço de rede + 1.

# A operação "OU" (OR) bit a bit com 1 (0x00000001) garante que o último bit
# seja '1', resultando no primeiro endereço de host.
#   Rede.....: ...00000000
#   OU 1.....: ...00000001
#   ----------------------
#   Resultado: ...00000001
intpri_host = p_rede | 0x00000001
prime_host = '.'.join([str(x) for x in intpri_host.to_bytes(4)])
