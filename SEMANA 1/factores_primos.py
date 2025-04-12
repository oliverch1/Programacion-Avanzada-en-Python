def factores_primos(n):
    '''factores primos(n)   Funcion que retorna los factores primos de un numero
    
    Parametros:
        - n: int
        
    Uso:
        factores_primos(12)  -> [2, 2, 3]'''
    if n < 1 or not isinstance(n, int):
        return []
    
    div = 2
    factores = []
    # Lazo que encuentra los divisores del numero (factores)
    while n != 1:    # is not
        # Si se tiene un factor, se guarda en la lista de salida
        if n % div == 0:
            factores.append(div)
            n //=  div   # n = n // div
        else:
            # ...de lo contrario se pasa a considerar el siguiente posible divisor
            div += 1     # div = div + 1
            
    return factores

print(factores_primos(360))