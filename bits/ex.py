# VARIÁVEIS DE ENTRADA (Altere estes valores para testar)
# Endereço IPv4 em formato string.
# Cada um dos quatro números (octetos) pode ir de 0 a 255.
ip = '192.168.1.10'
# Notação CIDR (Classless Inter-Domain Routing).
# Este número representa a quantidade de bits '1' no início da máscara de
# sub-rede, determinando o tamanho da porção de rede do endereço.
# Um /24, por exemplo, significa que os primeiros 24 bits são para a rede
# e os 8 bits restantes são para os hosts.
cidr = 24
# ----------------------------------------------------------------------
# 1 - CONVERSÃO PARA REPRESENTAÇÃO NUMÉRICA (BINÁRIA)
# Para realizar cálculos de rede, é muito mais fácil trabalhar com os
# endereços IP como números inteiros de 32 bits, em vez de strings.
# Converte a string '192.168.1.10' em um número inteiro.
# 1. `strIP.split('.')` -> Divide a string em uma lista: ['192', '168', '1', '10'].
# 2. `[int(x) for x in ...]` -> Converte cada elemento da lista para inteiro: [192, 168, 1, 10].
# 3. `bytes(...)` -> Converte a lista de inteiros em uma sequência de 4 bytes.
# 4. `int.from_bytes(..., 'big')` -> Interpreta esses 4 bytes como um único número inteiro de 32 bits.
#    O 'big' refere-se à ordem "big-endian", o padrão para redes.
intip = int.from_bytes(bytes([int(x) for x in ip.split('.')]), 'big')
# Calcula a máscara de sub-rede como um número inteiro.
# Uma máscara CIDR /24 tem 24 bits '1' seguidos por 8 bits '0'.
# 1. `(32 - intCIDR)` -> Calcula o número de bits do host (32 - 24 = 8).
# 2. `0xFFFFFFFF` -> É o número 2**32 - 1, que em binário é '11111111111111111111111111111111' (32 bits '1').
# 3. `>> (32 - intCIDR)` -> Desloca os bits para a direita, preenchendo com zeros à esquerda.
#    Isso cria os bits de host (ex: '00000000111111111111111111111111').
# 4. `<< (32 - intCIDR)` -> Desloca os bits de volta para a esquerda, preenchendo com zeros à direita.
#    Isso posiciona corretamente a máscara, resultando em 24 uns seguidos por 8 zeros
#    (ex: '11111111111111111111111100000000').
mark = 0xFFFFFFFF >> (32 - cidr) << (32 - cidr)


print(f'Máscara de sub-rede como inteiro..........: {mark}\n')

print(f'Máscara de sub-rede em binário é (32 bits): {mark:032b}\n')