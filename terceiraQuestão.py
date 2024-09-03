import json 

def deserializeJson(file: str) -> list | str:
    try:
        with open(file, 'r') as jsonFile:
            return json.load(jsonFile)
    except FileNotFoundError:
        return "Erro ao localizar o arquivo"

def faturamentoMin(data: list) -> str:
    # Contando com os valores 0.0
    # return f"O menor valor de faturamento foi de R${min([data[i]['valor'] for i in range(len(data))])}"
    
    faturamentos = [data[i]['valor'] for i in range(len(data)) if data[i]['valor'] > 0]
    
    return f"O menor valor de faturamento foi de R$ {min(faturamentos)}."

def faturamentoMax(data: list) -> str:
    faturamentos = max([data[i]['valor'] for i in range(len(data))])
    
    return f"O maior valor de faturamento foi de R$ {faturamentos}."

def maiorMedia(data: list) -> str:
    listaFaturamentos = [data[i]['valor'] for i in range(len(data)) if data[i]['valor'] > 0]
    mediaFaturamento = sum(listaFaturamentos) / len(listaFaturamentos)
    
    qtDias = len([data[i]['valor'] for i in range(len(data)) if data[i]['valor'] > mediaFaturamento])
    
    return f"Em {qtDias} dias o faturamento diario foi maior que a media mensal (R${mediaFaturamento: .4f})."

data = deserializeJson('dados.json')
print(faturamentoMin(data))
print(faturamentoMax(data))
print(maiorMedia(data))