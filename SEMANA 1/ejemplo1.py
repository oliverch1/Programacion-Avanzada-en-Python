
# Type Hints

nombre: str = "Bruno Fernandes"
altura: float = 1.75
peso: int = 70

#print(f"Nombre: {nombre}\nAltura: {altura}\nPeso: {peso}")

pares: list[int] = [num for num in range(20) if num%2==0]
meses: dict[int, str] = dict(zip([1,2,3,4,5,6,7,8,9,10,11,12],["enero","febrero","marzo","abril","mayo",
                                                               "junio","julio","agosto","septiembre","octubre",
                                                               "noviembre", "diciembre"]))
names: set[str] = {"Elvio", "Dina", "Elmer", "Elvio"}

#print(pares) #genera una lista
#print(meses) #genera un diccionario
#print(names) #genera una lista sin valores repetidos}

#%%
#CALCULANDO EL PROMEDIO DE NOTAS
import random
def promedio_notas(notas: list[float]) -> float:
    return sum(notas)/len(notas)

notas: list[float] = []
for _ in range(20):
    if random.choice([True,False]):
        nota = round(random.uniform(0,20),2)
    else:
        nota = random.randint(0,20)
    notas.append(nota)

#print(f"Notas: {notas}\nPromedio de notas: {promedio_notas(notas):.2f}")

#%%
#DATOS EN COMUN DE FILAS Y COLUMNAS
from typing import Optional
def valores_comun(fila: list[int], columna: list[int]) -> Optional[set]:
    if len(set(fila) & set(columna)) > 0:
        return set(fila) & set(columna)
    else:
        None

fila = random.sample(range(0,20),10)
columna = random.sample(range(0,20),10)

#print(f"Filas: {fila}\nColumnas: {columna}\n\nValores Comunes: {valores_comun(fila,columna)}")

#%%
#CALCULO DEL IMC
def IMC(altura: int | float, peso: int | float) -> float:
    return peso/altura**2

peso = round(random.normalvariate(70,10),2)
peso = min(max(peso,50),100)
altura = round(random.normalvariate(1.70,0.1),2)
altura = min(max(altura,1.50),2.00)

#print(f"Peso: {peso}kg\nAltura: {altura}m\nIMC: {IMC(altura,peso):.2f}")

#%%
from Factorial import factorial
import time

while True:
    num = input("Ingrese un numero: ")
    try:
        num = int(num)
        if num < 0:
            print("Ingrese un numero positivo")
            time.sleep(2)
        else:
            break
    except ValueError:
        print("Error, ingrese un numero entero positivo")
        time.sleep(2)

#print(f"El factorial de {num} es {factorial(num)}")
