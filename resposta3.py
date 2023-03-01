 import json

# abre o arquivo JSON com os valores de faturamento diário
with open('faturamento.json') as json_file:
    data = json.load(json_file)

    # inicializa variáveis
    faturamento = []
    soma = 0
    dias_acima_media = 0

    # lê os valores de faturamento e armazena na lista faturamento
    for item in data['faturamento']:
        valor = float(item['valor'])
        faturamento.append(valor)
        soma += valor

    # calcula o menor e o maior valor de faturamento
    menor_valor = min(faturamento)
    maior_valor = max(faturamento)

    # calcula a média mensal de faturamento
    media_mensal = soma / len(faturamento)

    # conta o número de dias em que o faturamento foi superior à média mensal
    for valor in faturamento:
        if valor > media_mensal:
            dias_acima_media += 1

    # imprime os resultados
    print(f"Menor valor de faturamento: R${menor_valor:.2f}")
    print(f"Maior valor de faturamento: R${maior_valor:.2f}")
    print(f"Número de dias com faturamento acima da média mensal: {dias_acima_media}")
