#TIME
import time
time_now = time.localtime()
print(time_now)
print(f"{time_now.tm_hour}:{time_now.tm_min}")
print(f"han pasado {time_now.tm_yday} dias desde el 1 de enero de {time_now.tm_year}")