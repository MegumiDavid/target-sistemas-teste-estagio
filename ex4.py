# 4

faturamento = {
    "SP": 67836.43,
    "RJ": 36678.66,
    "MG": 29229.88,
    "ES": 27165.48,
    "OUTROS": 19849.53
}

# calcula o total do faturamento
total = 0
for v in faturamento.values():
    total += v

# printa o valor percentual de cada estado
for k,v in faturamento.items():
    fat_estado = (v/total) * 100
    num_format = float("{:.2f}".format(fat_estado))
    print(f'{k}: {num_format}%')