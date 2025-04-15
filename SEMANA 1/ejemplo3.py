#LIBRERIA COLLECTIONS

#%%
#COUNTER
from collections import Counter
from random import randint

letras = [chr(randint(ord('a'),ord('z'))) for _ in range(100)]
counter = Counter(letras)
print(counter)
