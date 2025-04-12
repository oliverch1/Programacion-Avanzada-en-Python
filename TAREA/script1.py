# -*- coding: utf-8 -*-
#%%
def factores_primos(num: int) -> list[int]:
    """
    Retona los factores primos de un numero

    Parameters
    ----------
    num : INT

    Returns
    -------
    Lista con los factores primos (INT)

    """
    factores: list[int] = []
    if num < 1 or not isinstance(num, int):
        return factores
    
    div: int = 2
        
    while num != 1:
        if num % div == 0:
            factores.append(div)
            num //= div    # num = num // div
        else:
            div += 1
            
    return factores
            

#%%
def circunferencia(radio: int, centro: tuple[int, int]) -> float:
    pass


#%%
def saluda(nombre: str) -> None:
    print(nombre.capitalize())
    
#%%
nombre: str = "Elvio Lado"
peso: int = 80
altura: float = 1.72

numero: tuple[float] = (1.20, 3.33, 12.8, 3.14)
pares: list[int] = [num for num in range(20) if num % 2 == 0]
meses: dict[int, str] = {1: 'Ene', 2: 'Feb', 3: 'Mar'}
valores: set[str] = {'1', '2', '3', '4', '3', '2', '5'}

#%%
def mi_factorial(num: int) -> int:
    if not isinstance(num, int):
        raise TypeError("El atributo 'num' debe ser un 'int'")
        
    if num < 0:
        raise ValueError("Al atributo 'num' debe ser mayor o igual o 0")

    if num == 0:
        return 1

    return num * mi_factorial(num - 1)        

#%%
def promedio_notas(notas: list[int, float]) -> float:
    return sum(notas) / len(notas)


#%%
def imc(peso: int | float, altura: int | float) -> float:
    return peso / altura ** 2

#%%
from typing import Optional

def valores_comunes(fila: list[int], columna: list[int]) -> Optional[set]:
    if len(set(fila) & set(columna)) > 0:
        return set(fila) & set(columna)
    else:
        return None


#%%
from typing import Any

def foo(val: Any) -> Any:
    pass


#%%
from typing import Callable

def func(func: Callable[[int], int]) -> Any:
    pass

#%%
num = 5

try:
    print(mi_factorial(num))
except ValueError:
    print("Error con el valor")
except TypeError:
    print("Error con el tipo de datos")
except Exception as e:
    print("ERROR:", e)
    
#%%
def foo(*args, **kwargs):
    for arg in args:
        print(arg)
        
    for k, v in kwargs.items():
        print(k, "->", v)
        
#%%
def range_letters(ini: str = 'A', end: str = 'Z', case: str = 'upper', reverse: bool = False):
    if not isinstance(ini, str) or not isinstance(end, str):
        raise TypeError("Los parametros 'ini' y 'end' debe ser un caracter valido")
        
    if all([ini.isalpha(), end.isalpha()]):
        if ini.upper() < end.upper():
            if not reverse:
                letter = ord(ini.upper()) - 1
                while letter < ord(end.upper()):
                    letter += 1
                    if case == 'upper':
                        yield chr(letter).upper()
                    elif case == 'lower':
                        yield chr(letter).lower()
                    else:
                        raise AttributeError("El parametro 'case' debe ser 'upper' o'lower'")
            else:
                letter = ord(end.upper()) + 1
                while letter > ord(ini.upper()):
                    letter -= 1
                    if case == 'upper':
                        yield chr(letter).upper()
                    elif case == 'lower':
                        yield chr(letter).lower()
                    else:
                        raise AttributeError("El parametro 'case' debe ser 'upper' o'lower'")
            
        else:
            raise ValueError("EL parametro 'ini' debe ser un caracter anterior a 'end'")
    else:
        raise ValueError("Los parametros 'ini' y 'end' deben estar en el rango 'A-Z'")        
        
        
    
#%%
for letter in range_letters('b', 's', reverse=True):
    print(letter)
    
#%%
gen = range_letters('b', 's', reverse=True)

while True:
    try:
        print(next(gen))
    except StopIteration:
        break

    
#%%
from collections import Counter
from random import randint

chars = [chr(randint(ord('a'), ord('z'))) 
         for _ in range(100)]
count = Counter(chars)
print(count)

#%%
count['f']

#%%
count.most_common(3)

#%%
from collections import deque

buffer = deque(['a', 'b', 'c', 'd', 'e', 'f'])
print(buffer[3])

#%%
buffer.append('g')
print(buffer)

#%%
buffer.appendleft('Z')
print(buffer)

#%%
val = buffer.pop()
print(buffer)

#%%
val = buffer.popleft()
print(val)
print(buffer)

#%%
buffer = deque([1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
               maxlen=10)
buffer

#%%
buffer.append(11)
print(buffer)

#%%
# GESTION DE TIEMPO
# time
# datetime

#%%
# TIME
import time

time_now = time.localtime()
print(time_now)
print(time_now.tm_year)

#%%
print(time.asctime())   # ASCII Time

#%%
time_now = time.time()
print(time_now)

#%%
time.gmtime()

#%%
time.strftime("%d/%m/%Y %H:%M:%S", time.localtime())

#%%
time.strptime("10:32 4/3", "%H:%M %d/%m")  # p: parse

#%%
from time import sleep

num = 10

while num > 0:
    print(num)
    num -= 1
    sleep(1)

#%%
from datetime import datetime
    
#%%
time_past = datetime(2020, 12, 14, 1, 20, 0)
print(time_past)

#%%
datetime.now() - time_past

#%%
born = datetime(2009, 12, 4)
datetime.now() - born

#%%
from datetime import timedelta

flor = datetime(2024, 12, 10)
delta = timedelta(days=100)
flor + delta

#%%
print(f"{datetime.now():%d/%m/%Y}")

#%%
start = datetime.now()
delta = timedelta(weeks=1)
date = start

for idx, _ in enumerate(range(16), start=1):
    print(f"{idx:0>2}. {date:%d/%m/%Y}")
    date += delta
    
#%%
num = 23
print(f"b{num:0b}")
print(f"0x{num:0x}H")

#%%
num = 92_283_873
print(f"{num:,.2f}")

#%%
print(round(11.5))
print(round(12.5))

#%%
# DECORADORES
def sumar(num1, num2):
    return num1 + num2


S = sumar 
print(type(S))

#%%
S(3, 10) 

#%%
print(factores_primos(19028122927))

#%%
from time import perf_counter

def test_performance(num: int) -> int:
    start_time = perf_counter()
    result = factores_primos(num)
    end_time = perf_counter()
    print(f"Tiempo requerido: {end_time - start_time} seg")
    return result


test_performance(1902812292731)

#%%
def test_performance(func):
    def wrapper(*args, **kwargs):
        start_time = perf_counter()
        result = func(*args, **kwargs)
        end_time = perf_counter()
        print(f"Tiempo requerido: {end_time - start_time} seg")
        return result
    
    return wrapper


wrapper = test_performance(mi_factorial)
value = wrapper(25)
print(value)

#%%
@test_performance
def factores_primos(num: int) -> list[int]:
    factores: list[int] = []
    if num < 1 or not isinstance(num, int):
        return factores
    
    div: int = 2
        
    while num != 1:
        if num % div == 0:
            factores.append(div)
            num //= div    # num = num // div
        else:
            div += 1
            
    return factores
            

        
print(factores_primos(98383737))  

#%%
def show_voltages(func):
    def wrapper(str_data: str):
        print("DataIn:", str_data)
        result = func(str_data)
        return result
    
    return wrapper


@show_voltages
def get_mean_voltage(values: str) -> float:
    voltages = list(map(lambda x: float(x), values.split(',')))
    return sum(voltages) / len(voltages)


get_mean_voltage("12.4,14.2,12.8,11.9,13.8")

