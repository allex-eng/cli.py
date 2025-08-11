# Importa o módulo datetime para trabalhar com datas (nascimento, contribuição, etc.)
import datetime

# Importa relativedelta para adicionar ou subtrair anos, meses e dias com mais precisão
import dateutil.relativedelta

# Importa sys para poder encerrar o programa em caso de erro
import sys

# Data da Reforma da Previdência
DATA_REFORMA = datetime.datetime(2019, 11, 13)

# Entrada do sexo do usuário
sexo = input("Informe o sexo (masculino/feminino): ").lower()
if sexo != "masculino" and sexo != "feminino":
    sys.exit("Sexo inválido. Digite 'masculino' ou 'feminino'.")

# Entrada da data de nascimento
data_nascimento = input("Informe a data de nascimento (DD/MM/AAAA): ")
try:
    data_nascimento = datetime.datetime.strptime(data_nascimento, "%d/%m/%Y")
except:
    sys.exit("Data de nascimento inválida. Use o formato DD/MM/AAAA.")

# Entrada da data de início da contribuição
data_contribuicao = input("Informe a data de início da contribuição (DD/MM/AAAA): ")
try:
    data_contribuicao = datetime.datetime.strptime(data_contribuicao, "%d/%m/%Y")
except:
    sys.exit("Data de contribuição inválida. Use o formato DD/MM/AAAA.")

# Se começou a contribuir após a reforma, aplica-se as novas regras
if data_contribuicao > DATA_REFORMA:
    # Define idade mínima e tempo mínimo de contribuição com base no sexo
    if sexo == "masculino":
        idade_minima = 65
        tempo_contrib_min = 15
    else:
        idade_minima = 62
        tempo_contrib_min = 15

    # Calcula quando a pessoa atinge a idade mínima
    data_atinge_idade = data_nascimento + dateutil.relativedelta.relativedelta(years=idade_minima)

    # Calcula quando atinge o tempo mínimo de contribuição
    data_atinge_tempo = data_contribuicao + dateutil.relativedelta.relativedelta(years=tempo_contrib_min)

    # A aposentadoria ocorrerá quando ambos os requisitos forem atingidos
    if data_atinge_idade > data_atinge_tempo:
        data_aposentadoria = data_atinge_idade
    else:
        data_aposentadoria = data_atinge_tempo

    print("Aposentadoria (regras após reforma):", data_aposentadoria.strftime("%d/%m/%Y"))
    sys.exit()

# Se começou a contribuir antes da reforma, aplicam-se as regras antigas e de transição

# Define critérios de idade e contribuição por sexo
if sexo == "masculino":
    idade_minima = 65
    tempo_contrib_min = 15
    tempo_total = 35  # Anos para aposentadoria por tempo de contribuição
else:
    idade_minima = 62
    tempo_contrib_min = 15
    tempo_total = 30

# Calcula a data em que atinge a idade mínima
data_atinge_idade = data_nascimento + dateutil.relativedelta.relativedelta(years=idade_minima)

# Calcula a data em que completa 15 anos de contribuição
data_15_a_contrib = data_contribuicao + dateutil.relativedelta.relativedelta(years=tempo_contrib_min)

# A aposentadoria por idade é quando ambos os critérios (idade mínima e 15 anos de contribuição) são atingidos
if data_atinge_idade > data_15_a_contrib:
    data_ap_idade = data_atinge_idade
else:
    data_ap_idade = data_15_a_contrib

# Calcula o tempo de contribuição até a data da reforma
diferenca_contrib = dateutil.relativedelta.relativedelta(DATA_REFORMA, data_contribuicao)
anos_contribuidos = ( diferenca_contrib.years +diferenca_contrib.months / 12 +diferenca_contrib.days / 365.25)

# Calcula quanto tempo falta para atingir o tempo total exigido
tempo_faltando = tempo_total - anos_contribuidos
if tempo_faltando < 0:
    tempo_faltando = 0  # Garante que não haja valor negativo

# Aplica o pedágio de 50% sobre o tempo que falta
pedagio = tempo_faltando * 0.5

# Soma o tempo faltante ao pedágio para saber quanto ainda precisa contribuir
total_restante = tempo_faltando + pedagio

# Converte o tempo restante em dias
dias_restantes = int(total_restante * 365.25)

# Calcula a data de aposentadoria por tempo de contribuição (com pedágio)
data_ap_tempo = DATA_REFORMA + datetime.timedelta(days=dias_restantes)

# Exibe os dois tipos de aposentadoria possíveis
print("Aposentadoria por Idade:", data_ap_idade.strftime("%d/%m/%Y"))
print("Aposentadoria por Tempo de Contribuição (com pedágio):", data_ap_tempo.strftime("%d/%m/%Y"))