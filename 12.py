def pares():
    pares = []
    for i in range(1, 101):
        if i % 2 == 0:
            pares.append(i)
    return pares

resultado = ares()
print("Esses são os números pares de 1 a 100:", resultado)
