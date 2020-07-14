import time

import sys
sys.setrecursionlimit(1000000)

def factorial(n):
    respuesta = 1
    while n > 1:
        respuesta *=n
        n -= 1
    return respuesta

""" Implementación recursiva """
def factorial_r(n):
    if n == 1:
        return 1
    return n * factorial_r(n - 1)

if __name__ == "__main__":
    n = 1000
    comienzo =  time.time()
    factorial(n)
    final = time.time()
    print(comienzo - final)
    comienzo2 =  time.time()
    factorial_r(n)
    final2 = time.time()
    print(comienzo2 - final2)