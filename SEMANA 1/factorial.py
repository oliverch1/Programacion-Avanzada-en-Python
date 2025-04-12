def factores_primos(n):
    factores = []
    div = 2

    if not isinstance(n, int) or n<2:
        return factores
    else:
        while n!=1:
            if n%div==0:
                factores.append(div)
                n//=div
            else:
                div +=1
    return factores


num = int(input("ingrese un numero entero: "))
lista = factores_primos(num)
print(f"\nlos factores primos son:\n{lista}")

