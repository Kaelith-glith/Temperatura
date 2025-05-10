import requests

nome = input('Digite seu nome: ')
idade = int(input('Digite sua idade: '))

if idade <18:
    print(f'Voce é menor de idade, {nome}.')

else:
    print(f'Bem-vindo(a) ao sistema, {nome}!')

def obter_temperatura(cidade):
    chave_api = "655152422da656a68cbd7eaf5374f0bf"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={chave_api}&lang=pt_br&units=metric"

    resposta = requests.get(url)
    dados = resposta.json()

    if resposta.status_code == 200:
        temperatura = dados['main']['temp']
        descricao = dados['weather'][0]['description']
        print(f"Temperatura atual em {cidade}: {temperatura}°C, {descricao} \n tenha um otimo dia {nome}!")
    else:
        print("Cidade não encontrada ou erro na API.")

# Exemplo de uso:
cidade = input("Digite o nome da cidade: ")
obter_temperatura(cidade)
