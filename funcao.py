import requests

def buscar_carta(nome_carta):
    url = f"https://db.ygoprodeck.com/api/v7/cardinfo.php?name={nome_carta.replace(' ', '%20')}"
    response = requests.get(url)
    
    if response.status_code == 200:
        dados = response.json()
        carta = dados['data'][0]

        print(f"Nome: {carta['name']}")
        print(f"Tipo: {carta['type']}")
        print(f"Atributo: {carta.get('attribute', 'N/A')}")
        print(f"Descrição: {carta['desc']}")
        print(f"Nível: {carta.get('level', 'N/A')}")
        print(f"Ataque: {carta.get('atk', 'N/A')}")
        print(f"Defesa: {carta.get('def', 'N/A')}")
        print(f"Imagem: {carta['card_images'][0]['image_url']}")
    else:
        print("Carta não encontrada.")

# Exemplo de uso
nome = input("Digite o nome da carta Yu-Gi-Oh!: ")
buscar_carta(nome)
