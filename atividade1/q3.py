h_partida = int(input('Digite a hora da partida: '))
min_partida = int(input('Digite o minuto da partida: '))
h_chegada = int(input('Digite a hora da chegada: '))
min_chegada = int(input('Digite o minuto da chegada: '))
h_pausa = int(input('Digite a hora da pausa: '))
min_pausa = int(input('Digite o minuto da pausa: '))

litros = float(input('Digite a quantidade de litros de combustível gasto: '))
preco_litro = float(input('Digite o preço do litro de combustível (R$): '))
distancia = float(input('Digite a distância percorrida (Km): '))
# Converte o horário de partida, chegada e pausa para minutos
tempo_partida = h_partida * 60 + min_partida
tempo_chegada = h_chegada * 60 + min_chegada
tempo_pausa = h_pausa * 60 + min_pausa
# Verifica se a hora de chegada foi antes da hora de partida (o que indicaria que a viagem passou pela meia-noite)
if tempo_chegada < tempo_partida:
    tempo_chegada += 1440  # Adiciona 1440 minutos (24 horas * 60 minutos = 144) para corrigir a hora de chegada

# Calcula a duração total da viagem e o tempo efetivo de movimento, descontando a pausa
duracao = tempo_chegada - tempo_partida
tempo_total = duracao - tempo_pausa

horas_totais = duracao / 60 # Converte os tempos de minutos para horas e minutos
horas_movimento = tempo_total / 60  # Tempo de movimento em horas
# Converte o tempo de movimento total (em minutos) para horas, minutos e segundos
time = tempo_total * 60  # Tempo total em segundos
horas = time // 3600  # Calcula o número de horas
minutos = (time % 3600) // 60 # Calcula os minutos restantes
segundos = time % 60 # Calcula os segundos restantes
if horas_totais > 0: # Calcula a velocidade média global e a velocidade média em movimento
    vm_global = distancia / horas_totais # Velocidade média considerando todo o tempo (incluindo a pausa)
else:          
    vm_global = 0

if horas_movimento > 0:  # Velocidade média considerando apenas o tempo de movimento
    vm_movimento = distancia / horas_movimento
else:
    vm_movimento = 0

custo_total = litros * preco_litro # Calcula o custo total da viagem com base no consumo de combustível

if litros > 0:
    km_por_litro = distancia / litros # Calcula o desempenho do carro (quantos quilômetros o carro percorre por litro de combustível)
else:
    km_por_litro = 0

if horas_movimento > 0:
    litros_por_hora = litros / horas_movimento # Calcula o desempenho do carro em litros por hora (quanto de combustível o carro consome por hora de movimento)
else:
    litros_por_hora = 0

if distancia > 0: # Calcula o custo por quilômetro percorrido
    reais_por_km = custo_total / distancia
else:
    reais_por_km = 0

print(f'Tempo em movimento: {horas} hora(s), {minutos} minuto(s) e {segundos} segundo(s).')
print(f'Velocidade média global: {vm_global:.2f} Km/h')
print(f'Velocidade média em movimento: {vm_movimento:.2f} Km/h')
print(f'Custo total da viagem: R$ {custo_total:.2f}')
print(f'Desempenho do carro: {km_por_litro:.2f} Km/l')
print(f'Desempenho do carro: {litros_por_hora:.2f} l/h')
print(f'Desempenho do carro: R$ {reais_por_km:.2f} por Km')