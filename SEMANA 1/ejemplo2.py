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
def rango_letras(inicio: str='A', fin: str='Z', caso: str='upper', reverso: bool=False):
    if not isinstance(inicio, str) or not isinstance(fin, str):
        raise TypeError
    if all([inicio.isalpha(),fin.isalpha()]):
        if inicio.upper() < fin.upper():
            if not reverso:
                letra = ord(inicio.upper())-1
                while letra < ord(fin.upper()):
                    letra += 1
                    if caso == 'upper':
                        yield chr(letra).upper()
                    elif caso == 'lower':
                        yield chr(letra).lower()
                    else:
                        raise AttributeError
            else:
                letra = ord(inicio.upper()) + 1
                while letra > ord(fin.upper()):
                    letra -= 1
                    if caso == 'upper':
                        yield chr(letra).upper()
                    elif caso == 'lower':
                        yield chr(letra).lower()
                    else:
                        raise AttributeError
        else:
            raise ValueError
    else:
        raise ValueError

gen = rango_letras('A', 'C')
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen)) 