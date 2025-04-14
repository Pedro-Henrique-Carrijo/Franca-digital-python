def divisiveis_por_7():
    contador = 0
    for i in range(1, 1001):
        if i % 7 == 0:
            contador += 1
    return contador

resultado = divisiveis_por_7()
print("Quantidade de números entre 1 e 1000 divisíveis por 7:", resultado)
