import os 
import time
os.system('cls')

numero = int(input('digite um numero: '))

for i in range(1,11):
    print(i)
    resultado = numero * i
    print(f'{numero} x {i} = {resultado}')
    time.sleep(1)