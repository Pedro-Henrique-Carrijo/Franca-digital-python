def soma_impares_multiplos_de_3():
    soma = 0
    for i in range(1, 501):
        if i % 2 != 0 and i % 3 == 0:
            soma += i
    return soma

resultado = soma_impares_multiplos_de_3()
print("Soma dos ímpares múltiplos de 3 de 1 até 500:", resultado)
