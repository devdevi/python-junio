goal = int(input("Ingrese un numero: "))
epsilon = 0.01
loop = epsilon**2
answer = 0.0

while abs(answer**2 - goal) >= epsilon and answer <= goal:
    answer += loop

if abs(answer**2) - goal >= epsilon:
    print(f"No se encontro la raiz cuadrada de {goal}")
else:
    print(f"La raiz cuadrada de {goal} es {answer} ")
