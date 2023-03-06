fat_mensal = [
	{
		"dia": 1,
		"valor": 22174.1664
	},
	{
		"dia": 2,
		"valor": 24537.6698
	},
	{
		"dia": 3,
		"valor": 26139.6134
	},
	{
		"dia": 4,
		"valor": 0.0
	},
	{
		"dia": 5,
		"valor": 0.0
	},
	{
		"dia": 6,
		"valor": 26742.6612
	},
	{
		"dia": 7,
		"valor": 0.0
	},
	{
		"dia": 8,
		"valor": 42889.2258
	},
	{
		"dia": 9,
		"valor": 46251.174
	},
	{
		"dia": 10,
		"valor": 11191.4722
	},
	{
		"dia": 11,
		"valor": 0.0
	},
	{
		"dia": 12,
		"valor": 0.0
	},
	{
		"dia": 13,
		"valor": 3847.4823
	},
	{
		"dia": 14,
		"valor": 373.7838
	},
	{
		"dia": 15,
		"valor": 2659.7563
	},
	{
		"dia": 16,
		"valor": 48924.2448
	},
	{
		"dia": 17,
		"valor": 18419.2614
	},
	{
		"dia": 18,
		"valor": 0.0
	},
	{
		"dia": 19,
		"valor": 0.0
	},
	{
		"dia": 20,
		"valor": 35240.1826
	},
	{
		"dia": 21,
		"valor": 43829.1667
	},
	{
		"dia": 22,
		"valor": 18235.6852
	},
	{
		"dia": 23,
		"valor": 4355.0662
	},
	{
		"dia": 24,
		"valor": 13327.1025
	},
	{
		"dia": 25,
		"valor": 0.0
	},
	{
		"dia": 26,
		"valor": 0.0
	},
	{
		"dia": 27,
		"valor": 25681.8318
	},
	{
		"dia": 28,
		"valor": 1718.1221
	},
	{
		"dia": 29,
		"valor": 13220.495
	},
	{
		"dia": 30,
		"valor": 8414.61
	}
]

# init variaveis
# inicia o maior e menor do faturamento sendo como o primeiro item da lista
total_valor = 0
higher = {"dia": fat_mensal[0]['dia'], "valor": fat_mensal[0]['valor']}
lower = {"dia": fat_mensal[0]['dia'], "valor": fat_mensal[0]['valor']}

# pega o maior valor e menor salvando o dia também
# calcula o total do valor para fazer a média depois
for i in range(1, len(fat_mensal)):
    if (fat_mensal[i]['valor'] != 0.0):
        total_valor += fat_mensal[i]['valor']
    if (fat_mensal[i]['valor'] >= higher['valor']):
        higher['dia'] = fat_mensal[i]['dia']
        higher['valor'] = fat_mensal[i]['valor']
    if (fat_mensal[i]['valor'] <= lower['valor'] and fat_mensal[i]['valor'] != 0.0):
        lower['dia'] = fat_mensal[i]['dia']
        lower['valor'] = fat_mensal[i]['valor']

# media
media = total_valor / len(fat_mensal)

# vare a lista novamente para selecionar os items maiores que a média
total_dias = 0
for i in fat_mensal:
    if (i['valor'] > media):
        total_dias+=1

# printa os dados obtidos
print('------------------------------------')
print('Menor faturamento do mês:')
print(f" - valor: {lower['valor']}")
print(f" - dia:   {lower['dia']}\n")
print("Maior faturamento do mês:")
print(f" - valor: {higher['valor']}")
print(f" - dia:   {higher['dia']}\n")
print(f"Numero de dias em que o faturamento\nfoi maior que do mês do mês: {total_dias}")
print('------------------------------------')
    

