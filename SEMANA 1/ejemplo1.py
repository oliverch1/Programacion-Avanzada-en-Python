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
#print(names) #genera una lista sin valores repetidos

