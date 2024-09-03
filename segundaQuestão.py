# 2) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores 
# (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, 
# ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência. 

def isInFibonacciSeq(value: int) -> bool:
    old = 0
    current = 1
    
    nums = [old, current]
    
    while current <= value:
        aux = current
        current += old
        old = aux

        nums.append(current)
        
    return (f"O numero {value} está na sequencia de Fibonacci" 
            if value in nums
            else f"O numero {value} não esta na sequencia de Fibonacci")


value = int(input("Digite um numero para verificar se ele esta na sequencia de Fibonacci: "))
print(isInFibonacciSeq(value))


