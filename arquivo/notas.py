import csv
import statistics
from datetime import datetime
from collections import defaultdict
import os

# Nome do arquivo de entrada
nome_arquivo = 'cotacao_dolar.csv'

# 1) Ler o arquivo e montar a lista de sublistas
dados = []
with open(nome_arquivo, 'r', encoding='utf-8') as f:
    leitor = csv.reader(f, delimiter=';')
    for linha in leitor:
        valor1 = float(linha[0])
        valor2 = float(linha[1])
        data = datetime.strptime(linha[2], '%Y-%m-%d').date()
        dados.append([valor1, valor2, data])

# 2) Gerar arquivos por ano
anos = defaultdict(list)
for linha in dados:
    ano = linha[2].year
    anos[ano].append(linha)

base_nome, ext = os.path.splitext(nome_arquivo)
for ano, linhas in anos.items():
    nome_ano = f"{base_nome}_{ano}{ext}"
    with open(nome_ano, 'w', encoding='utf-8', newline='') as f:
        escritor = csv.writer(f, delimiter=';')
        for v1, v2, data in linhas:
            escritor.writerow([f"{v1:.2f}", f"{v2:.2f}", data.isoformat()])

# 3) Gerar médias mensais por ano com statistics.mean
dados_ano_mes = defaultdict(lambda: defaultdict(list))
for v1, v2, data in dados:
    media_diaria = (v1 + v2) / 2
    ano = data.year
    mes = data.month
    dados_ano_mes[ano][mes].append(media_diaria)

for ano, meses in dados_ano_mes.items():
    nome_saida = f"media_cotacao_{ano}.csv"
    with open(nome_saida, 'w', encoding='utf-8', newline='') as f:
        escritor = csv.writer(f, delimiter=';')
        for mes in sorted(meses):
            media_mensal = statistics.mean(meses[mes])
            nome_mes = datetime(ano, mes, 1).strftime('%B')  # Nome do mês por extenso
            escritor.writerow([nome_mes, f"{media_mensal:.4f}"])
