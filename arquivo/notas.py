import csv
import statistics
from datetime import datetime
from collections import defaultdict
from calendar import month_name

# 1) Ler o arquivo cotacao_dolar.csv e transformar em lista de sublistas
dados = []
with open('cotacao_dolar.csv', newline='', encoding='utf-8') as f:
    leitor = csv.reader(f, delimiter=';')
    for linha in leitor:
        if not linha or len(linha) < 3:
            continue  # Ignora linhas incompletas
        try:
            valor1 = float(linha[0].replace(',', '.'))
            valor2 = float(linha[1].replace(',', '.'))
            data = datetime.strptime(linha[2], "%Y-%m-%d").date()
            dados.append([valor1, valor2, data])
        except ValueError:
            continue  # Ignora linhas com dados inválidos

# 2) Gerar arquivos para cada ano
por_ano = defaultdict(list)
for linha in dados:
    ano = linha[2].year
    por_ano[ano].append(linha)

for ano, linhas in por_ano.items():
    nome_arquivo = f"cotacao_dolar_{ano}.csv"
    with open(nome_arquivo, 'w', newline='', encoding='utf-8') as f:
        escritor = csv.writer(f, delimiter=';')
        for l in linhas:
            escritor.writerow([f"{l[0]:.2f}", f"{l[1]:.2f}", l[2]])

# 3) Gerar arquivos por ano com médias mensais usando statistics.mean
for ano, linhas in por_ano.items():
    medias_por_mes = defaultdict(list)
    for l in linhas:
        mes = l[2].month
        media_dia = (l[0] + l[1]) / 2
        medias_por_mes[mes].append(media_dia)
    
    nome_saida = f"media_cotacao_{ano}.csv"
    with open(nome_saida, 'w', newline='', encoding='utf-8') as f:
        escritor = csv.writer(f, delimiter=';')
        for mes in sorted(medias_por_mes.keys()):
            nome_mes = month_name[mes]  # Nome do mês (em inglês)
            media_mensal = statistics.mean(medias_por_mes[mes])
            escritor.writerow([nome_mes, f"{media_mensal:.2f}"])
