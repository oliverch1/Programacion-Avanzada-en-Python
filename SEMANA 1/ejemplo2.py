# *ARGS **KWARGS
from typing import Any

def  foo(*args: str, **kwargs: str) -> Any:
    for arg in args:
        print(arg)
    for k,v in kwargs.items():
        print(k,'->',v)

#print(f"{foo('A')}\n{foo('A','B','C')}\n{foo(num1=1)}\n{foo(num1=1,num2=2,num3=3)}\n{foo('A','B','C',num1=1,num2=2,num3=3)}")

#%%

# GENERADORES CON yield
import time
def rango_letras(inicio: str='A', fin: str='Z', caso: str='upper', reverso: bool=False):
    if not isinstance(inicio, str) or not isinstance(fin, str):
        raise TypeError
    if all([inicio.isalpha(), fin.isalpha()]):
        inicio_ord = ord(inicio.upper())
        fin_ord = ord(fin.upper())
        
        if not reverso:
            if inicio_ord > fin_ord:
                raise ValueError("El inicio debe ser menor que el fin cuando reverso=False")
            letra = inicio_ord - 1
            while letra < fin_ord:
                letra += 1
                if caso == 'upper':
                    yield chr(letra).upper()
                elif caso == 'lower':
                    yield chr(letra).lower()
                else:
                    raise AttributeError("El caso debe ser 'upper' o 'lower'")
        else:
            if inicio_ord < fin_ord:
                raise ValueError("El inicio debe ser mayor que el fin cuando reverso=True")
            letra = inicio_ord + 1
            while letra > fin_ord:
                letra -= 1
                if caso == 'upper':
                    yield chr(letra).upper()
                elif caso == 'lower':
                    yield chr(letra).lower()
                else:
                    raise AttributeError("El caso debe ser 'upper' o 'lower'")
    else:
        raise ValueError("Las entradas deben ser letras del alfabeto")
    
gen = rango_letras('A', 'C')
#print(next(gen))
#print(next(gen))
#print(next(gen))
#print(next(gen))

for letra in rango_letras('C','A',reverso=True):
    #print(letra)
    #time.sleep(1)
    pass
