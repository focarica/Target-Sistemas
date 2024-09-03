# 4) Escreva um programa na linguagem que desejar onde calcule o percentual de representação que cada estado teve dentro do valor total mensal da distribuidora.  

# OBS: Foi utilizado valores medios para os demais estados.

estados = {
    'SP': 67836.43, 'RJ': 36678.66, 'MG': 29229.88, 'ES': 27165.48, 'AC': 864.76, 
    'AL': 864.76, 'AP': 864.76, 'AM': 864.76, 'BA': 864.76, 'CE': 864.76, 'DF': 864.76, 
    'GO': 864.76, 'MA': 864.76, 'MT': 864.76, 'MS': 864.76, 'PA': 864.76, 'PB': 864.76, 
    'PE': 864.76, 'PI': 864.76, 'PR': 864.76, 'RN': 864.76, 'RO': 864.76, 'RR': 864.76, 
    'RS': 864.76, 'SC': 864.76, 'SE': 864.76, 'TO': 864.76
}
faturamentoTotal = sum([i for i in estados.values()])

print("Percentual na faturação")
for estado, valor in estados.items():
    print(f"{estado} - {(valor / faturamentoTotal) * 100: .4f} %")