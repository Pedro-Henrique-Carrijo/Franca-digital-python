def fatorial(numero):
    resultado = 1
    for i in range(1, numero + 1):
        resultado *= i
    return resultado

numero = int(input("Me fale um numero para calcular o fatorial: "))
resultado = fatorial(numero)
print(f"O fatorial de {numero} é {resultado}.")
