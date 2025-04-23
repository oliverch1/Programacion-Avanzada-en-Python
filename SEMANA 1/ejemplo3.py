#LIBRERIA COLLECTIONS

#%%
#COUNTER
from collections import Counter
from random import randint

letras = [chr(randint(ord('a'),ord('z'))) for _ in range(100)]
count = Counter(letras)
#print(count)

#%%
#DEQUE
from collections import deque

buffer = deque(['b','c','d','e','f','g'])
#print(buffer)

buffer.append('h')
#print(buffer)

buffer.appendleft('a')
#print(buffer)

val = buffer.pop()
#print(buffer, val, sep = ' -> ')

val = buffer.popleft()
#print(buffer, val, sep = ' -> ')

#%%
#NAMETUPLES
from collections import namedtuple

Alumno = namedtuple('Alumno', ['nombre','apellido','codigo'])

alumno1 = Alumno('Alvaro','Meza','u20201b349')
print(alumno1.nombre)
print(alumno1.codigo)
print(alumno1)