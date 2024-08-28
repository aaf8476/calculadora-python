def resto_divisao (num1, num2):
    if num2 != 0:
        return num1 % num2
    else:
        return "Erro na divisão"
    
resultado = resto_divisao (25,0)
print(resultado)