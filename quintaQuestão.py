# 5) Escreva um programa que inverta os caracteres de um string. 

def invertString(string: str) -> str:
    p1, p2 = string[0], string[-1]
    
    string = list(string)
    
    for i in range(len(string)//2):
        string[i], string[-1-i] = p2, p1
        
        p1, p2 = string[i+1], string[-1-(i+1)]
        
    return ''.join(string)
    

print(invertString("hoje"))
