# define um dicionário com os valores de faturamento por estado
faturamento = {
    'SP': 67836.43,
    'RJ': 36678.66,
    'MG': 29229.88,
    'ES': 27165.48,
    'Outros': 19849.53
}

# calcula o total mensal de faturamento
total_mensal = sum(faturamento.values())

# calcula e imprime o percentual de representação de cada estado
for estado, valor in faturamento.items():
    percentual = (valor / total_mensal) * 100
    print(f"{estado}: {percentual:.2f}%")
