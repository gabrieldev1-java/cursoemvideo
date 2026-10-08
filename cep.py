import requests
while True:
    cep = input('CEP (8 números): ').strip()
    if len(cep) == 8 and cep.isdigit():
        break
    print('ERRO! O CEP deve ter exatamente 8 números.')

try:
    resposta = requests.get(f'https://viacep.com.br/ws/{cep}/json/', timeout=5)
    resposta.raise_for_status()  # gera erro se o status não for 200
    dados = resposta.json()
except requests.exceptions.RequestException:
    print('Não foi possível acessar a API. Verifique sua conexão.')
else:
    if 'erro' in dados:  # a ViaCEP responde {"erro": true} se o CEP não existe
        print('CEP não encontrado.')
    else:
        print(f'Rua: {dados["logradouro"]}')
        print(f'Bairro: {dados["bairro"]}')
        print(f'Cidade: {dados["localidade"]} - {dados["uf"]}')