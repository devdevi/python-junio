def f(x):
    respuesta = 0

    for i in range(1000):
        respuesta += 1

    print(respuesta)

    for i in range(x):
        respuesta += x
    print(respuesta)

    for i in range(x):
        print(i, 'Respuesta')
        for j in  range(x):
            print(j)
            respuesta +=1
            respuesta +=1
    print(respuesta)
    return respuesta

f(0)
x=2
print(2x)*8